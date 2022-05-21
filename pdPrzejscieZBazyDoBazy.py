import numpy as np

matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, -1, -1, -1, -1],
                   [1, 1, -1, -1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, -1, -1],
                   [1, -1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, -1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, -1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, -1], ])


def isMatrixOrtagonalna(matrix, epsilon=0.05):
    dot = np.dot(matrix, matrix.T)
    # print(dot)
    for i in range(len(dot)):
        for j in range(len(dot[i])):
            if i == j and dot[i][j] != 0:
                continue
            if(dot[i][j] > epsilon):
                # print("Macierz nie jest ortogonalna")
                return False
    # print("Macierz jest ortogonalna")
    return True


def normalize(matrix):
    wynik = []
    for vector in matrix:
        len = np.dot(vector, vector.T)
        if len != 0:
            vector = vector / np.sqrt(len)
        wynik.append(vector)
    return np.array(wynik)


def isMatrixJednostkowa(matrix, epsilon=0.05):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] > 1 - epsilon and matrix[i][j] < 1 + epsilon:
                continue
            if matrix[i][j] < epsilon and matrix[i][j] > -epsilon:
                continue
            if matrix[i][j] > epsilon or matrix[i][j] < -epsilon:
                return False
    return True


def isMacierzOrtonormalna(matrix, epsilon=0.05):
    dot = np.dot(matrix, matrix.T)
    return isMatrixJednostkowa(dot)


def przejsciePrzezBaze(wektor, bazaPocz, bazaNowa):
    xb = []
    if isMacierzOrtonormalna(bazaNowa):
        if isMatrixJednostkowa(bazaPocz):
            return np.dot(bazaNowa.T, wektor)
        return np.dot(np.dot(bazaNowa.T, bazaPocz), wektor)
    return np.dot(np.dot(np.linalg.inv(bazaNowa), bazaPocz), wektor)


# print(isMatrixOrtagonalna(matrix))
normalizedMatrix = normalize(matrix)
# print(normalizedMatrix)
# print(isMatrixOrtagonalna(normalizedMatrix))
# print(isMacierzOrtonormalna(normalizedMatrix))


wektor = [8, 6, 2, 3, 4, 6, 6, 5]
wektorWBazieOrtonormalnej = przejsciePrzezBaze(
    wektor, matrix, normalizedMatrix)
print(wektorWBazieOrtonormalnej)

# Sprawdzenie, czyli przejscie z bazy znormalizowanej do bazy początkowej
powrotDoBazy = przejsciePrzezBaze(
    wektorWBazieOrtonormalnej, normalizedMatrix, matrix)
print(powrotDoBazy)
