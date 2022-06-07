import numpy as np
import math as m
from asyncio.windows_events import NULL

def zaookroglenie(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            matrix[i][j] = round(matrix[i][j],3)
    return matrix




def wektorLength(u):
    dot = np.dot(u.T, u)
    return m.sqrt(dot)


def projekcja(u, v):
    licznik = np.dot(u.T, v)
    mianownik = np.dot(u.T, u)
    if mianownik != 0:
        return licznik/mianownik*u


# def qrDecomposition(macierzA):
#     Q = []
#     v1 = []
#     v2 = []
#     wektoryV = []
#     for i in range(len(macierzA)):
#         v1.append(macierzA[i][0])
#         v2.append(macierzA[i][1])
#     wektoryV.append(np.array(v1))
#     wektoryV.append(np.array(v2))

#     u1 = wektoryV[0]
#     v2 = wektoryV[1]
#     e1 = u1/wektorLength(u1)
#     proju1v2 = projekcja(u1, v2)
#     u2 = v2 - proju1v2
#     e2 = u2/wektorLength(u2)
#     Q.append(e1)
#     Q.append(e2)
#     Q = np.array(np.array(Q).T)

#     R = np.dot(Q.T, macierzA)
#     return Q, R


def rozkladQR(macierzA):
    matrixWektorowV=[ [ x[i] for x in macierzA ] for i in range(len(macierzA[1])) ]
    matrixWektorowU = []
    macierzQ = []
    
    for wektorV in matrixWektorowV:
        wektorV = np.array(wektorV)
        projekcjaWektora = NULL
        for wektorZMacierzyU in matrixWektorowU:
            projekcjaWektora+=projekcja(wektorZMacierzyU, wektorV)
        wektorUx = wektorV - projekcjaWektora
        matrixWektorowU.append(wektorUx)
        dlugoscUx = wektorLength(wektorUx)
        if dlugoscUx != 0:
            macierzQ.append(wektorUx/dlugoscUx)
        else:
            macierzQ.append(wektorUx)
        Q = np.array(macierzQ).T
        R = np.dot(Q.T, macierzA)
    return Q,R


macierzA = np.array([[2, 0, 1],
                     [0, 1, 1],
                     [4, 1, 1],
                     [1, 2, 1]])


# Q, R = qrDecomposition(macierzA)
# print(Q)
# print("\n")
# print(R)

# print("\n\n\n\n\n")

Q, R = rozkladQR(macierzA)
print(zaookroglenie(Q))
print("\n")
print(zaookroglenie(R))
