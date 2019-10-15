"""
module textiles;
"""

from abc import ABC, abstractmethod
import pandas


def convert_to_float(value):
    """
    Преобразование значений в столбцах датафрейма;
    :param value: float
    :return: float
    """
    value = str(value)
    value = value.replace(",", ".")
    value = round(float(value), 2)
    return value


########################################################################################################################


class DataComponent(ABC):
    """
    "Внешний интерфейс" для классов-компонентов;
    """

    # Основной датафрейм; Объект pandas.DataFrame;
    _dataframe = None
    _length = 0

    def dataframe(self) -> pandas.DataFrame:
        """
        Основной датафрейм;
        :return: pandas.DataFrame
        """
        return self._dataframe

    def length(self) -> int:
        """
        Возвращает количество строк датафрейма;
        :return: int
        """
        return len(self._dataframe)


########################################################################################################################


class TextilesBase(ABC):
    """
    Базовый класс модуля; Содержит основные поля класса;
    """

    # Названия признаков (колонок) датафрейма;
    _feature_names = ['grave', 'internal_storage', 'warp_size', 'weft_size', 'type', 'condition',
                      'weaving_technique', 'warp_material', 'weft_material', 'warp_dyed',
                      'weft_dyed', 'twist_warp', 'twist_weft', 'angle_warp', 'angle_weft',
                      'warp_a', 'warp_b', 'weft_a', 'weft_b', 'warp_dens', 'weft_dens']

    _quartiles = None
    _outliers = None

    def __init__(self, filename):
        """
        Последовательно формируется основной датафрейм (из csv файла);
        Численные свойства датафрейма приводятся к типу float (self._normalize_features());
        """
        self._dataframe = pandas.read_csv(filename)
        self._format_features()
        self._normalize_features()
        self._density_coefficient()
        self._dataframe.dropna()
        self._get_quartiles()

    @callable
    def _filter_features(self):
        """
        """
        pass

    def _format_features(self):
        """
        Форматирует колонки датафрейма;
        """
        self._dataframe = pandas.DataFrame(self._dataframe[[
            'grave', 'internal_storage', 'warp_size', 'weft_size', 'type', 'condition',
            'weaving_technique', 'warp_material', 'weft_material', 'warp_dyed',
            'weft_dyed', 'twist_warp', 'twist_weft', 'angle_warp', 'angle_weft',
            'warp_a', 'warp_b', 'weft_a', 'weft_b', 'warp_dens', 'weft_dens']])

    def _normalize_features(self):
        """
        Converts warp and weft thread thick to float;
        """
        self._dataframe['warp_a'] = self._dataframe.warp_a.apply(convert_to_float)
        self._dataframe['warp_b'] = self._dataframe.warp_b.apply(convert_to_float)
        self._dataframe['weft_a'] = self._dataframe.weft_a.apply(convert_to_float)
        self._dataframe['weft_b'] = self._dataframe.weft_b.apply(convert_to_float)
        # рассчет средних значений толщин нитей по основе и по утку;
        # получаемые значения округляются до 2 знаков после запятой;
        self._dataframe['warp_mean'] = round((self._dataframe['warp_a'] + self._dataframe['warp_b']) / 2, 2)
        self._dataframe['weft_mean'] = round((self._dataframe['weft_a'] + self._dataframe['weft_b']) / 2, 2)

    def _density_coefficient(self):
        """
        "Коэффициент плотности" - соотношение плотности по основе к плотности по утку;
        """
        self._dataframe['density_coefficient'] = round(
            self._dataframe['warp_dens'] / self._dataframe['weft_dens'], 2)

    def _get_quartiles(self):
        """
        :return: null
        """
        # self._quartiles = Quartiles(self)


########################################################################################################################


class Textiles(TextilesBase, DataComponent):
    """
    Базовый класс модуля; Формирует pandas.Dataframe и предоставляет внешний интерфейс для описательных данных;
    """

    def filter_type(self, item_type):
        """
        Возвращает датафрейм, отфильтрованный по заданному типу;
        """
        return self._dataframe[self._dataframe['type'] == item_type]

    #     def unbalanced(self):
    #         """
    #         Выборка данных из подготовленного датафрейма;
    #         Предполагается, что для сбалансированных тканей разница между плотностью
    #         по основе и плотностью по утку не должна превышать 3 единиц;
    #         """
    #         return self._dataframe[abs(self._dataframe['warp_dens'] - self._dataframe['weft_dens']) > 3]

    def weaving_technique(self, technique):
        """
        Возвращает датафрейм, отфильтрованный по заданному типу
        ткацкого переплетения;
        """
        return self._dataframe[self._dataframe['weaving_technique'] == technique]

    def balanced(self):
        """
        Выборка данных из подготовленного датафрейма;
        Предполагается, что для сбалансированных тканей разница между плотностью
        по основе и плотностью по утку не должна превышать 3 единиц;
        """
        return self._dataframe[abs(self._dataframe['warp_dens'] - self._dataframe['weft_dens']) <= 3]

    def unbalanced(self):
        """
        """

    def create_outliers(self):
        """
        """
        if self._outliers is None:
            self._outliers = Outliers(self)

    def quartiles(self):
        """
        """
        if self._quartiles is not None:
            return self._quartiles
        return Quartiles(self)

    def outliers(self):
        """
        """
        if self._outliers is not None:
            return self._outliers
        return Outliers(self)


