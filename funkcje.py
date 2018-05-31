#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: hamowanie.py
# Authors: Mateusz Ciesielski, Jakub Kaliszewski, Artur Matusiak

import pylab
#definicja używaych bibliotek

g = float(9.81)#definicja stałej g
plik = open("hamowanie.txt", "w+")  # zdefiniowanie strumienia do pliku

def wprowadzenie(V, T, C):
    global Predkosc, Tarcie, Czas_Reakcji#deklaracja zmiennych, są globalne
    Predkosc = float(V)#funkcja wczytania strumienia jako float do zmiennej Predkosc
    Tarcie = float(T)#funkcja wczytania strumienia jako float do zmiennej Tarcie
    Czas_Reakcji=float(C)

def obliczenia():
    global Droga, Czas, Czascal,Przyspieszenie,a1,a2,a3,a4,t1,t2,t3,t4,dr1,dr2,dr3,dr4 #deklaracja zmiennych, są globalne
    Przyspieszenie = float(Tarcie * g)#obliczenie przyspieszenia
    Czas = float(Predkosc/Przyspieszenie)
    Czascal = Czas + Czas_Reakcji#obliczenie czasu, dodałem czas reakcji
    Droga = float((Predkosc*Czas_Reakcji) + ((Przyspieszenie*Czas**2)/2) + (Predkosc*Czas))
    a1=float(0.9*g)
    a2=float(0.6*g)
    a3=float(0.3*g)
    a4=float(0.05*g)
    t1 = float(Predkosc / a1)
    t2 = float(Predkosc / a2)
    t3 = float(Predkosc / a3)
    t4 = float(Predkosc / a4)
    dr1=float((Predkosc * t1) - (a1 * t1 ** 2) / 2 + Predkosc * Czas_Reakcji)
    dr2=float((Predkosc * t2) - (a2 * t2 ** 2) / 2 + Predkosc * Czas_Reakcji)
    dr3=float((Predkosc * t3) - (a3 * t3 ** 2) / 2 + Predkosc * Czas_Reakcji)
    dr4=float((Predkosc * t4) - (a4 * t4 ** 2) / 2 + Predkosc * Czas_Reakcji)

def ZwrocDroge(): ##Wywolywana w glownym programie, by moc potem wypisac wynik w MessageBox
    Droga = float((Predkosc*Czas_Reakcji) + ((Przyspieszenie*Czas**2)/2) + (Predkosc*Czas))
    return Droga

def ZwrocCzasCal(): ##Wywolywana w glownym programie, by moc potem wypisac wynik w MessageBox
    Czascal = float((Predkosc/Przyspieszenie) + (Czas_Reakcji))
    return Czascal

def ZapisDoPliku(plik):
    plik.write("t[s]\tv[m/s]\ts[m]\n");
    s1 = []
    for i in pylab.frange(0.000, Czas_Reakcji, 0.001):
        Droga = float(Predkosc * i)
        s1.append(Droga)  # dopisanie wyniku na koniec listy
        Predkosc_Chwilowa = float(Predkosc)
        bufor = str("{0:.3f}".format(i))  # zamiana wartosci i (czas) na string, wymagania funkcji write by na wejsciu byl string
        plik.write(bufor)  # zapisanie do pliku wartosci i (czas)
        plik.write("\t")  # zrobienie tabulacji w pliku
        bufor2 = str("{0:.3f}".format(Predkosc_Chwilowa))  # zamiana wartosci v2 na string, wymagania funkcji write
        plik.write(bufor2)  # zapisanie do pliku wartosci v2
        plik.write("\t")  # zrobienie tabulacji w pliku
        bufor3 = str("{0:.3f}".format(Droga))  # zamiana wartosci v2 na string, wymagania funkcji write
        plik.write(bufor3)  # zapisanie do pliku wartosc
        plik.write('\n')  # przejscie do nowej lini w pliku
        if (i == Czas_Reakcji): Zapamietana = Droga

    for i in pylab.frange(0.001, Czas, 0.001):
        Droga = float((Predkosc * i)-(Przyspieszenie * i ** 2) / 2+Zapamietana)
        Predkosc_Chwilowa=Predkosc-(i*Przyspieszenie)
        s1.append(Droga)#dopisanie wyniku na koniec listy
        bufor4 = str("{0:.3f}".format(i + Czas_Reakcji))  # zamiana wartosci i (czas) na string, wymagania funkcji write
        plik.write(bufor4)  # zapisanie do pliku wartosci i (czas)
        plik.write("\t")  # zrobienie tabulacji w pliku
        bufor5 = str("{0:.3f}".format(Predkosc_Chwilowa))  # zamiana wartosci v2 na string, wymagania funkcji write
        plik.write(bufor5)  # zapisanie do pliku wartosci v2
        plik.write("\t")  # zrobienie tabulacji w pliku
        bufor6 = str("{0:.3f}".format(Droga + Zapamietana))  # zamiana wartosci Droga na string, wymagania funkcji write
        plik.write(bufor6)  # zapisanie do pliku wartosc
        plik.write('\n')  # przejscie do nowej lini w pliku

