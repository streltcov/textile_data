"""
"""


import pandas


class Textiles:
    """ "Надстройка" над датафреймом Pandas; """
    
    def __init__(self, path: str, sep=','):
        """ """
        self.__dataframe = pandas.read_csv(path, sep=sep)
        self.__check_dataframe()
        self.__define_dens_quartiles()
        self.__define_thick_quartiles()
        self.__define_dens_outliers()
        self.__define_thick_outliers()
        self.__define_dens_cleared()
        self.__define_thick_cleared()
    
    def __check_dataframe(self):
        """ """
        return True
    
    def __define_dens_quartiles(self):
        """ Вычисляет значения 1, 2 и 3 квартиля плотностей по основе и по утку (сохраняются в кортежи); """
        self.__warp_dens_quartiles = self.__dataframe.warp_dens_mean.quantiles([0.25, 0.5, 0.75])
        self.__weft_dens_quartiles = self.__dataframe.weft_dens_mean.quantiles([0.25, 0.5, 0.75])
    
    def __define_thick_quartiles(self):
        """ Вычисляет значения 1, 2 и 3 квартиля тощин нитей по сонове и утку (сохраняются в кортежи); """
        self.__warp_thick_quartiles = self.__dataframe.warp_nominal.quantiles([0.25, 0.5, 0.75])
        self.__weft_thick_quartiles = self.__dataframe.weft_nominal.quantiles([0.25, 0.5, 0.75])
    
    def __define_dens_outliers(self):
        """ """
        self.__outliers = self.__dataframe
    
    def __define_cleared(self):
        """ """
        self.__cleared = self.__dataframe
    
    def dataframe(self):
        """ Возвращает базовый датафрейм """
        return self.__dataframe
    
    def dens_cleared(self):
        """ Возвращает датафрейм, очищенный от выбросов """
        return self.__dens_cleared
    
    def thick_cleared(self):
        """ """
        return self.__thick_cleared
    
    def dens_outliers(self):
        """ Возвращает датафрейм выбросов, рассчитанных по межквартильным интервалам по плотности тканей; """
        return self.__outliers
    
    def thick_outliers(self):
        """ Возвращает датафрейм выбросов, рассчитанных по межквартильным интервалам по толщинам нитей; """
        return self.__thick_outliers
    
    def filter_type(self, type: str):
        """ Фильтрует базовый датафрейм по переданному параметром типу; Изменяет базовый датафрейм; """
        return self.__dataframe.query('type == "' + str(type) + '"')
    
    def warp_dens_quartiles(self, number):
        """ Возвращает кортеж квартилей плотности ткани необработанного датасета; """
        number = int(number)
        if number >=0 and number <= 2:
            return self.__warp_dens_quartiles[number]
    
    def weft_dens_quartiles(self, number):
        """ """
        number = int(number)
        if number >= 0 and number <= 2:
            return self.__weft_dens_quartiles[number]
    
    def warp_thick_quartiles(self, number):
        """ """
    
    def weft_thick_quartiles(self, number):
        """ """


def quality_1(textiles: Textiles):
    """ """

def quality_2(textiles: Textiles):
    """ """

def quality_3(textiles: Textiles):
    """ """
