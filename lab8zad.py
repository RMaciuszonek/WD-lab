import pandas as pd
import numpy as np

def lab8zad():
    # zadanie 1
    print("ZADANIE 1")
    xlsx = pd.ExcelFile('datasets\\imiona.xlsx')
    df = pd.read_excel(xlsx, header=0)
    print(df)

    # zadanie 2
    print("ZADANIE 2")
    #
    print(df[df['Liczba'] > 1000])
    #
    print(df[df['Imie'] == 'ROBERT'])
    #
    grouped = df.groupby(['Rok']).agg({'Liczba': ['sum']})
    print(grouped)
    #
    grouped = df[(df['Rok'] > 2000) & (df['Rok'] < 2005)].groupby(['Rok']).agg({'Liczba': ['sum']})
    print(grouped)
    #
    grouped = df.groupby(['Plec']).agg({'Liczba': ['sum']})
    print(grouped)
    #
    grouped = df.groupby(['Rok', 'Plec'])['Liczba'].nlargest(1)
    print('\n========\n')
    print(grouped)
    #
    grouped = df.groupby(['Imie', 'Plec'])['Liczba'].sum().nlargest(1)
    print('\n=========\n')
    print(grouped)


    # zadanie 3
    df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')




if __name__ == '__main__':
    lab8zad()