def wykres1(CzyPrzykladowe):
    #Obliczanie wartosci
    t = pylab.frange(0.000, Czascal, 0.001)# lista argumentów osi x od <0;czas>, wykorzystanie biblioteki, frange obsługuje float
    s1 = []# lista wartości, lista, wyniki obliczeń na dole wpisywane
    if(CzyPrzykladowe==0):
        s2=[]
        s3=[]
        s4=[]
        s5=[] # dla innych wsp.

    for i in pylab.frange(0.000,Czas_Reakcji,0.001):
        Droga = float(Predkosc * i)
        s1.append(Droga)#dopisanie wyniku na koniec listy
        if (CzyPrzykladowe == 0):
            s2.append(Droga)
            s3.append(Droga)
            s4.append(Droga)
            s5.append(Droga)
        if(i>=Czas_Reakcji): Zapamietana = Droga


    for i in pylab.frange(0.001, Czas, 0.001):
        LimDroga=float((Predkosc * i)-(a4 * i ** 2) / 2+Zapamietana)
        Droga = float((Predkosc * i)-(Przyspieszenie * i ** 2) / 2+Zapamietana)
        s1.append(Droga)#dopisanie wyniku na koniec listy
        if (CzyPrzykladowe == 0):
            Drogaa = float((Predkosc * i)-(a1 * i ** 2) / 2+Zapamietana)
            if (i<=t1): s2.append(Drogaa)
            else: s2.append(dr1) #Ify dodane, by nie liczylo (a potem nie rysowalo) ujemnej drogi i predkosci
            Drogaa = float((Predkosc * i)-(a2 * i ** 2) / 2+Zapamietana)
            if (i<=t2): s3.append(Drogaa)
            else: s3.append(dr2)
            Drogaa = float((Predkosc * i)-(a3 * i ** 2) / 2+Zapamietana)
            if (i<=t3): s4.append(Drogaa)
            else: s4.append(dr3)
            Drogaa = float((Predkosc * i)-(a4 * i ** 2) / 2+Zapamietana)
            if (i<=t4): s5.append(Drogaa)
            else: s5.append(dr4)

