'''
git add .
git commit -m 'Metody Inzynierii Wiedzy zajecia 4'
git push
'''
from asyncio.windows_events import NULL
import math
import random
import numpy as np

path = "./metodyInzynieriiWiedzy/zajecia3/"

lista = []
delimiter = " "
with open(path + 'australian.dat', 'r') as file:
    for line in file:
        tmp = line.split(sep=delimiter)
        tmp = list(map(lambda e: float(e), tmp))
        lista.append(tmp)


def metrykaEuklidesowa(p1, p2):
    suma = 0
    for i in range(len(p1)-1):
        toAdd = p1[i] - p2[i]
        suma += (toAdd*toAdd)

    return math.sqrt(suma)


def metrykaEuklidesowaNumPy(p1, p2, utnij=False):
    if utnij:
        p1 = p1[:-1]
        p2 = p2[:-1]
    v1 = np.array(p1)
    v2 = np.array(p2)
    c = v2 - v1
    return math.sqrt(np.dot(c, c))

# # print(metrykaEuklidesowa([1.0, 22.08], [0.0, 22.67]))
# print(metrykaEuklidesowa(lista[0], lista[1]))
# print(metrykaEuklidesowa(lista[0], lista[2]))
# print(metrykaEuklidesowa(lista[0], lista[3]))


def grupAstr(lista, who):
    wynik = dict()
    y = lista[who]
    for i in range(1, len(lista)):
        decision = lista[i][len(lista[i])-1]
        if decision in wynik.keys():
            wynik[decision].append(metrykaEuklidesowaNumPy(y, lista[i]))
        else:
            wynik[decision] = [metrykaEuklidesowaNumPy(y, lista[i])]
    return wynik


zgrupowaniAustralijczycy = grupAstr(lista, 0)


# =======================
#       ZAJECIA 4
#  Grupowanie do slownika
#   i zwracanie dezycji
# =======================
def grupowanieDoTupla(x, lista):
    wynik = []
    for i in range(0, len(lista)):
        odleglosc = metrykaEuklidesowaNumPy(lista[i], x)
        wynik.append((lista[i][len(lista[i])-1], odleglosc))
    return wynik


nowy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
grupowanieDoTuplaWynik = grupowanieDoTupla(nowy, lista)
# print(grupowanieDoTuplaWynik)


def zamianaListyNaSlownik(lista):
    wynik = dict()
    for itemList in lista:
        decision = itemList[0]
        if decision not in wynik.keys():
            wynik[decision] = []
        wynik[decision].append(itemList[1])
    return wynik


listDoDict = zamianaListyNaSlownik(grupowanieDoTuplaWynik)
# print(listDoDict)


def kNajmniejszych(k, slownik):
    wynik = dict()
    for key in slownik:
        sortedDict = sorted(slownik[key])
        sortedDict = sortedDict[:k]
        wynikSum = sum(sortedDict)
        wynik[key] = wynikSum
    return wynik
# print(kNajmniejszych(5, listDoDict))


def decyzja(who, lista, k):
    # utworzenie tablicy która zawiera pary liczb (x,y) gdzie
    # x to klasa decyzyjna, a y to odleglość od zmiennej who
    tuple = []
    for i in range(0, len(lista)):
        odleglosc = metrykaEuklidesowaNumPy(lista[i], who)
        tuple.append((lista[i][len(lista[i])-1], odleglosc))

    # utworzenie slownika który zawiera dane w nastepującej postaci słownika,
    # który w kluczu ma klasę decyzyjną a w wartości tablice odległości zmiennej
    # who do wszystkich punktów z klasą decyzyjną zawartą w kluczu
    # {decision: [odleglosci who od punktow gdzie z decyzją decision]}
    slownik = dict()
    for itemList in tuple:
        decision = itemList[0]
        if decision not in slownik.keys():
            slownik[decision] = []
        slownik[decision].append(itemList[1])

    # posortowanie wartości w danym kluczu, a następnie wzięcie k najmniejszych wartości
    # oraz zsumowanie ich, przez co dostajemy słownik w postaci klucz który przyjmuje
    # wartość klast decyzyjnej oraz wartośc która przyjmuje zsumowaną odległość k
    # najmniejszych wartości (k najbliższych sąsiadów)
    # { decision : odległość }
    dictWithKSmallest = dict()
    for key in slownik:
        sortedDict = sorted(slownik[key])
        sortedDict = sortedDict[:k]
        wynikSum = sum(sortedDict)
        dictWithKSmallest[key] = wynikSum
    # print(dictWithKSmallest)  # print slownika z sumami i klasami decyzyjnymi

    # wyznaczenie decyzji dla podanych parametrów, szukamy klucz, czyli klasy decyzyjnej, który
    # jest najbliżej zmiennej who, czyli który ma przypisaną najmniejsza wartość.
    # Jako krok początkowy ustalamy, że najmniejszą wartością jest wartość klucza pierwszego
    # jeśli napotkamy na mniejszą wartośc do zmiennej klasaDecyzyjnaWynik przypisujemy dany klucz
    # kiedy znajdziemy jeszcze raz tą samą wartość inkrementujemy zmienną ilość
    listaKluczy = list(dictWithKSmallest.keys())
    klasaDecyzyjnaWynik = listaKluczy[0]
    ilosc = 1
    for i in range(1, len(listaKluczy)):
        if dictWithKSmallest[listaKluczy[i]] == dictWithKSmallest[klasaDecyzyjnaWynik]:
            ilosc += 1
        elif dictWithKSmallest[listaKluczy[i]] < dictWithKSmallest[klasaDecyzyjnaWynik]:
            klasaDecyzyjnaWynik = listaKluczy[i]
            ilosc = 1

    # RETURN: jeżeli ilosc jest >1 to znaczy, że mamy dwie najmniejsze wartości zatem nie można
    # wyznaczyć klasy decyzyjnej, w każdym innym przypadku zwracamy klasę decyzyjną z najmniejszą odległością
    if ilosc > 1:
        return
    else:
        return klasaDecyzyjnaWynik


