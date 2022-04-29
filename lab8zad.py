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
    grouped = df.groupby(['Rok'])
    print(grouped.agg({'Liczba': ['sum']}))
    #
    grouped2 = df[(df['Rok'] > 2000) & (df['Rok'] < 2005)].groupby(['Rok']).agg({'Liczba': ['sum']})
    print(grouped2)
    #
    grouped3 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
    print(grouped3)
    #
    print(df.loc([[0], ['Plec']]))


if __name__ == '__main__':
    lab8zad()