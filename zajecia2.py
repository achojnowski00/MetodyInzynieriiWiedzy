haslo = "gifgyiUIG!@HUI1563"
haslo2 = "password123456"


def sprawdzenieHasla(paswd):
    length = True
    lower = False
    upper = False
    specialChar = False

    if len(paswd) < 10:
        length = False
    else:
        for i in range(0, len(paswd)):
            if "A" <= paswd[i] and paswd[i] <= "Z":
                upper = True
            else:
                lower = True

        if length and lower and upper and specialChar:
            print("Strong password")
        else:
            print("weak password")


sprawdzenieHasla(haslo)

list2 = [1, 2, 3, 99, 5]

for i in range(len(list2)):
    if list2[i] == 99:
        continue
    else:
        print(list2[i])


def czynalezy(liczba, lista):
    tmp = 0
    wynik = "Tu bedzie pzechowywany wynik"
    while tmp < len(lista):
        if lista[tmp] == liczba:
            wynik = True
            break
        else:
            wynik = False
        tmp += 1
    return wynik


czyNalezyWynik = czynalezy(5, list2)
print(czyNalezyWynik)


with open('plik.txt', 'r') as file:
    for i in file:
        print(i)

print("----")

with open('plik.txt', 'r') as file:
    for i in file:
        print(i, end='')


lista = ["python", "css", "html"]
fileOut = open('plik2.txt', 'w')
for i in lista:
    print(i, file=fileOut)


miasta = ["olsztyn", "warszawa", "krakow", "lodz"]
resualt = map(lambda x: x[:3], miasta)
print("\n", list(resualt))
print(type(resualt))

tablica = ["public.html", "plik.txt", "plik2.txt", "dok.doxc"]


def konkretnePliki(lista, roz):
    for plik in lista:
        index = -1
        for i in range(len(plik)):
            if plik[i] == ".":
                index = i
                break
        if plik[index+1:] == roz:
            print(plik)


konkretnePliki(tablica, "txt")


def x(lista, ext):
    for e in lista:
        if e.endswith(ext):
            yield e


dupa = x(tablica, ".txt")
print(list(dupa))


'''

przesłuchać wykład

'''
