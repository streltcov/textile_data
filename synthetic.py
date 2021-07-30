""" Генерация набора псевдослучайных синтетических данных для классификации текстиля;

"""


import random
import numpy as np
import pandas as pd

print("Class size - ", end='')
size = int(input())

i = 0

warp_nominal_1, warp_nominal_2, warp_nominal_3 = [], [], []
weft_nominal_1, weft_nominal_2, weft_nominal_3 = [], [], []
warp_dens_1, warp_dens_2, warp_dens_3 = [], [], []
weft_dens_1, weft_dens_2, weft_dens_3 = [], [], []

while i < size:
    # Наиболее качественные ткани - группа 1;
    # Плотность по основе - более 25; Плотность по утку - более 15;
    # Толщины нитей по основе - от 0,2 до 0,4; Толшины нитей по утку - 0,2 от до 0,5;
    warp_dens_1.append(int(round(random.uniform(25, 45), 0)))
    weft_dens_1.append(int(round(random.uniform(15, 25), 0)))
    warp_nominal_1.append(round(random.uniform(0.2, 0.4), 2))
    weft_nominal_1.append(round(random.uniform(0.2, 0.5), 2))
    # Средняя по качеству ткани - группа 2;
    # Плотность по основе - от 12 (включительно) до 25; Плотность по утку - от 9 (включительно )до 15;
    # Толшины нитей по основе - от 0,2 до 0,4; Толщины нитей по утку - от 0,2 до 0,5;
    warp_dens_2.append(int(round(random.uniform(12, 25), 0)))
    weft_dens_2.append(int(round(random.uniform(9, 15), 0)))
    warp_nominal_2.append(round(random.uniform(0.2, 0.4), 2))
    weft_nominal_2.append(round(random.uniform(0.2, 0.5), 2))
    # Наименее качественные ткани - группа 3;
    # Плотность по основе - от 2 (условно) до 11; Плотность по утку - от 2 (условно) до 8;
    # Толшины по основе - от 0,5 до 1,0; Толщины по утку - от 0,5 до 1,0;
    warp_dens_3.append(int(round(random.uniform(2, 11), 0)))
    weft_dens_3.append(int(round(random.uniform(2, 8), 0)))
    warp_nominal_3.append(round(random.uniform(0.5, 1.0), 2))
    weft_nominal_3.append(round(random.uniform(0.5, 1.0), 2))
    i += 1

print("Group 1:")
print(warp_nominal_1)
print(warp_dens_1)

print("Group 2:")
print(warp_nominal_2)
print(warp_dens_2)

print("Group 3:")
print(warp_nominal_3)
print(warp_dens_3)

columns = ['warp_nominal', 'weft_nominal', 'warp_dens', 'weft_dens']

index_1 = range(0, size)
# index_2 = range()
# index_3 = range()

df_1 = pd.DataFrame()
# df_2 = pd.DataFrame()
# df_3 = pd.DataFrame()

# df = None

# print(df)

filename = str(input())
# df.to_csv(filename)
