import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def z1():
    x = np.arange(1, 21, 0.01)
    y = 1/x
    plt.plot(x, y)
    plt.xlabel('x')
    plt.xlabel('f(x)')
    plt.axis([1, 21, 0, 1])
    plt.show()


def z2():
    x = np.arange(1, 20, 1)
    y = 1/x
    plt.plot(x, y, 'g^:')
    plt.xlabel('x')
    plt.xlabel('f(x)')
    plt.axis([0, 20, 0, 1])
    plt.show()


def z3():
    x = np.arange(0, 30, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.subplot(2, 1, 1)
    plt.plot(x, y1, 'b', label='wykres sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(x, y2, 'r', label='wykres cos(x)')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.legend()
    plt.show()


def z4():
    df = pd.read_csv('datasets/iris.data', sep=',', decimal='.')
    print(df)
    # 1. sepal length in cm
    # 2. sepal width in cm
    # 3. petal length in cm
    # 4. petal width in cm
    # 5. class:
    #     -- Iris Setosa
    #     -- Iris Versicolour
    #     -- Iris Virginica

    # przygotowanie wektora kolorów
    colors = np.random.randint(0, 50, len(df.index))
    # przygotowanie wektora z rozmiarami 'kropek'
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    scale = np.abs(x - y)
    plt.scatter(x, y, c=colors, s=scale)
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.show()


def z5():
    xlsx = pd.ExcelFile("datasets\\imiona.xlsx")
    df = pd.read_excel(xlsx, header=0)
    print(df)
    # wykres 1
    grouped = df.groupby('Plec')
    etykiety = list(grouped.groups.keys())
    wartosci = list(grouped.agg('Liczba').sum())
    plt.subplot(1, 3, 1)
    plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
    plt.xlabel('Płeć')
    plt.ylabel('Liczba narodzonych dzieci')
    # wykres 2
    plt.subplot(1, 3, 2)
    x = df['Rok'].unique()
    k = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values
    m = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values
    moje = [df['Rok'].unique().tolist(),
            df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values.to,
            df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values.tolist()]
    print(k)
    print(m)
    print(moje)
    plt.plot(x, k, label="Kobiety")
    plt.plot(x, m, label="Mężczyźni")
    plt.xlabel('Rok')
    # wykres 3
    plt.subplot(1, 3, 3)
    x = df['Rok'].unique()
    y = df.groupby('Rok').agg('Liczba').sum()
    plt.bar(x, y)
    plt.xlabel('Rok')
    # wyświetlamy cały wykres
    plt.subplots_adjust(wspace=0.85)
    plt.show()



def lab10zad():
    # z1()
    # z2()
    # z3()
    # z4()
    z5()


if __name__ == '__main__':
    lab10zad()
