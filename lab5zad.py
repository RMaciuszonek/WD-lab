import numpy as np

def zad1():
    a = np.arange(4, 84, 4)
    print(a)


def zad2():
    lista = np.arange(10, dtype='float')
    print(lista)
    lista_2 = lista.astype(dtype='int32')
    print(lista_2)


def zad3(n: int):
    mat = 2 ** np.arange(n*n)
    mat = mat.reshape((n, n))
    return mat


def zad4(podstawa, ilosc_poteg: int):
    return np.logspace(1, ilosc_poteg, num=ilosc_poteg, base=podstawa)
    # return podstawa ** np.arange(1, ilosc_poteg + 1)


def zad5(dlugosc_wektora: int):
    return np.diag([a for a in range(dlugosc_wektora, -1, -1)], 2)



def zad6(s1: str, s2: str, s3: str):
    najdluzsze_slowo = max(len(s1), len(s2), len(s3))
    s1_arr = np.array(list(s1))
    s2_arr = np.array(list(s2))
    s3_arr = np.array(list(s3))
    print(s1_arr)
    print(s2_arr)
    print(s3_arr)
    print(najdluzsze_slowo)
    # mat = np.diag()


def zad7(n: int):
    return 0



def zad8(tablica, kierunek):
    # pionowo
    if kierunek == 1:
        return 0
    # poziomo
    else:
        return 0

def lab5zad():
    zad1()
    zad2()
    print(zad3(4))
    print(zad4(2, 4))
    zad5(6)
    zad6('jajko', 'zajac wielkanocny', 'prezent')
    print(zad7(3))
    print(zad8(np.arange(5), 1))

if __name__ == '__main__':
    lab5zad()