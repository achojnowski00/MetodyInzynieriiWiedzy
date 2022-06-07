from asyncio.windows_events import NULL
import math as m
import numpy as np

def zaookroglenie(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            matrix[i][j] = round(matrix[i][j],3)
    return matrix


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











def svdDecomposition(matrix):
    wiersze = len(matrix)
    kolumny = len(matrix[0])
    if(kolumny >= wiersze):
        ata = np.dot(matrix.T, matrix)
        
        wartosciWlasne = np.linalg.eigh(ata)[0]
        wektoryV = np.linalg.eigh(ata)[1].T

        tmp = np.ones(len(wartosciWlasne))
        tmp2 = np.ones((len(wektoryV),len(wektoryV[0])))
        for i in range (len(wartosciWlasne)):
            tmp[len(wartosciWlasne)-i-1] = round(wartosciWlasne[i],3)
        wartosciWlasne = tmp
        
        for i in range(len(wektoryV)):
            tmp2[len(wektoryV)-i-1] = wektoryV[i]
        wektoryV = tmp2.T

        wartosciSignularne = []
        for i in range(len(wartosciWlasne)):
            wartosciSignularne.append(wartosciWlasne[i]**0.5)
        
        sigma = np.zeros((len(matrix),len(matrix[0])))
        for i in range(len(sigma)):
            if wartosciSignularne[i] != 0:
                sigma[i][i] = wartosciSignularne[i]

        wektoryU = np.ones((len(matrix),len(matrix)))
        for i in range (len(wartosciSignularne)):
            sigma_i = wartosciSignularne[i]
            if sigma_i != 0:
                ui = np.dot(matrix, wektoryV.T[i]) / sigma_i
                wektoryU[i] = ui
        wektoryU = wektoryU.T
    else:
        aat = np.dot(matrix, matrix.T)
        wartosciWlasne = np.linalg.eigh(aat)[0]
        wektoryU = np.linalg.eigh(aat)[1].T

        tmp = np.ones(len(wartosciWlasne))
        tmp2 = np.ones((len(wektoryU),len(wektoryU[0])))
        for i in range (len(wartosciWlasne)):
            tmp[len(wartosciWlasne)-i-1] = round(wartosciWlasne[i],3)
        wartosciWlasne = tmp

        for i in range(len(wektoryU)):
            tmp2[len(wektoryU)-i-1] = wektoryU[i]
        wektoryU = tmp2.T

        wartosciSignularne = []
        for i in range(len(wartosciWlasne)):
            wartosciSignularne.append(wartosciWlasne[i]**0.5)

        sigma = np.zeros((len(matrix),len(matrix[0])))
        for i in range(len(sigma)):
            if wartosciSignularne[i] != 0:
                sigma[i][i] = wartosciSignularne[i]
        
        wektoryV = np.zeros((len(matrix[0]),len(matrix[0]))) # shape zgadza sie
        for i in range (len(wektoryV)):
            sigma_i = wartosciSignularne[i]
            if sigma_i != 0:
                # print(sigma_i)
                vi = np.dot(matrix.T, wektoryU.T[i]) / sigma_i
                wektoryV[i] = vi
        wektoryV = wektoryV.T



    print("Macierz: \n", matrix,"\n")
    # print("Wartosci wlasne (lambdy):\n", wartosciWlasne, "\n")
    # print("Wartosci singularne:\n", wartosciSignularne, "\n\n")
    print("Wektory wlasne U bez transpozycji:\n", zaookroglenie(wektoryU), "\n")
    print("Sigma:\n", sigma, "\n\n")
    print("Wektory wlasne V bez transpozycji:\n", zaookroglenie(wektoryV), "\n")

    print("po wymnozeniu: \n", zaookroglenie(np.dot(np.dot(wektoryU, sigma), wektoryV.T)), '\nKONIEC WYNIKU SVD\n\n')




matrixB = np.array([[1,2,0],[2,0,2]], dtype=np.float64)
# matrixB = np.array([[1,2],[2,0],[0,2]], dtype=np.float64)
# matrixB = np.array([[1,2,0],[2,0,2],[1,0,1]], dtype=np.float64)
 
svdDecomposition(matrixB)



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




