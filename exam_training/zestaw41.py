import math

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Zad.1. Na jednym wykresie narysuj wykresy krzywych: y = log(2x), y = −4x + 2, y = 2 cos(x) na przedziale
# [0.5, 10]. Wykres powinien posiadać tytuł, legendę, podpisane etykiety obu osi. Dodaj siatkę na wykres.
# Linie krzywych powinny mieć różne style i różne kolory inne niż domyślne. Zapisz wykres w formacie png za
# pomocą kodu.
def z1():
    print('zadanie 1')
    x = np.linspace(0.5,10, 1000)
    y1 = np.log10(2*x)
    y2 = -4*x + 2
    y3 = 2 * np.cos(x)
    plt.plot(x, y1, '-', color='tan', label='y = log(2x)')
    plt.plot(x, y2, '--', color='teal', label='y = -4x + 2')
    plt.plot(x, y3, ':', color='lawngreen', label='y = 2cos(x)')
    plt.title('Wykres krzywych')
    plt.xlabel('Wartości x')
    plt.ylabel('Wartości y')
    plt.legend()
    plt.grid(color='r', linestyle='--', linewidth=0.3)
    plt.savefig('wykres_funkcji_zad_1.png')
    plt.show()



# Zad.2. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku ceny41.xlsx jako ramkę danych (Data Frame),
# • wyświetl na konsoli średnią cenę poszczególnych produktów ze wszystkich miesięcy
# Produkt 1 - średnia ze wszystkich miesięcy
# Produkt 2 - średnia ze wszystkich miesięcy
# • stwórz wykres liniowy prezentujący dane zawarte w ramce danych (wszystkie dane)
# • umieść swój numer indeksu w lewym dolnym rogu wykresu.
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
# Zapisz wykres w formacie jpg za pomocą kodu.
def z2():
    print('zadanie 2')
    excel = pd.ExcelFile('ceny41.xlsx')
    df = pd.read_excel(excel, header=0)
    print(df)
    # tmp = df.groupby("Roodzaje towarów i usług").add({'Wartosc': ['sum']})
    # print(tmp)
    df.groupby(['Miesiące', 'Rodzaje towarów i usług']).size().unstack().plot(kind='bar', stacked=False)
    # df.plot(kind='bar', x=0, y=3, legend=True)
    plt.legend(loc='best')
    plt.title('Ceny produktów w 2017 roku')
    plt.xlabel('Miesiące')
    plt.ylabel('Wartosc')
    plt.show()


# Zad.3. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku cechy41.csv,
# • podziel wartości obu cech na koszyki od 0 do 200 z krokiem 50
# • stwórz wykres słupkowy poziomy prezentujący dane zawarte w pliku (mogą być dwa wykresy)
# • Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
# Zapisz wykres w formacie png za pomocą kodu.
def z3():
    print('zadanie 3')
    df = pd.read_csv('cechy41.csv', delimiter=';', decimal=',')
    print(df)



if __name__ == '__main__':
    z1()
    # z2()
    z3()
