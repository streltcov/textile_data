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

#######################################################################################################################



# Загрузка датафрейма из CSV файла;
textiles = pandas.read_csv('dataframe.csv')

len_textiles_base = len(textiles)
textiles = textiles.dropna(subset=['warp_dens', 'weft_dens'])
len_textiles = len(textiles)

########################################################################################################################

# Приведение типов колонок датафрейма к значению с плавающей запятой;
textiles['warp_a'] = textiles.warp_a.apply(convert_to_float)
textiles['warp_b'] = textiles.warp_b.apply(convert_to_float)
textiles['weft_a'] = textiles.weft_a.apply(convert_to_float)
textiles['weft_b'] = textiles.weft_b.apply(convert_to_float)

########################################################################################################################

# Вычисление "усредненных" толщин нитей;
textiles['warp_nominal'] = round((textiles['warp_a'] + textiles['warp_b']) / 2, 2)
textiles['weft_nominal'] = round((textiles['weft_a'] + textiles['weft_b']) / 2, 2)

########################################################################################################################

# Соотношение плотностей по основе и утку;
textiles['warp_weft'] = round((textiles['warp_dens'] / textiles['weft_dens']), 2)

########################################################################################################################

# Добавление признака density_coefficient;
textiles['density_ratio'] = round((textiles['warp_dens'] / textiles['weft_dens']), 2)

########################################################################################################################

textiles['thick_ratio'] = round((textiles['warp_nominal'] / textiles['weft_nominal']), 3)

########################################################################################################################

# QUALITY GROUPS

# Group A: warp-faced tabby with warp count less than 15 yarns per cm and average yarn diameter about 0.5-0.8 for warps
# and 0.6-0.9 for wefts; the ratio of warps to wefts is 1 to 2;

group_A = textiles.query('warp_dens <= 15 and warp_nominal > 0.5 and warp_nominal < 0.8 and weft_nominal > 0.6 and weft_nominal < 0.9')

# Group B: Warp-faced tabby with warp count 16-29 and average yarn diameter about 0.3-0.6 for warps and 0.3-0.6
# for wefts; the ratio of warps to wefts is 1 to 2 or less;

group_B = textiles.query('warp_dens > 16 and warp_dens <= 29 and warp_nominal > 0.3 and warp_nominal < 0.5 and weft_nominal > 0.3 and weft_nominal < 0.6')

# Group C: Warp-faced tabby with a warp count of more than 30 yarns per cm and average yarn diameter

group_C = textiles.query('warp_dens >= 30')

group_D = pandas.concat([textiles, group_A, group_B, group_C]).drop_duplicates(keep=False)

########################################################################################################################
