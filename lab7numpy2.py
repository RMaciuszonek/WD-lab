import numpy as np


def p1():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    print(a)
    print(b)
    c = a - b
    print(c)
    print(b**2)
    print(a)
    a += b
    print(a)
    a -= b
    print(a)


def p2():
    a = np.arange(12).reshape((3, 4))
    print(a)
    print(a.sum())
    print(a.sum(axis=0))
    print(a.sum(axis=1))
    print(a.cumsum(axis=1))


def p3():
    a = np.arange(3)
    b = np.arange(3)
    print(a)
    print(b)
    print(a.dot(b))
    print(np.dot(a, b))


def p4():
    a = np.ones(3, dtype='int32')
    print(a.dtype)
    b = np.linspace(0, np.pi, 3)
    print(b.dtype)
    c = a+b
    print(c)
    print(c.dtype)
    d = np.exp(c*1j)
    print(d)
    print(d.dtype)


def p5():
    b = np.arange(3)
    print(b)
    print(np.exp(b))
    print(np.sqrt(b))
    c = np.array([2., -1, 4.])
    print(np.add(b, c))


def p6():
    a = np.arange(6).reshape((3, 2))
    print(a)
    for b in a:
        print(b)
        print("")


def p7():
    a = np.arange(6).reshape((3, 2))
    print(a)
    for b in a.flat:
        print(b)
        print("")


def p8():
    a = np.arange(6)
    print(a)
    print(a.shape)
    b = np.array([np.arange(3), np.arange(3), np.arange(3)])
    print(b)
    print(b.shape)


def p9():
    a = np.arange(6)
    print(a)
    print(a.shape)
    print("")
    b = a.reshape((2, 3))
    print(b)
    print(b.shape)
    print("")
    c = b.reshape((3, 2))
    print(c)
    print(c.shape)
    print("")
    d = c.ravel()
    print(d)
    print(d.shape)
    print("")
    e = b.T
    print(e)
    print(e.shape)
    print("")


def lab7numpy2():
    p1()
    p2()
    p3()
    p4()
    p5()
    p6()
    p7()
    p8()
    p9()


if __name__ == '__main__':
    lab7numpy2()
