import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


def p1():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('jakieś liczby')
    plt.show()


def p2():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
    plt.axis([0, 6, 0, 20])
    plt.show()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
    plt.axis([0, 6, 0, 20])
    plt.show()


def p3():
    t = np.arange(0.5, 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
    plt.show()


def p4():
    x = np.linspace(0, 2, 100)
    plt.plot(x, x, label='liniowa')
    plt.plot(x, x**2, label='kwadratowa')
    plt.plot(x, x**3, label='szesscienna')
    plt.xlabel('etykieta x')
    plt.ylabel('etykieta y')
    plt.title('Prosty wykres')
    plt.legend()
    plt.savefig('wykres matplot.png')
    plt.show()
    im1 = Image.open('wykres matplot.png')
    im1 = im1.convert('RGB')
    im1.save('nowy.jpg')


def p5():
    x = np.arange(0, 10, 0.1)
    s = np.sin(x)
    plt.plot(x, s, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Wykres sin(x)')
    plt.legend()
    plt.show()


def p6():
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100
    print(f"a={data['a'][0]}), b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('wartosc a')
    plt.ylabel('wartosc b')
    plt.show()


def p7():
    x1 = np.arange(0, 2, 0.02)
    x2 = np.arange(0, 2, 0.02)
    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, '-')
    plt.title('wykres sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    ax = plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'r-')
    plt.title('wykres cos(x)')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def p8():
    x1 = np.arange(0, 2, 0.02)
    x2 = np.arange(0, 2, 0.02)
    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)
    fig, axs = plt.subplots(3, 2, )
    # wykres 1
    axs[0, 0].plot(x1, y1, '-')
    axs[0, 0].set_title('wykres sin(x)')
    axs[0, 0].set_xlabel('x')
    axs[0, 0].set_ylabel('sin(x)')
    # wykres 2
    axs[1, 1].plot(x2, y2, 'r-')
    axs[1, 1].set_title('wykres cos(x)')
    axs[1, 1].set_xlabel('x')
    axs[1, 1].set_ylabel('cos(x)')
    # wykres 3
    axs[2, 0].plot(x2, y2, 'r-')
    axs[2, 0].set_title('wykres cos(x)')
    axs[2, 0].set_xlabel('x')
    axs[2, 0].set_ylabel('cos(x)')
    # figura
    fig.delaxes(axs[0, 1])
    fig.delaxes(axs[1, 0])
    fig.delaxes(axs[2, 1])
    plt.show()


def p9():
    data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
            'Stolica': ['Bruksela', 'New Delhi', 'Brasilisa', 'Warszawa'],
            'Kontynent': ['Europa', 'Azja', 'Ameryka Połódniowa', 'Europa'],
            'Populacja': [11190846, 1303171035, 207847528, 38675467]}
    df = pd.DataFrame(data)
    print(df)
    grupa = df.groupby('Kontynent')
    etykiety = list(grupa.groups.keys())
    wartosci = list(grupa.agg('Populacja').sum())
    plt.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
    plt.xlabel('Kontynenty')
    plt.ylabel('Populacja w mld')
    plt.show()


def p10():
    x = np.random.randn(10000)
    plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Wartości')
    plt.ylabel('Prawdopodobieństwo')
    plt.xlabel('Histogram')
    plt.gray()
    plt.show()


def p11():
    df = pd.read_csv('datasets/dane.csv', header=0, sep=';', decimal='.')
    print(df)
    seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
    wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: "{:.1f}%".format(pct),
    textprops=dict(color='black'), colors=['red', 'green'])
    plt.title('Suma zamówień dla sprzedawców')
    plt.legend(loc='lower right')
    plt.ylabel('Procentowy wynik wartości zamówienia')


def lab10wprowadzenie():
    p1()
    p2()
    p3()
    p4()
    p5()
    p6()
    p7()
    p8()
    p9()
    p10()
    p11()


if __name__ == '__main__':
    lab10wprowadzenie()
