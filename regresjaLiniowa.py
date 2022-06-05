import math as m
import numpy as np


def regresjaLiniowa(matrix):
    macierzX = np.array([[1, x[0]] for x in matrix])
    macierzY = np.array([y[1] for y in matrix])
    MT_dot_M_to_power_minus_one = np.linalg.inv(np.dot(macierzX.T, macierzX))
    lewa_odwrotnosc = np.dot(MT_dot_M_to_power_minus_one, macierzX.T)
    macierzBeta = np.dot(lewa_odwrotnosc, macierzY)
    return macierzBeta 


matrixZPunktow = np.array([
    [2, 1],
    [5, 2],
    [7, 3],
    [8, 3]
])

beta = regresjaLiniowa(matrixZPunktow)
print(beta)
print("f(x) = ", beta[1], "x + ", beta[0],sep="")


'''
punkty do zadania
(2, 1)
(5, 2)
(7, 3)
(8, 3)

Beta:
[2 / 7 ] 0.28571429
[5 / 14] 0.35714286

wyklad 4 kwietnia 2022 
17 minuta omówienie tego zadania
'''
