import math as m
import numpy as np


def lewaOdwrotnosc(macierz):
    mDotMT = np.dot(macierz.T, macierz)
    macierzOdwrotna = np.linalg.inv(mDotMT)
    return np.dot(macierzOdwrotna, macierz.T)


def regresjaLiniowa(matrix):
    matrix_x = np.array([[1, x[0]]for x in matrix])
    matrix_y = np.array([x[1]for x in matrix])
    lewa_odw = lewaOdwrotnosc(matrix_x)
    return np.dot(lewa_odw, matrix_y)


matriz = np.array([[2, 1],
                   [5, 2],
                   [7, 3],
                   [8, 3]])

print(regresjaLiniowa(matriz))


'''
punkty do zadania
(2, 1)
(5, 2)
(7, 3)
(8, 3)

Beta:
[2 / 7 ]
[5 / 14]

wyklad 4 kwietnia 2022 
17 minuta omówienie tego zadania
'''
