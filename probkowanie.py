def probkowanie(function, startX, lastX, howManyDivisions=10):
    wynik = 0
    # ustalamy na ile prostokatow próbkowania podzielimy nasz wykres
    # oraz grubosc pojedynczego prostokata
    amoundOfRect = 2 ** howManyDivisions
    widthOfSigleRect = ((lastX - startX) / amoundOfRect)
    for i in range(amoundOfRect):
        # obliczamy w ktorym X'ie aktualnie jestesmy
        # do x od którego zaczynamy liczy dodajemy grubosc prodstokatow ktore juz przeszlismy,
        # przez co otrzymujemy wartosc X na poczatku aktualnego prostokata, aby zwiekszyc
        # dokladnosc pomiaru, dodajemy polowe grubosci aktualnego prostokata i naszym currentX
        # zostaje X na srodku prostokatu ktorego pole bedziemy obliczac
        # |         |
        # |... X ...|
        # |         |
        currentX = startX + (widthOfSigleRect * i) + widthOfSigleRect / 2
        '''
        currentX = startX + (widthOfSigleRect * i) + widthOfSigleRect # X na końcu prostokata
        currentX = startX + (widthOfSigleRect * i) # X na poczatku prostokata
        '''
        # do wyniku dodajemy wartośc mnozenia ktora ma postać:
        # wartosc funkcji w danym punkcie RAZY grubość pojedynczego prostokata
        wynik += function(currentX) * widthOfSigleRect
    return wynik


def f(x):
    # return ((x**2)/3)*2
    # return x
    return x**2


print(probkowanie(f, 6, 13, 15))
# dla funkcji y=x^2, całka od 6 do 13 równa się ~= 660, program za pomocą metody próbkowania
# z ilością 2^15 prostokątów zwraca następujące wyniki: 660.333333306773