########################################################################################################################


class Quartiles:
    """
    Квартили для среднего значения толщин нитей и средних значений плотности тканей;
    """

    __warp_thick_1, __warp_thick_2, __warp_thick_3 = [0, 0, 0]
    __weft_thick_1, __weft_thick_2, __weft_thick_3 = [0, 0, 0]
    __warp_dens_1, __warp_dens_2, __warp_dens_3 = [0, 0, 0]
    __weft_dens_1, __weft_dens_2, __weft_dens_3 = [0, 0, 0]

    def __init__(self, textiles: Textiles):
        """
        """
        [self.__warp_thick_1, self.__warp_thick_2, self.__warp_thick_3] =\
            textiles.dataframe()['warp_mean'].quantile([0.25, 0.5, 0.75])
        [self.__weft_thick_1, self.__weft_thick_2, self.__weft_thick_3] =\
            textiles.dataframe()['weft_mean'].quantiles([0.25, 0.5, 0.75])
        [self.__warp_dens_1, self.__warp_dens_2, self.__warp_dens_3] =\
            textiles.dataframe()['warp_dens'].quantile([0.25, 0.5, 0.75])
        [self.__weft_dens_1, self.__weft_dens_2, self.__weft_dens_3] =\
            textiles.dataframe()['weft_dens'].quantile([0.25, 0.5, 0.75])

    def warp_thick(self, number: int) -> float:
        """
        :return: float
        """
        thick = {1: self.__warp_thick_1, 2: self.__warp_thick_2, 3: self.__warp_thick_3}
        if number in thick:
            return thick[number]
        return 0.0

    def weft_thick(self, number: int) -> float:
        """
        :return: float
        """
        thick = {1: self.__weft_thick_1, 2: self.__weft_thick_2, 3: self.__weft_thick_3}
        if number in thick:
            return thick[number]
        return 0.0

    def warp_dens(self, number: int):
        """
        :return:
        """
        dens = {1: self.__warp_dens_1, 2: self.__warp_dens_2, 3: self.__warp_dens_3}
        if number in dens:
            return dens[number]
        return 0.0

    def weft_dens(self, number: int) -> float:
        """
        :return:
        """
        dens = {1: self.__warp_dens_1, 2: self.__warp_dens_2, 3: self.__warp_dens_3}
        if number in dens:
            return dens[number]
        return 0.0


########################################################################################################################


class Balanced(DataComponent):
    """
    Textiles class for "balanced" textiles;
    """

    def _filter_features(self):
        """
        """
        pass


########################################################################################################################


class Unbalanced(DataComponent):
    """
    Textiles class for "unbalanced" textiles;
    """

    def _filter_features(self):
        """
        """
        pass


########################################################################################################################


class Outliers:
    """
    Выбросы для основного датафрейма Textiles;
    """
    __outliers_dataframe = None
    __cleared_dataframe = None

    def __init__(self, textiles: Textiles):
        """
        """
        self.__clear(textiles)

    def __clear(self, textiles: Textiles):
        """
        Последовательно исключает из датафрейма выбросы по среднему значению толщин нитей;
        """
        self.__cleared = textiles.dataframe()[
            textiles.dataframe().warp_mean < (warp_mean_quantile_3 + 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
            ]
        self.__cleared = self.__cleared[
            self.__cleared.warp_mean > (warp_mean_quantile_1 - 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
            ]
        self.__cleared = self.__cleared[
            self.__cleared.weft_mean < (weft_mean_quantile_3 + 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
            ]
        self.__outliers = self.__outliers[
            self.__outliers.weft_mean > (weft_mean_quantile_1 - 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
            ]

    def __outliers(self, textiles: Textiles):
        """
        "Выбросы" в данных;
        """
        self.__cleared = self.__dataframe[
            self.__dataframe.warp_mean < (warp_mean_quantile_3 + 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
            ]
        self.__cleared = self.__cleared[
            self.__cleared_dataframe.warp_mean > (
                        warp_mean_quantile_1 - 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
            ]
        self.__cleared = self.__cleared[
            self.__cleared_dataframe.weft_mean < (
                        weft_mean_quantile_3 + 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
            ]
        self.__outliers = self.__outliers[
            self.__outliers_dataframe.weft_mean > (
                        weft_mean_quantile_1 - 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
            ]

    def cleared_dataframe(self):
        """
        Возвращает датафрейм, очищенный от "выбросов";
        """
        return self.__cleared_dataframe

    def outliers(self):
        """
        Возвращает датафрейм "выбросов";
        """
        return self.__outliers_dataframe
