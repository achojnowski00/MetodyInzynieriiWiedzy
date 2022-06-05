from asyncio.windows_events import NULL
import math as m
import numpy as np


def projekcja(u,v):
    return (np.dot(u.T,v) / np.dot(u.T,u)) * u


def dlugosc(u):
    return m.sqrt(np.dot(u.T,u))

 
def rozkladQR(a):
    matrixWektorowV=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    matrixWektorowU = []
    macierzQ = []
    
    for wektorV in matrixWektorowV:
        wektorV = np.array(wektorV)
        projekcjaWektora = NULL
        for wektorZMacierzyU in matrixWektorowU:
            projekcjaWektora+=projekcja(wektorZMacierzyU, wektorV)
        wektorUx = wektorV - projekcjaWektora
        matrixWektorowU.append(wektorUx)
        dlugoscUx = dlugosc(wektorUx)
        if dlugoscUx != 0:
            macierzQ.append(wektorUx/dlugoscUx)
        else:
            macierzQ.append(wektorUx)
        Q = np.array(macierzQ).T
    return Q


def aPlusJeden(a):
    macierzQ = rozkladQR(a)
    QTA = np.dot(macierzQ.T, a)
    return np.dot(QTA, macierzQ)


def szukanieWartosciWlasnych(a, epsilon=0.0001):
    wynik = a
    while (wynik - np.triu(wynik)).sum()>epsilon:
        wynik = aPlusJeden(wynik)
    return np.diag(wynik)
      

matrixA = np.array([
    [1, 2, 2],
    [1, 8, 0],
    [2, 5, 4]
])


wynik = szukanieWartosciWlasnych(matrixA)
for i in range(len(wynik)):
    print("λ{ktoraLambda} = {wartoscWlasna}"
        .format(ktoraLambda = i, 
               wartoscWlasna = np.round(wynik[i],3)))
