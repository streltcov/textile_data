"""
module textiles;
"""


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

class TextilesBase:
    """
    """
    __dataframe = None
    __dataframe_length = None
    
    def __init__(self, filename):
        """
        """
        self.__dataframe = pandas.read_csv(filename)


class Textiles(TextilesBase):
    """
    Базовый класс модуля; Формирует pandas.Dataframe
    """
    __dataframe = None
    __dataframe_length = None
    
    __quantiles = None

    def __init__(self, filename):
        """
        """
        self.__dataframe = pandas.read_csv(filename)
        self.__format_features()
        self.__normalize_features()
        self.__density_coefficient()
        self.__dataframe.dropna()
        self.__quantiles()

    def item_type(self, item_type):
        """
        Возвращает датафрейм, отфильтрованный по заданному типу;
        """
        return self.__dataframe[self.__dataframe['type'] == item_type]

    def unbalanced(self):
        """
        Выборка данных из подготовленного датафрейма;
        Предполагается, что для сбалансированных тканей разница между плотностью
        по основе и плотностью по утку не должна превышать 3 единиц;
        """
        return self.__dataframe[abs(self.__dataframe['warp_dens'] - self.__dataframe['weft_dens']) > 3]

    def __format_features(self):
        """
        Форматирует колонки датафрейма;
        """
        self.__dataframe = pandas.DataFrame(self.__dataframe[[
            'grave', 'internal_storage', 'warp_size', 'weft_size', 'type', 'condition',
            'weaving_technique', 'warp_material', 'weft_material', 'warp_dyed',
            'weft_dyed', 'twist_warp', 'twist_weft', 'angle_warp', 'angle_weft',
            'warp_a', 'warp_b', 'weft_a', 'weft_b', 'warp_dens', 'weft_dens']])

    def __normalize_features(self):
        """
        Converts warp and weft thread thick to float;
        """
        self.__dataframe['warp_a'] = self.__dataframe.warp_a.apply(convert_to_float)
        self.__dataframe['warp_b'] = self.__dataframe.warp_b.apply(convert_to_float)
        self.__dataframe['weft_a'] = self.__dataframe.weft_a.apply(convert_to_float)
        self.__dataframe['weft_b'] = self.__dataframe.weft_b.apply(convert_to_float)
        # рассчет средних значений толщин нитей по основе и по утку;
        # получаемые значения округляются до 2 знаков после запятой;
        self.__dataframe['warp_mean'] = round((self.__dataframe['warp_a'] + self.__dataframe['warp_b']) / 2, 2)
        self.__dataframe['weft_mean'] = round((self.__dataframe['weft_a'] + self.__dataframe['weft_b']) / 2, 2)

    def __density_coefficient(self):
        """
        "Коэффициент плотности" - соотношение плотности по основе к плотности по утку;
        """
        self.__dataframe['density_coefficient'] = round(
            self.__dataframe['warp_dens'] / self.__dataframe['weft_dens'],
            2)
    
        def dataframe(self):
        """
        Возвращает основной датафрейм без филтрации по параметрам;
        """
        return self.__dataframe

    def weaving_technique(self, technique):
        """
        Возвращает датафрейм, отфильтрованный по заданному типу
        ткацкого переплетения;
        """
        return self.__dataframe[self.__dataframe['weaving_technique'] == technique]

    def balanced(self):
        """
        Выборка данных из подготовленного датафрейма;
        Предполагается, что для сбалансированных тканей разница между плотностью
        по основе и плотностью по утку не должна превышать 3 единиц;
        """
        return self.__dataframe[abs(self.__dataframe['warp_dens'] - self.__dataframe['weft_dens']) <= 3]
    
    def create_quantiles():
        """
        """
        if is None self._quantiles:
            self.__quantiles = Quantiles(self)
    
    def create_outliers():
        """
        """
        if is None self.__outliers:
            self.__outliers = Outliers(self)
    
    def quantiles():
        """
        """
        if is not None self.quantiles:
            return self._quantiles
        raise QuantilesNotSetError()
    
    def outliers():
        """
        """
        if is not None self.__outliers:
            return self.__outliers
        raise OutliersNotSetError()

#     def __quantiles(self):
#         """
#         Вычисляет квартили для численных параметров датафрейма;
#         """
#         self.__warp_mean_quantile_1, self.__warp_mean_quantile_3 = self.__dataframe.warp_mean.quantile([0.25, 0.75])
#         self.__weft_mean_quantile_1, self.__weft_mean_quantile_3 = self.__dataframe.weft_mean.quantile([0.25, 0.75])
#         self.__warp_dens_quantile_1, self.__warp_dens_quantile_3 = self.__dataframe.warp_dens.quantile([0.25, 0.75])
#         self.__weft_dens_quantile_1, self.__weft_dens_quantile_3 = self.__dataframe.weft_dens.quantile([0.25, 0.75])

#     def __textiles_descriptive(self):
#         """
#         """


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
        self.__warp_mean_quantile_1, self.__warp_mean_quantile_3 = self.__dataframe.warp_mean.quantile([0.25, 0.75])
        self.__weft_mean_quantile_1, self.__weft_mean_quantile_3 = self.__dataframe.weft_mean.quantile([0.25, 0.75])
        self.__warp_dens_quantile_1, self.__warp_dens_quantile_3 = self.__dataframe.warp_dens.quantile([0.25, 0.75])
        self.__weft_dens_quantile_1, self.__weft_dens_quantile_3 = self.__dataframe.weft_dens.quantile([0.25, 0.75])
    
    def quantile():
        """
        """


class Outliers:
    """
    Textiles outliers and basic statistics;
    """
    __dataframe = None
    __outliers = None
    __cleared = None

    def __init__(self, textiles: Textiles):
        """
        """
        self.__textiles = textiles
        self.__dataframe = self.__textiles.dataframe()
        self.__clear()

    def __clear(self):
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

    def __outliers(self):
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

    def cleared(self):
        """
        Возвращает датафрейм, очищенный от "выбросов";
        """
        return self.__cleared

    def outliers(self):
        """
        Возвращает датафрейм "выбросов";
        """
        return self.__outliers
