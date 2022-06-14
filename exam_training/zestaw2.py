from textwrap import wrap

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Zad.1. Odwzoruj wykres znajdujący się w pliku o nazwie w2.png. Odcienie kolorów mogą się różnić, jednak
# główne barwy muszą być zachowane. Zapisz wykres w formacie png za pomocą kodu
def z1():
    y = ['A', 'B', 'C', 'D', 'E']
    x = [35, 45, 12, 41, 40]
    c = ['lightskyblue', 'pink', 'coral', 'silver', 'darkviolet']
    plt.subplot(1, 2, 1)
    plt.title('Wykres lewy')
    plt.barh(y, x, color=c)
    plt.subplot(1, 2, 2)
    plt.title('Wykres prawy')
    x2 = [-30, -33, -39, -35, -31]
    c2 = ['violet', 'mediumturquoise', 'darkturquoise', 'saddlebrown', 'olive']
    plt.barh(y, x2, color=c2)
    plt.savefig('wykres_zad_1.png')
    plt.show()


# Zad.2. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku ceny2.xlsx jako ramkę danych (Data Frame),
# • wyświetl na konsoli średnią cenę poszczególnych produktów ze wszystkich lat
# Produkt 1 - średnia ze wszystkich lat
# Produkt 2 - średnia ze wszystkich lat
# • stwórz wykres liniowy prezentujący dane zawarte w ramce danych
# • umieść swój numer indeksu w lewym dolnym rogu wykresu.
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
# Zapisz wykres w formacie jpg za pomocą kodu
def z2():
    excel = pd.ExcelFile('ceny2.xlsx')
    df = pd.read_excel(excel, header=0, decimal=',', sheet_name=0)
    print(type(excel))
    print(type(df))
    print(df)
    print('\nŚrednia cena poszczególnych produktów ze wszystkich lat')
    wynik = df.groupby(['Rodzaje towarów']).mean()
    print(wynik)
    ryz = df.where(df['Rodzaje towarów'] == 'ryż - za 1kg')
    maka = df.where(df['Rodzaje towarów'] == 'mąka pszenna - za 1kg')
    plt.figure()
    plt.plot(ryz['Rok'], ryz['Wartość'], label='Ryż')
    plt.plot(maka['Rok'], maka['Wartość'], label='Mąka')
    plt.legend()
    plt.text(2010, 2, '136301', fontsize=16)
    plt.savefig('wykres_zad_2')
    plt.show()


# Zad.3. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku nieruchomosci2.csv,
# • uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją “czystych danych” (w kolumnach)
# • stwórz wykres kołowy prezentujący dane zawarte w pliku (mogą być dwa wykresy kołowe)
# • Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
# Zapisz wykres w formacie pdf za pomocą kodu.
def z3():
    df = pd.read_csv('nieruchomosci.csv', header=None, delimiter=';', decimal=',')
    # print(df)
    df = df.T
    # print(df)
    df.set_axis(['Rynek', 'Powierzchnia', 'Rok', 'Liczba'], axis=1, inplace=True)
    print(df)
    df['Liczba'] = pd.to_numeric(df['Liczba'])
    print(df)
    ###########################################################################
    plt.subplot(1, 2, 1)
    tmp = df.groupby('Powierzchnia').agg({'Liczba': ['sum']})
    print(tmp)
    print(tmp.reset_index())
    print(type(tmp))
    labels = tmp.iloc[:, 1:]
    labels = labels.index.values
    values = tmp[tmp.columns[0:]].to_numpy()[:, 0]
    explode = [0.05, 0.05, 0.05, 0.05]
    # print(values)
    # print(labels)
    plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%')
    plt.title("\n".join(wrap('"Liczba" nieruchomości o powierzchni', 28)))
    plt.tight_layout()
    ###########################################################################
    plt.subplot(1, 2, 2)
    tmp = df.groupby('Rynek').sum()
    print(tmp)
    labels = tmp.iloc[:, 1:]
    labels = labels.index.values
    values = tmp[tmp.columns[0:]].to_numpy()[:, 0]
    explode = [0.05, 0]
    colors = ['magenta', 'violet']

    print(values)
    print(labels)
    plt.pie(values, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title("\n".join(wrap('"Liczba" nieruchomości danego rynku', 28)))
    circle = plt.Circle((0, 0), 0.4, color='white')
    plt.gcf().gca().add_artist(circle)
    plt.subplots_adjust(wspace=.8)
    plt.tight_layout()
    plt.show()
    ###########################################################################


if __name__ == '__main__':
    # z1()
    # z2()
    z3()
