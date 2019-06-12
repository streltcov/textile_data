"""
module textile_dataframes;
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


########################################################################################################################


def density_coefficient(dataframe):
    return dataframe


########################################################################################################################


# Основной датафрейм; Содержит все (неотфильтрованные) данные;
dataframe = pandas.read_csv('raw_data/dataframe.csv')
dataframe = pandas.DataFrame(dataframe[
                                 ['grave', 'internal_storage', 'size_warp', 'size_weft', 'type', 'condition',
                                  'weaving_technique',
                                  'warp_material', 'weft_material', 'warp_dyed', 'weft_dyed', 'twist_warp',
                                  'twist_weft', 'angle_warp', 'angle_weft',
                                  'warp_a', 'warp_b', 'weft_a', 'weft_b', 'warp_dens', 'weft_dens']
                             ])

########################################################################################################################


# приведение типов столбцов таблицы;
dataframe['warp_a'] = dataframe.warp_a.apply(convert_to_float)
dataframe['warp_b'] = dataframe.warp_b.apply(convert_to_float)
dataframe['weft_a'] = dataframe.weft_a.apply(convert_to_float)
dataframe['weft_b'] = dataframe.weft_b.apply(convert_to_float)

# рассчет средних значений толщин нитей по основе и по утку;
# получаемые значения округляются до 2 знаков после запятой;
dataframe['warp_mean'] = round((dataframe['warp_a'] + dataframe['warp_b']) / 2, 2)
dataframe['weft_mean'] = round((dataframe['weft_a'] + dataframe['weft_b']) / 2, 2)

# "Коэффициент плотности" - соотношение плотности по основе к плотности по утку;
dataframe['density_coefficient'] = round(dataframe['warp_dens'] / dataframe['weft_dens'], 2)

# удаление строк с пропущенными и нулевыми значениями;
dataframe = dataframe.dropna()

# Выборка данных из подготовленного датафрейма;
# Предполагается, что для сбалансированных тканей разница между плотностью
# по основе и плотностью по утку не должна превышать 3 единиц;
balanced = dataframe[abs(dataframe['warp_dens'] - dataframe['weft_dens']) <= 3]
unbalanced = dataframe[abs(dataframe['warp_dens'] - dataframe['weft_dens']) > 3]

# Ткани с переплетением типа "рогожка";
baskets = dataframe[dataframe['weaving_technique'] == 'basket']

# выборка узких бинтов;
narrow_bands = dataframe[dataframe['type'] == 'n_band']

# выборка средних бинтов;
middle_bands = dataframe[dataframe['type'] == 'm_band']

# выборка широких бинтов;
wide_bands = dataframe[dataframe['type'] == 'w_band']
