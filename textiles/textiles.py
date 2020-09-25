"""
"""


import pandas


class Textiles:
    """ "Надстройка" над датафреймом Pandas; """
    
    def __init__(self, path: str, sep=','):
        """ """
        self.__dataframe = pandas.read_csv(path, sep=sep)
    
    def dataframe(self):
        """ Возвращает базовый датафрейм """
        return self.__dataframe
    
    def cleared(self):
        """ Возвращает датафрейм, очищенный от выбросов """
    
    def outliers(self):
        """ Возвращает датафрейм выбросов, рассчитанных по межквартильным интервалам """
    
    def filter_type(self, type: str):
        """ Фильтрует базовый датафрейм по переданному параметром типу; Изменяет базовый датафрейм; """
    
    def warp_dens_quartile(self, number):
        """ """
    
    def weft_dens_quartile(self, number):
        """ """
    
    def warp_thick_quartile(self, number):
        """ """
    
    def weft_thick_quartile(self, number):
        """ """
    
    def quality_1(self):
        """ Возвращает датафрейм (с полным набором параметров), отфильтрованный по критериям первой группы по качеству """
    
    def quality_2(self):
        """ Возвращает датафрейм (с полным набором параметров), отфильтрованный по критериям первой группы по качеству """
    
    def quality_3(self):
        """ Возвращает датафрейм (с полным набором параметров), отфильтрованный по критериям первой группы по качеству """
