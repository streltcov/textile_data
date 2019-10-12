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


class TextilesBase(ABC):
    """
    Базовый класс модуля; Формирует pandas.Dataframe
    """
    _dataframe = None
    _dataframe_length = None
    _outliers = None
    _quartiles = None
    
    def __init__(self, filename):
        """
        """
        self._dataframe = pandas.read_csv(filename)
        self._format_features()
        self._normalize_features()
        self._density_coefficient()
        self._dataframe.dropna()

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

    def dataframe(self):
        """
        Возвращает основной датафрейм без филтрации по параметрам;
        """
        return self._dataframe


########################################################################################################################


class Textiles(TextilesBase):
    """
    Базовый класс модуля; Формирует pandas.Dataframe
    """

    def _filter_features(self):
        """
        """
        pass

    def item_type(self, item_type):
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
    
    def create_quantiles(self):
        """
        """
        if self._quartiles is None:
            self._quartiles = Quantiles(self)
    
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
        return None
    
    def outliers(self):
        """
        """
        if self._outliers is not None:
            return self._outliers
        return None


########################################################################################################################


class Balanced(TextilesBase):
    """
    Textiles class for "balanced" textiles;
    """

    def _filter_features(self):
        """
        """
        pass


########################################################################################################################


class Unbalanced(TextilesBase):
    """
    Textiles class for "unbalanced" textiles;
    """

    def _filter_features(self):
        """
        """
        pass


########################################################################################################################


class Quantiles:
    """
    """
    __warp_mean_quantile_1 = None
    __warp_mean_quantile_3 = None
    __weft_mean_quantile_1 = None
    __weft_mean_quantile_3 = None
    __warp_dens_quantile_1 = None
    __warp_dens_quantile_3 = None
    __weft_dens_quantile_1 = None
    __weft_dens_quantile_3 = None
    
    def __init__(self, textiles: Textiles):
        """
        """
        self.__warp_mean_quantile_1, self.__warp_mean_quantile_3 = textiles.dataframe().warp_mean.quantile([0.25, 0.75])
        self.__weft_mean_quantile_1, self.__weft_mean_quantile_3 = textiles.dataframe().weft_mean.quantile([0.25, 0.75])
        self.__warp_dens_quantile_1, self.__warp_dens_quantile_3 = textiles.dataframe().warp_dens.quantile([0.25, 0.75])
        self.__weft_dens_quantile_1, self.__weft_dens_quantile_3 = textiles.dataframe().weft_dens.quantile([0.25, 0.75])
    
    def quantile(self):
        """
        """


########################################################################################################################


class Outliers:
    """
    Textiles outliers and basic statistics;
    """
    __dataframe = None
    __outliers_dataframe = None
    __cleared_dataframe = None

    def __init__(self, textiles: Textiles):
        """
        """
        if textiles.quartiles() is None:
            textiles.create_quantiles()
        self.__dataframe = textiles.dataframe()
        self.__clear(textiles)

    def __clear(self, textiles: Textiles):
        """
        Defines dataframe outliers;
        """
        self.__cleared = self.__dataframe[
            self.__dataframe.warp_mean < (warp_mean_quantile_3 + 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
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
        Defines dataframe outliers;
        """
        self.__cleared = self.__dataframe[
            self.__dataframe.warp_mean < (warp_mean_quantile_3 + 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
        ]
        self.__cleared = self.__cleared[
            self.__cleared_dataframe.warp_mean > (warp_mean_quantile_1 - 1.5 * (warp_mean_quantile_3 - warp_mean_quantile_1))
        ]
        self.__cleared = self.__cleared[
            self.__cleared_dataframe.weft_mean < (weft_mean_quantile_3 + 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
        ]
        self.__outliers = self.__outliers[
            self.__outliers_dataframe.weft_mean > (weft_mean_quantile_1 - 1.5 * (weft_mean_quantile_3 - weft_mean_quantile_1))
        ]

    def cleared(self):
        """
        Возвращает датафрейм, очищенный от "выбросов";
        """
        return self.__cleared_dataframe

    def outliers(self):
        """
        Возвращает датафрейм "выбросов";
        """
        return self.__outliers_dataframe
