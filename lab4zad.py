import sys


class NaZakupy:
    nazwa_produktu = 'nazwa_produktu'
    ilosc = 0
    jednostka_miary = 'kg'
    cena_jednostki = 1

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jednostki):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jednostki = cena_jednostki

    def wyswietl_produkt(self):
        print('nazwa_produktu:'
              + self.nazwa_produktu
              + '\nilosc:' + str(self.ilosc)
              + '\njednostka miary:'
              + self.jednostka_miary
              + '\ncena jednostki:'
              + str(self.cena_jednostki))

    def ile_produktu(self):
        return str(self.ilosc) + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jednostki


class CiagArytmetyczny:
    ciag = []
    a1 = 0
    r = 0
    dlugosc_ciagu = 0

    def __init__(self, a1, r, dlugosc_ciagu):
        self.a1 = a1
        self.r = r
        self.dlugosc_ciagu = dlugosc_ciagu

    def wyswietl_dane(self):
        print('a1: ' + str(self.a1) + ', r: ' + str(self.r) + ', dlugosc ciagu: ' + str(self.dlugosc_ciagu), sep='')
        print(self.ciag)

    def pobierz_elementy(self, ciag):
        self.ciag = ciag

    def pobierz_parametry(self, a1, r):
        self.a1 = a1
        self.r = r

    def policz_sume(self):
        return sum(self.ciag)

    def policz_elementy(self):
        self.ciag = [x * self.r + self.a1 for x in range(0, self.dlugosc_ciagu + 1)]


class Robaczek:
    x = 0
    y = 0
    krok = 0

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def podaj_pozycje(self):
        return [self.x, self.y]

    def idz_w_gore(self):
        self.y += self.krok

    def idz_w_dol(self):
        self.y -= self.krok

    def idz_w_lewo(self):
        self.x -= self.krok

    def idz_w_prawo(self):
        self.x += self.krok


def lab4():
    # zad 1
    plik = open('liczby.txt', 'w+')
    liczby = [x**2 for x in range(0, 31)]
    plik.writelines("%s\n" % l for l in liczby)
    plik.close()
    # zad 2
    plik = open('liczby.txt', 'r')
    print(plik.read())
    plik.close()
    # zad 3
    with open('plikWith.txt', 'w+') as plik2:
        plik2.writelines('new line 1\n')
        plik2.writelines('new line 2\n')
        plik2.writelines('new line 3\n')
    # zad 4
    na_zakupy = NaZakupy('produkt 1', 5.3, 'kg', 3.5)
    na_zakupy.wyswietl_produkt()
    print(na_zakupy.ile_produktu())
    print(na_zakupy.ile_kosztuje())
    # zad 5
    ciag_arytmetyczny = CiagArytmetyczny(1, 5, 10)
    ciag_arytmetyczny.policz_elementy()
    ciag_arytmetyczny.wyswietl_dane()
    print(str(ciag_arytmetyczny.policz_sume()))
    # zad 6
    robaczek = Robaczek(0, 0, 1)
    print(robaczek.podaj_pozycje())
    robaczek.idz_w_gore()
    robaczek.idz_w_gore()
    robaczek.idz_w_gore()
    print(robaczek.podaj_pozycje())
    robaczek.idz_w_prawo()
    robaczek.idz_w_prawo()
    robaczek.idz_w_prawo()
    print(robaczek.podaj_pozycje())
    robaczek.idz_w_dol()
    robaczek.idz_w_dol()
    print(robaczek.podaj_pozycje())
    robaczek.idz_w_lewo()
    robaczek.idz_w_lewo()
    print(robaczek.podaj_pozycje())


if __name__ == '__main__':
    lab4()
