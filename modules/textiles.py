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


class Textiles:
    """
    Базовый класс модуля; Формирует pandas.Dataframe
    """
    __dataframe = None
    __dataframe_length = None
    def __init__(self, filename):
        """
        """
        self.__dataframe = pandas.read_csv(filename)
        self.__format_features()
        self.__normalize_features()
        self.__density_coefficient()
        self.__dataframe.dropna()
    def dataframe(self):
        """
        Returns dataframe;
        """
        return self.__dataframe
    def weaving_technique(self, technique):
        """
        Returns dataframe filtered by weaving_technique;
        """
        return self.__dataframe[self.__dataframe['weaving_technique'] == technique]
    def balanced(self):
        """
        """
        return self.__dataframe[abs(self.__dataframe['warp_dens'] - self.__dataframe['weft_dens']) <= 3]
    def unbalanced(self):
        """
        """
        dataframe[abs(dataframe['warp_dens'] - dataframe['weft_dens']) > 3]
    def __format_features(self):
        """
        Formats dataframe columns;
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
        self.__dataframe['warp_mean'] = round((self.__dataframe['warp_a'] + self.__dataframe['warp_b']) / 2, 2)
        self.__dataframe['weft_mean'] = round((self.__dataframe['weft_a'] + self.__dataframe['weft_b']) / 2, 2)
    def __density_coefficient(self):
        """
        Adds new column to dataframe - 'density_coefficient';
        """
        self.__dataframe['density_coefficient'] = round(
            self.__dataframe['warp_dens'] / self.__dataframe['weft_dens'],
            2)
    def __textiles_descriptive(self):
        """
        """


class TextileOutliers:
    """
    Textiles outliers and basic statistics;
    """
    __dataframe = None
    def __init__(self, dataframe: Textiles):
        """
        """
        self.__dataframe = dataframe
        self.__clear()
    def __clear(self):
        """
        Defines dataframe outliers;
        """
    def outliers(self):
        """
        Returns outliers;
        """

#######################################################################################################################

# # рассчет средних значений толщин нитей по основе и по утку;
# # получаемые значения округляются до 2 знаков после запятой;
# dataframe['warp_mean'] = round((dataframe['warp_a'] + dataframe['warp_b']) / 2, 2)
# dataframe['weft_mean'] = round((dataframe['weft_a'] + dataframe['weft_b']) / 2, 2)

# # "Коэффициент плотности" - соотношение плотности по основе к плотности по утку;
# dataframe['density_coefficient'] = round(dataframe['warp_dens'] / dataframe['weft_dens'], 2)

# # Выборка данных из подготовленного датафрейма;
# # Предполагается, что для сбалансированных тканей разница между плотностью
# # по основе и плотностью по утку не должна превышать 3 единиц;

# # Ткани с переплетением типа "рогожка";
# baskets = dataframe[dataframe['weaving_technique'] == 'basket']

# # выборка узких бинтов;
# narrow_bands = dataframe[dataframe['type'] == 'n_band']

# # выборка средних бинтов;
# middle_bands = dataframe[dataframe['type'] == 'm_band']

# # выборка широких бинтов;
# wide_bands = dataframe[dataframe['type'] == 'w_band']
