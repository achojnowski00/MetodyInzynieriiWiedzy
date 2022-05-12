import numpy as np
import math as m

macierzA = np.array([[2, 0],
                     [0, 1],
                     [1, 2]])


def wektorLength(u):
    dot = np.dot(u.T, u)
    return m.sqrt(dot)


def projekcja(u, v):
    licznik = np.dot(u.T, v)
    mianownik = np.dot(u.T, u)
    if mianownik != 0:
        return licznik/mianownik*u


def qrDecomposition(A):
    Q = []
    v1 = []
    v2 = []
    wektoryV = []
    for i in range(len(A)):
        v1.append(A[i][0])
        v2.append(A[i][1])
    wektoryV.append(np.array(v1))
    wektoryV.append(np.array(v2))

    u1 = wektoryV[0]
    v2 = wektoryV[1]
    e1 = u1/wektorLength(u1)
    proju1v2 = projekcja(u1, v2)
    u2 = v2 - proju1v2
    e2 = u2/wektorLength(u2)
    Q.append(e1)
    Q.append(e2)
    Q = np.array(np.array(Q).T)

    R = np.dot(Q.T, A)
    return Q, R


Q, R = qrDecomposition(macierzA)
print(Q)
print("\n")
print(R)