#Wykres droga
    pylab.figure()
    pylab.plot(t, s1)#podanie danychdo wykresu
    pylab.text(ZwrocCzasCal() / 10, LimDroga - 2 * (LimDroga/8), ' '.join(['Ft=', str(Tarcie)]), fontsize=10, color='#1009f2')  # (Pozycja x, Pozycja y, Podpis, Wielkosc fonta, Kolor)
    if (CzyPrzykladowe == 0):
        pylab.plot(t, s2)
        pylab.text(ZwrocCzasCal()/10, LimDroga - 3*(LimDroga/8) , 'Ft=0.9',fontsize=10,color='#2f7013')
        pylab.plot(t, s3)
        pylab.text(ZwrocCzasCal()/10, LimDroga - 4*(LimDroga/8), 'Ft=0.6',fontsize=10, color='#c72923')
        pylab.plot(t, s4)
        pylab.text(ZwrocCzasCal()/10, LimDroga - 5*(LimDroga/8), 'Ft=0.3',fontsize=10,color='#4dd3ed')
        pylab.plot(t, s5)
        pylab.text(ZwrocCzasCal()/10, LimDroga - 6*(LimDroga/8), 'Ft=0.05',fontsize=10,color='#b56afe')
    pylab.ylabel('Droga [m]', fontsize=10)#opis osi y
    pylab.xlabel('Czas [s]', fontsize=10)#opis osi x
    pylab.title('Zaleznosc s[t] w trakcie hamowania', fontsize=11)#Tytuł wykresu
    pylab.grid(True)#wykres ma byc ciagly
    pylab.savefig('S_od_t.png', dpi=300)  # zapis wykresu do pliku automatycznie
    fig = pylab.gcf()
    fig.canvas.set_window_title(u'Zalezność s[t] w trakcie hamowania')  # Tytuł okienka z wykresami
    pylab.show()

def wykres2(CzyPrzykladowe):
    t = pylab.frange(0.000, Czascal, 0.001)# lista argumentów osi x od <0;czas>, wykorzystanie biblioteki, frange obsługuje float
    v = []  # lista wartości, lista, wyniki obliczeń na dole wpisywane
    if (CzyPrzykladowe == 0):
        v1 = []
        v2 = []
        v3 = []
        v4 = []  # dla innych wsp.
    for i in pylab.frange(0.000,Czas_Reakcji,0.001):
        Droga = float(Predkosc * i)
        Predkosc_Chwilowa = float(Predkosc)
        v.append(Predkosc_Chwilowa)#dopisanie wyniku na koniec listy
        if (CzyPrzykladowe == 0):
            v1.append(Predkosc_Chwilowa)
            v2.append(Predkosc_Chwilowa)
            v3.append(Predkosc_Chwilowa)
            v4.append(Predkosc_Chwilowa)
        if (i >= Czas_Reakcji): Zapamietana = Droga

    for i in pylab.frange(0.001, Czas, 0.001):
        Predkosc_Chwilowa = float(Predkosc - Przyspieszenie * i)
        v.append(Predkosc_Chwilowa)  # dopisanie wyniku na koniec listy
        if (CzyPrzykladowe == 0):
            Predkosc_Chwilowa2 = float(Predkosc - a1 * i)
            if (Predkosc_Chwilowa2 >= 0):
                v1.append(Predkosc_Chwilowa2)
            else:
                v1.append(0)
            Predkosc_Chwilowa2 = float(Predkosc - a2 * i)
            if (Predkosc_Chwilowa2 >= 0):
                v2.append(Predkosc_Chwilowa2)
            else:
                v2.append(0)
            Predkosc_Chwilowa2 = float(Predkosc - a3 * i)
            if (Predkosc_Chwilowa2 >= 0):
                v3.append(Predkosc_Chwilowa2)
            else:
                v3.append(0)
            Predkosc_Chwilowa2 = float(Predkosc - a4 * i)
            if (Predkosc_Chwilowa2 >= 0):
                v4.append(Predkosc_Chwilowa2)
            else:
                v4.append(0)
    pylab.figure()
    pylab.plot(t, v)
    pylab.text(ZwrocCzasCal()/10, Predkosc - 1*(Predkosc/8), ' '.join(['Ft=', str(Tarcie)]), fontsize=11, color='#1009f2') #(Pierwsze 2 atr. okreslaja pozycje X i Y)
    if (CzyPrzykladowe == 0):
        pylab.text(ZwrocCzasCal()/10, Predkosc - 2*(Predkosc/8),'Ft = 0.05', fontsize=11, color='#b56afe')
        pylab.text(ZwrocCzasCal()/10, Predkosc - 3*(Predkosc/8),'Ft = 0.3', fontsize=11, color='#4dd3ed')
        pylab.text(ZwrocCzasCal()/10, Predkosc - 4*(Predkosc/8),'Ft = 0.6', fontsize=11, color='#c72923')
        pylab.text(ZwrocCzasCal()/10, Predkosc - 5*(Predkosc/8),'Ft = 0.9', fontsize=11, color='#2f7013')
        pylab.plot(t, v1)
        pylab.plot(t, v2)
        pylab.plot(t, v3)
        pylab.plot(t, v4)
    pylab.ylabel('Predkosc [m/s]', fontsize=10)#opis osi y
    pylab.xlabel('Czas [s]', fontsize=10)#opis osi x
    pylab.title('Zaleznosc v[t] w trakcie hamowania', fontsize=11)#Tytuł wykresu
    pylab.grid(True)#wykres ma byc ciagly
    pylab.xlim([0, ZwrocCzasCal()])
    pylab.ylim([0, Predkosc + (Predkosc/10)])
    pylab.savefig('V_od_t.png', dpi=300)  # zapis wykresu do pliku automatycznie
    fig = pylab.gcf()
    fig.canvas.set_window_title(u'Zalezność v[t] w trakcie hamowania')#Tytuł okienka z wykresami
    pylab.show()