# print(decyzja(nowy, lista, 5))

# print("   metyryka forem: ", metrykaEuklidesowa(lista[0], lista[5]))
# print("metyryka wektorem: ", metrykaEuklidesowaNumPy(lista[0], lista[5]))


def przydzielLosoweDecyzje(lista):
    wynik = []
    for item in range(len(lista)):
        newItem = lista[item]
        newItem = newItem[:-1]
        newItem.append(float(random.randint(0, 1)))
        wynik.append(newItem)
    return wynik


def minimumListy(lista):
    indexMin = 0
    for i in range(len(lista)):
        if lista[i] < lista[indexMin]:
            indexMin = i
    return indexMin


def robienieSlownikDecyzjaWartosci(lista):
    # slownik zawierający klase decyzyjna i tablice tablic ktora daje taka decyzje
    slownikDecyzjaWartosci = dict()
    for i in range(len(lista)):
        length = len(lista[i])
        if lista[i][length-1] not in slownikDecyzjaWartosci.keys():
            slownikDecyzjaWartosci[lista[i][length-1]] = []
        slownikDecyzjaWartosci[lista[i][length-1]].append(lista[i][:-1])
    return slownikDecyzjaWartosci

# !!!!!!!!!!!!!!!!!!!!!!!!!
#
# wyjebać printy z funkcji
#
# !!!!!!!!!!!!!!!!!!!!!!!!!


def znajdzSrodek(lista):
    slownikDecyzjaWartosci = robienieSlownikDecyzjaWartosci(lista)
    # print(slownikDecyzjaWartosci)

    klucze = list(slownikDecyzjaWartosci.keys())
    slownikDecyzjaPunktSrodkowy = dict()
    for klucz in klucze:
        listaPunktow = slownikDecyzjaWartosci[klucz]
        listaOdleglosciDlaKonkretnegoKlucza = []
        for punkt in listaPunktow:
            sumaOdleglosciOdWszystkichPunktow = 0
            for punktDoKtoregoMierzymy in listaPunktow:
                odlegloscDoPunktu = metrykaEuklidesowaNumPy(
                    punkt, punktDoKtoregoMierzymy)
                sumaOdleglosciOdWszystkichPunktow += odlegloscDoPunktu
            listaOdleglosciDlaKonkretnegoKlucza.append(
                sumaOdleglosciOdWszystkichPunktow)

        # print("dla klucza", klucz,listaOdleglosci)
        indexNajmniejszejOdleglosci = minimumListy(
            listaOdleglosciDlaKonkretnegoKlucza)
        slownikDecyzjaPunktSrodkowy[klucz] = listaPunktow[indexNajmniejszejOdleglosci]

    return slownikDecyzjaPunktSrodkowy


