import numpy


def gen_ur_mnk(wektorX, wektorY, stopienWielomianu):
    # Dostajemy wektor X, który zawiera zmienne niezależne x
    # Dostajemy wektor Y, który zawiera zmienne zależne y
    # Mamy zmienne niezależne x i budujemy z nich macierz
    # Liczymy ile jest tych zmiennych x - to będzie ilość wierszy i kolumn
    # macierzy A (czyli macierzy z róznymi potęgami zmiennych x)
    n = len(wektorX)

    # Tworzymy zerowe macierze A i B, i wypełniamy je zerami
    A = numpy.zeros((stopienWielomianu + 1, stopienWielomianu + 1))
    B = numpy.zeros((stopienWielomianu + 1,))

    # Nastepnie wypełniamy te macierze
    X = [1.0 for i in range(n)]
    Y = [wektorY[i] for i in range(n)]

    A[0, 1] = len(X)

    # UZUPEŁNIANIE GÓRNEGO TRÓJKĄTA
    for i in range(stopienWielomianu + 1):
        A[0][i] = sum(X)

        B[i] = sum(Y)

        # Propagacja wartości macierzy A "w lewo w dół"
        for j in range(i):
            A[j + 1][i - j - 1] = A[0][i]

        for j in range(n):
            # Mnożymy każdy z elementów x przez siebie
            X[j] *= wektorX[j]
            # Mnożymy każdy z elementów y przez potęgę x (zaczynając od
            # pierwszej potęgi)
            Y[j] *= wektorX[j]

    # UZUPEŁNIANIE DOLNEGO TRÓJKĄTA
    for i in range(stopienWielomianu):
        A[i + 1, stopienWielomianu] = sum(X)

        for j in range(len(wektorX)):
            X[j] *= wektorX[j]

        for j in range(i + 1, stopienWielomianu):
            A[j + 1, stopienWielomianu - j + i] = A[i + 1, stopienWielomianu]

    print("macierz A:", A)
    print("\nmacierz B:", B)

    return A, B


def wielomian4(x,wsp):

    y = wsp[-1]

    for i in range(len(wsp)-2,-1,-1):
        y = y*x + wsp[i]

    return y

def r_kwadrat(y,f):
    for (p, q) in zip(y, f):  # łączenie w pary x i y
        print(p, q)

    ysr = (sum(y))/(len(y))
    L = 0
    M = 0
    for i in range(len(f)):
        L = L + ((y[i]) - (f[i]))**2
    for i in y:
        M = M + (i - ysr)**2
    print('Współczynnik determinacji:',(1 - (L/M)))
    return 1 - (L/M)


def blad(y,f):
    L = 0
    for i in range(len(f)):
        L = L + ((y[i]) - (f[i]))**2
    L = L/len(y)
    print('Błąd średniokwadratowy:',L)
    return L