def wykres3(CzyPrzykladowe):
    vv = pylab.frange(0.00, 60, 0.01)
    ss = []
    ss1 = []
    ss2 = []
    ss3 = []
    ss4 = []
    for i in pylab.frange(0.00, 60, 0.01):#3ci wykres
        Czazz=i/(Tarcie * g)
        if (CzyPrzykladowe == 0):
            Czazz1=i/(0.9 * g)
            Czazz2=i/(0.6 * g)
            Czazz3=i/(0.3 * g)
            Czazz4=i/(0.05 *g)
        Drogaaa=float((Czazz * i)-(Tarcie * Czazz ** 2) / 2)
        ss.append(Drogaaa)
        if (CzyPrzykladowe == 0):
            Drogaaa=float((Czazz1 * i)-(0.9* Czazz1**2)/2)
            ss1.append(Drogaaa)
            Drogaaa=float((Czazz2 * i)-(0.6* Czazz2**2)/2)
            ss2.append(Drogaaa)
            Drogaaa=float((Czazz3 * i)-(0.3* Czazz3**2)/2)
            ss3.append(Drogaaa)
            Drogaaa=float((Czazz4 * i)-(0.05* Czazz4**2)/2)
            ss4.append(Drogaaa)
    pylab.figure()
    pylab.plot(vv, ss)
    pylab.text(5, 900, ' '.join(['Ft=', str(Tarcie)]), fontsize=11, color='#1009f2')
    if (CzyPrzykladowe == 0):
        pylab.text(5, 850,'Ft=0.9', fontsize=11, color='#2f7013')
        pylab.text(5, 800,'Ft=0.6', fontsize=11, color='#c72923')
        pylab.text(5, 750,'Ft=0.3', fontsize=11, color='#4dd3ed')
        pylab.text(5, 700,'Ft=0.05', fontsize=11, color='#b56afe')
        pylab.plot(vv, ss1)
        pylab.plot(vv, ss2)
        pylab.plot(vv, ss3)
        pylab.plot(vv, ss4)
    pylab.ylabel('Droga [m]', fontsize=10)
    pylab.xlabel('Predkosc [m/s]', fontsize=10)
    pylab.title('Zaleznosc drogi hamowania od predkosci poczatkowej', fontsize=11)  # Tytuł wykresu
    pylab.grid(True)
    pylab.xlim([0, 62])
    pylab.ylim([0, ((20 * 60) - (Tarcie * 20 ** 2) / 2) + 2])
    pylab.savefig('Droga_hamowania_od_pred_pocz.png', dpi=300)  # zapis wykresu do pliku automatycznie
    fig = pylab.gcf()
    fig.canvas.set_window_title(u'Zalezność drogi hamowania od prędkości początkowej')  # Tytuł okienka z wykresami
    pylab.show()  # pokazanie wykresu

def program():
    plik = open("hamowanie.txt", "w+")
    ZapisDoPliku(plik)
    plik.close()#zamkniecie strumienia do pliku