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


def zad6():
    words = ['jajko', 'zajac wielkanocny', 'prezent']
    print(words)
    najdluzsze_slowo = words[np.argmax(words)]
    najdluzsze_slowo_len = max(len(words[0]), len(words[1]), len(words[2]))
    words = np.delete(words, np.argmax(words))
    print(words)
    print(najdluzsze_slowo)
    print(najdluzsze_slowo_len)
    m = np.full((najdluzsze_slowo_len, najdluzsze_slowo_len), " ")
    for i in range(najdluzsze_slowo_len):
        m[i][i] = najdluzsze_slowo[i]
    for i in range(len(words[0])):
        m[najdluzsze_slowo_len - 1][i] = words[0][i]
    for i in range(len(words[1])):
        m[i][najdluzsze_slowo_len - 1] = words[1][len(words[1]) - i -1]
    print(m)


def zad7(n: int):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            m[i][j] = 2 * (np.abs(i-j) + 1)
    return m


def zad8(tablica: np.ndarray, kierunek):
    # pionowo
    num_rows, num_cols = tablica.shape
    if kierunek == 0:
        if num_rows % 2 == 0:
            return np.array(np.split(tablica, 2))
        else:
            print("operacjia nie mozliwa (liczba wierszy macierzy jest nieparzysta")
    # poziomo
    elif kierunek == 1:
        if num_cols % 2 == 0:
            return np.array(np.hsplit(tablica, 2))
        else:
            print("operacjia nie mozliwa (liczba column macierzy jest nieparzysta")


def zad9(r: int):
    m = r + np.arange(25).reshape((5, 5))
    return m


def lab5zad():
    zad1()
    zad2()
    print(zad3(4))
    print(zad4(2, 4))
    zad5(6)
    zad6()
    print(zad7(3))
    m = np.arange(16).reshape((4, 4))
    print(m)
    print(zad8(m, 1))
    print(zad9(100))


if __name__ == '__main__':
    lab5zad()
