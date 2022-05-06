import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def listing1():
    ts = pd.Series(np.random.randn(1000))
    ts = ts.cumsum()
    print(ts)
    ts.plot()
    plt.show()


def listing2():
    data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
            'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
            'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
            'Populacja': [11190846, 1303171035, 207847528, 38675467]}
    df = pd.DataFrame(data)
    print(df)
    grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
    print(grupa)
    wykres = grupa.plot.bar()
    wykres.set_ylabel('Mld')
    wykres.set_xlabel('Kontynent')
    wykres.tick_params(axis='x', labelrotation=0)
    wykres.legend()
    wykres.set_title('Populacja z podziałem na kontynenty')
    plt.savefig('wykres.png')
    plt.show()


def listing3():
    df = pd.read_csv('datasets/dane.csv', header=0, sep=';', decimal='.')
    print(df)
    grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
    grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20,figsize=(6, 6), legend=(0, 0), colors=['red', 'green'])
    plt.legend(loc='lower right')
    plt.title('suma zamówień dla sprzedawcy')
    plt.show()


def listing4():
    ts = pd.Series(np.random.randn(1000))
    ts = ts.cumsum()
    df = pd.DataFrame(ts, columns=['Wartości'])
    print(df)
    df['Średnia krocząca'] = df.rolling(window=50).mean()
    df.plot()
    plt.legend()
    plt.show()


def lab9pandaswykresy():
    listing1()
    listing2()
    listing3()
    listing4()


if __name__ == '__main__':
    lab9pandaswykresy()
