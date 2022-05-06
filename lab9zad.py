import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def lab9zad():
    # zadanie 1
    xlsx = pd.ExcelFile('datasets\\imiona.xlsx')
    df = pd.read_excel(xlsx, header=0)
    print(df)
    grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
    grupa.plot()
    plt.show()
    # zadanie 2
    grupa = df.groupby(["Plec"]).agg({'Liczba': ['sum']})
    grupa.plot.bar()
    plt.show()
    # zadanie 3
    grupa = df[(df['Rok'] > 2012) & (df['Rok'] < 2018)].groupby(['Rok']).agg({'Liczba': ['sum']})
    grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20,figsize=(6, 6), legend=(0, 0))
    plt.legend(loc='lower right')
    plt.show()
    # zadanie 4
    df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
    print(df)
    grupa = df.groupby(['Sprzedawca'])['Sprzedawca'].count()
    grupa.plot.bar()
    plt.show()



if __name__ == '__main__':
    lab9zad()
