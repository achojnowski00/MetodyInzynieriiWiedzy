# imie = input("Jak się nazywasz? ")
# print("Cześć {fname}".format(fname = imie))

zm1 = "test"
zm2 = 5
zm3 = 5.5

print("zm1:{zm1value} type: {zm1format}\n"
      "zm2:{zm2value} type: {zm2format}\n"
      "zm3:{zm3value} type: {zm3format}".format(zm1value=zm1, zm2value=zm2, zm3value=zm3, zm1format=type(zm1), zm2format=type(zm2), zm3format=type(zm3)))


list = ["ala", "ma", "kota"]

# to co podamy przed joinem to łącznik jaki bedzie miedzy wyrazami
joinedList = '_'.join(list)
print(joinedList)

splitedList = joinedList.split("_")
print(splitedList)

miws = "Metody Inżynierii Wiedzy Są"
print("{str} zawiera {len} znakow".format(str=miws, len=len(miws)))

miws = miws.lower()
print("{str} zawiera {len} znakow".format(str=miws, len=len(miws)))

miwsBezPl = miws.replace("ą", "a").replace("ż", "z").replace(" ", "")
print("{str} zawiera {len} znakow".format(str=miwsBezPl, len=len(miwsBezPl)))

set1 = set(miwsBezPl)
print(('{str} {len}'.format(str=set1, len=len(set1))))

tuple = (1, "jeden")

print("{x}, {type}".format(x=tuple, type=type(tuple)))

progLangs = ["python", "c", "cpp", "java", "prolog"]
print(len(progLangs))
print(progLangs.index("python"))

list1 = ["one", "two"]
list2 = ["three", "four"]
list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

list1.append("five")
print(list1)

slownik = {"Polska": "Warszawa", "Rosja": "Moskwa", "Litwa": "Wilno", "Białoruś": "Mińsk",
           "Ukraina": "Kijów", "Słowacja": "Bratysława", "Czechy": "Praga", "Niemcy": "Berlin"}
print(slownik.values())
print(sorted(slownik.values()))
print(sorted(slownik))

'''
Jak przesortowac slownik ale w środku
OrderBy(x => x.Value)
             x.Key)
tak w c#
'''


print(bool(" "))
print(bool(""))
print(bool(1))
print(bool(0))
print(bool(["", ""]))


zdanie = "Ala ma dużego kota i psa ale juz małego"

unique = set(zdanie)
print(len(unique))
if len(unique) > 15:
    print("dużo znaków")
else:
    print("mało znaków :)")


for i in range(0, 11):
    print(i)

for i in range(len(joinedList)):
    if joinedList[i] != "_":
        print(joinedList[i], end="")
    else:
        print(" ", end="")
