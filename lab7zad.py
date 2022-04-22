import numpy as np

def zad1():
    print('zad1')
    a = np.arange(3)
    b = [3, 4, 5]
    print(np.dot(a, b))


def zad2():
    print('zad2')
    a = np.arange(9).reshape((3, 3))
    b = np.arange(10, 26, 1).reshape((4, 4))
    print(a)
    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b)
    print(b.min(axis=0))
    print(b.min(axis=1))


def zad3():
    print('zad3')
    a = np.arange(3)
    b = [3, 4, 5]
    print(a * b)


def zad4():
    print('zad4')
    a = np.arange(3, dtype='int32')
    b = np.arange(3, dtype='float')
    print(a * b)


def zad5():
    print('zad5')
    a = np.array([np.arange(3, 6, 1), np.arange(12, 15, 1)])
    print(a)
    a = np.sin(a)
    print(a)


def zad6():
    print('zad6')
    b = np.array([np.arange(8, 11, 1), np. arange(22, 25, 1)])
    print(b)
    b = np.cos(b)
    print(b)


def zad7():
    print('zad7')
    a = np.sin(np.array([np.arange(3, 6, 1), np.arange(12, 15, 1)]))
    b = np.cos(np.array([np.arange(8, 11, 1), np. arange(22, 25, 1)]))
    print(a + b)


def zad8():
    print('zad8')
    m = np.arange(20, 53, 4).reshape((3, 3))
    for n in m:
        print(n)
        print("")


def zad9():
    print('zad9')
    m = np.arange(20, 53, 4).reshape((3, 3))
    for n in m.flat:
        print(n)
        print("")


def zad10():
    print('zad10')
    # m = np.zeros((9, 9))
    m = np.arange(81).reshape((9, 9))
    print(m)
    # mamy mozliwosc zmienia rozmiaru macierzy jedynie na takie gdzie
    # iloczyn ilosc kolumn i ilosci wierszy da 81 (czyli tyle co 9 * 9)
    # dostepne warianty: (1*81), (3*27), (9*9), (27*9), (81*1)


def zad11():
    print('zad11')
    m = np.arange(12)
    m1 = m.reshape((3, 4))
    m2 = m.reshape((4, 3))
    m3 = m.reshape((2, 6))
    for a in m1.flat:
        print(a)
    for a in m2.flat:
        print(a)
    for a in m3.flat:
        print(a)
    # wyswietlane wyniki sa identyczne


def lab7zad():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
    zad8()
    zad9()
    zad10()
    zad11()


if __name__ == '__main__':
    lab7zad()