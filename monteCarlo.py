import random
import math


def monteCarlo(funct, startX, lastX, points=5000):
    # wyznaczamy wielkość prostokatu na ktorym
    # bedziemy wstawiac losowe punkty
    max = funct(lastX)
    min = 0
    # jeśli początkowy y leży pod wykresem to za minimum
    # przyjmujemy wartośc początkowego X czyli startX
    if funct(startX) < 0:
        min = funct(startX)
    pod = 0
    for i in range(points):
        # losujemy losowe wspolrzedne nowego punktu
        randomX = random.uniform(startX, lastX)
        randomY = random.uniform(min, max)

        # sprawdanie, czy punkt leży pod funkcją czy nad,
        # jeśli pod to inkrementujemy zmienną pod
        functionValueOfRandomX = funct(randomX)
        if(randomY <= functionValueOfRandomX):
            pod += 1

    # zwracamy proporcje czyli pole prostokata razy
    #  ilosc pod funkcją dzielone przez ilosc punktow
    return (lastX-startX)*(max-min)*(pod/points)


def funkcja(x):
    # return ((x**2)/3)*2
    # return x
    return x**2


print(monteCarlo(funkcja, 6, 13))
# dla funkcji y=x^2, całka od 6 do 13 równa się ~= 660, program za pomocą metody monteCarlo
# z ilością 5000 punktów zwraca następujące wyniki: 664.607  661.297  662.716
# Dla innnych funkcji oraz wartości całki program zachowuje podobny margines błędu
