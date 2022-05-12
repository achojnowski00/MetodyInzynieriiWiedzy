import numpy as np
import math as m


def sredniaArytmetyczna(wektor):
    return sum(wektor)/len(wektor)


def wariancja(wektor):
    srednia = sredniaArytmetyczna(wektor)
    mianownik = 0
    for i in range(len(wektor)):
        mianownik += (wektor[i] - srednia) ** 2
    return mianownik/len(wektor)


def sredniaArytmetyczna2(wektor):
    wektorJednostkowy = np.ones(len(wektor))
    return np.dot(wektor, wektorJednostkowy) / len(wektor)


def wariancja2(wektor):
    v1 = np.array(wektor)
    v2 = np.array(sredniaArytmetyczna2(wektor))
    c = v1 - v2
    return np.dot(c, c)/len(wektor)


def wariancja3(wektor):
    wektorZeSrednia = sredniaArytmetyczna2(wektor) * np.ones(len(wektor))
    wektorMinusSrednia = wektor-wektorZeSrednia
    return np.dot(wektorMinusSrednia.T, wektorMinusSrednia) / len(wektor)


def odchylenieStandardowe(wektor):
    return m.sqrt(wariancja3(wektor))


lista = [4, -3, 2, 5]
print("Srednia arytmetyczna dla {0} jest równa {1}".format(
    lista, sredniaArytmetyczna2(lista)))
# print("Wariancja dla {0} jest równa {1}".format(lista, wariancja(lista)))
print("Wariancja dla {0} jest równa {1}".format(lista, wariancja3(lista)))
print("Odchylenie standardowe dla {0} jest równe {1}".format(
    lista, odchylenieStandardowe(lista)))