def przydzielenieNowychWartosci(lista, srodkiMasy):
    slownikDecyzjaWartosci = robienieSlownikDecyzjaWartosci(lista)
    slownikNowychWartosci = {}
    listaZNowymiWartosciami = []
    klucze = list(slownikDecyzjaWartosci.keys())
    listaWszystkichPunktow = []
    for klucz in klucze:
        listaWszystkichPunktow += slownikDecyzjaWartosci[klucz]
    # print(listaWszystkichPunktow)

    for klucz in klucze:
        slownikNowychWartosci[klucz] = []
    for punkt in listaWszystkichPunktow:
        doKtorejDecyzjiBlizej = klucze[0]
        for klucz in klucze:
            if metrykaEuklidesowa(punkt, srodkiMasy[klucz]) < metrykaEuklidesowa(punkt, srodkiMasy[doKtorejDecyzjiBlizej]):
                doKtorejDecyzjiBlizej = klucz
        # slownikNowychWartosci[doKtorejDecyzjiBlizej].append(punkt)
        punkt.append(doKtorejDecyzjiBlizej)
        listaZNowymiWartosciami.append(punkt)

    return listaZNowymiWartosciami


def nauczyciel(australian):
    lista = przydzielLosoweDecyzje(australian)
    iteracje = 0
    srodkiMasy = znajdzSrodek(lista)
    noweWartosci = przydzielenieNowychWartosci(lista, srodkiMasy)

    while iteracje < 10:
        print("iteracja numer ",  iteracje, srodkiMasy)
        srodkiMasy = znajdzSrodek(noweWartosci)
        print(srodkiMasy)
        najnowszeWartosci = przydzielenieNowychWartosci(lista, srodkiMasy)
        noweWartosci = najnowszeWartosci
        iteracje += 1

    slownikDecyzjaPunkty = robienieSlownikDecyzjaWartosci(noweWartosci)
    print("    zer: ", len(slownikDecyzjaPunkty[0]))
    print("jedynek: ", len(slownikDecyzjaPunkty[1]))
    return noweWartosci


#        dostaje liste(australiana)
#        przydzielam losowe wartosci (RAZ, przy wywołaniu)
#
#        while iteracje < 10
#          wyznaczam srodek masy (potrzebuje listy z losowymi wartosciami)
#   przydzielam nowe wartosci (potrzebuje listy z losowymi wartosciami i srodek masy)
#   zwiekszam interacje += 1
# po petli mam liste z posegregowanymi punktami
# zamieniam to na slownik zeby sprawdzic czy wszystko dziala poprawnie


# lista2 = przydzielLosoweDecyzje(lista)
# srodkiMasy = znajdzSrodek(lista)  # zmienic na lista2
# print(srodkiMasy[0], srodkiMasy[1])
# noweWartosci = przydzielenieNowychWartosci(lista, srodkiMasy)

# srodkiMasy2 = znajdzSrodek(noweWartosci)
# print(srodkiMasy2[0], srodkiMasy2[1])
# noweWartosci2 = przydzielenieNowychWartosci(noweWartosci, srodkiMasy2)

# srodkiMasy3 = znajdzSrodek(noweWartosci2)
# print(srodkiMasy3[0], srodkiMasy3[1])
# noweWartosci3 = przydzielenieNowychWartosci(noweWartosci2, srodkiMasy3)

# srodkiMasy4 = znajdzSrodek(noweWartosci3)
# print(srodkiMasy4[0], srodkiMasy4[1])
# noweWartosci4 = przydzielenieNowychWartosci(noweWartosci3, srodkiMasy4)

# srodkiMasy5 = znajdzSrodek(noweWartosci4)
# print(srodkiMasy5[0], srodkiMasy5[1])
# noweWartosci5 = przydzielenieNowychWartosci(noweWartosci4, srodkiMasy5)


nauczyciel(lista)

'''
Krok 2
mamy 2 srodki masy
pętla po wszystkich punktach i mierzymy odleglosc do jednego punktu masy i do 2go. Ustawimy decyzję
na taką do którego punktu jest temu punktowi blizej

krok3
zakonczenie po X razach lub jeśli żadna kropka juz nie zmienia swojego koloru





krok1
waga kropki:
potrzebujemy kropke(jej wspolrzedne) i liste kropek => suma odleglosci kropki od pozostalych kropek
otrzymamy liste odleglosci i szukamy minimalnej i wtedy ta kropka z najmniejsza odlegloscia
bedzie srodkiem masy

Srodek masy:
lista kropek z jednej decyzji => kropka ktora jets srodkiem masy







pomysły
zrobic slownik takie ze 
slownik = {[wspolrzedne punktu] : odleglosc , ....}
potem slownik.values.minimum
a potem slownik[value.minimum]

'''

# 28 lutego godzina 10 minut - przyklad z tym co zrobic (nauczyciel)
# zobaczyc zapis [:-1]
