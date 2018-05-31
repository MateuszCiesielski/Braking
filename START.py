#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: hamowanie.py
# Authors: Mateusz Ciesielski, Jakub Kaliszewski, Artur Matusiak

import Tkinter #biblioteka odpowiedzialna za GUI
import tkMessageBox #biblioteka odpowiedzialna za wyskakujące okienka
import funkcje #plik z funkcjami
from Tkinter import *

window = Tk() # utworzenie okna
window.minsize(550,250) #minimalne wymiary okna
window.title(u"Hamowanie pojazdow") #tytuł
window.configure(bg="#4C66FF")
window.iconbitmap(default="icon.ico")

def error(): #wypisywanie błędu w przypadku podania złych danych
    tkMessageBox.showinfo(u'Błąd', u'Podano nieprawidłowe dane.')

def statusWlasny(): #zmiana z wybierania z listy na wpisywanie własnego współczynnika
    global status
    status=1
    Dane_wybor.pack_forget()
    Dane_wlasne.pack(side=LEFT)
    Lista.pack_forget()
    E2.pack(side=RIGHT)
    Button_wlasne.pack_forget()
    Button_wybor.pack()

def statusWybor(): #zmiana z wpisywania własnego na wybór z listy
    global status
    status=0
    Dane_wlasne.pack_forget()
    Dane_wybor.pack(side=LEFT)
    E2.pack_forget()
    Lista.pack(side=RIGHT)
    Button_wybor.pack_forget()
    Button_wlasne.pack()


def zamiana(zmienna):
    if (((zmienna.replace('.','',1).isdigit() == True) or (zmienna.replace(',','',1).isdigit() == True)) and ((zmienna.replace('.','',1)>0) or (zmienna.replace(',','',1)>0))):#w sprytny sposob sprawdzam czy string jest liczba
        return float(zmienna.replace(",", "."))#Jesli tak to funkcja zwraca float
    else:  return 0

def helloCallBack():
    b=0.5 #zadeklarowanie zmiennej b, bo jak jest tylko w if'ie to nie działa
    if (status == 0): #jeśli status = 0 to znaczy, że współczynnik został wybrany z listy
        if(wybrane_tarcie.get() == tarcie[0]): b = 0.9
        if(wybrane_tarcie.get() == tarcie[1]): b = 0.6
        if(wybrane_tarcie.get() == tarcie[2]): b = 0.3
        if(wybrane_tarcie.get() == tarcie[3]): b = 0.05
    else: #współczynnik wprowadzony przez użytkownika
        if(zamiana(E2.get())!=0): b=zamiana(E2.get())
        else: error()
    if(zamiana(E1.get())==0 or zamiana(E3.get())==0): error()
    else:
        a=zamiana(E1.get())
        c=zamiana(E3.get())
        funkcje.wprowadzenie(a, b, c)
        funkcje.obliczenia()
        DrogaKoncowa=funkcje.ZwrocDroge()
        CzasKoncowy=funkcje.ZwrocCzasCal()
        string1="%.4f" %DrogaKoncowa
        string2="%.4f" %CzasKoncowy
        lines=[''.join([u'Droga całkowita wynosi: \t', string1, '[m/s]']), ''.join([u'Czas końcowy wynosi: \t', string2, '[s]'])]
        Wyniki='\n'.join(lines)
        tkMessageBox.showinfo(u'Wyniki', Wyniki)
        funkcje.program()

#==================funkcje wyświetlające wykres=================================
def wyswietlWykres1():
    b=0.5
    if (status == 0):
        if(wybrane_tarcie.get() == tarcie[0]): b = 0.9
        if(wybrane_tarcie.get() == tarcie[1]): b = 0.6
        if(wybrane_tarcie.get() == tarcie[2]): b = 0.3
        if(wybrane_tarcie.get() == tarcie[3]): b = 0.05
    else: 
        if(zamiana(E2.get())!=0): b=zamiana(E2.get())
        else: error()
    if(zamiana(E1.get())==0 or zamiana(E3.get())==0): error()
    else:
        a=zamiana(E1.get())
        c=zamiana(E3.get())
        funkcje.wprowadzenie(a, b, c)
        funkcje.obliczenia()
        funkcje.wykres1(przykladowe1.get())

def wyswietlWykres2():
    b=0.5
    if (status == 0):
        if(wybrane_tarcie.get() == tarcie[0]): b = 0.9
        if(wybrane_tarcie.get() == tarcie[1]): b = 0.6
        if(wybrane_tarcie.get() == tarcie[2]): b = 0.3
        if(wybrane_tarcie.get() == tarcie[3]): b = 0.05
    else: 
        if(zamiana(E2.get())!=0): b=zamiana(E2.get())
        else: error()
    if(zamiana(E1.get())==0 or zamiana(E3.get())==0): error()
    else:
        a=zamiana(E1.get())
        c=zamiana(E3.get())
        funkcje.wprowadzenie(a, b, c)
        funkcje.obliczenia()
        funkcje.wykres2(przykladowe2.get())

def wyswietlWykres3():
    b=0.5
    if (status == 0):
        if(wybrane_tarcie.get() == tarcie[0]): b = 0.9
        if(wybrane_tarcie.get() == tarcie[1]): b = 0.6
        if(wybrane_tarcie.get() == tarcie[2]): b = 0.3
        if(wybrane_tarcie.get() == tarcie[3]): b = 0.05
    else: 
        if(zamiana(E2.get())!=0): b=zamiana(E2.get())
        else: error()
    if(zamiana(E1.get())==0 or zamiana(E3.get())==0): error()
    else:
        a=zamiana(E1.get())
        c=zamiana(E3.get())
        funkcje.wprowadzenie(a, b, c)
        funkcje.obliczenia()
        funkcje.wykres3(przykladowe3.get())

status=0 # jeśli status=0 to współczynnik jest wybierany z listy, jeśli status=1 jest samodzielnie wpisywany

#========================================================================================================
#ramka 1 - prędkość
#========================================================================================================
frame1=Frame(window, bg="#4C66FF")
frame1.pack(padx=10)
Tytul=Label(frame1,bg="#4C66FF",width=30,text=u"Dane wejściowe.")
Tytul.pack(side=TOP)

Dane=Label(frame1,width=30,bg="#4C66FF",justify=LEFT,compound = LEFT, text=u"Podaj predkość początkową[m/s]:")
Dane.pack(side=LEFT)
E1=Entry(frame1, bd=5)
E1.pack(side=RIGHT)
#========================================================================================================
#ramka 2 - wybor wspolczynika tarcia
#========================================================================================================
frame2=Frame(window, bg="#4C66FF")
frame2.pack(side=TOP, pady=5)
Dane_wlasne=Label(frame2,width=30,bg="#4C66FF",justify=LEFT,compound = LEFT,text=u"Podaj współczynnik tarcia:")
Dane_wybor=Label(frame2,width=30,bg="#4C66FF",justify=LEFT,compound = LEFT,text=u"Wybierz współczynnik tarcia:")
Dane_wybor.pack(side=LEFT) # domyślnie wyświetlony label dla wybierania z listy
tarcie = [u"0.9 - jezdnia sucha, opona zużyta",
 u"0.6 - jezdnia wilgotna, nowa opona",
 u"0.3 - silny deszcz, nowa opona",
 u"0.05 - lód, nowa opona"]
wybrane_tarcie = StringVar(window)
wybrane_tarcie.set(u"0.9 - jezdnia sucha, opona zużyta") # Domyslnie wybrane

Lista=OptionMenu(frame2, wybrane_tarcie, *tarcie)
Lista.configure(bg="#4E557F")
E2=Entry(frame2, bd=5)
Lista.pack(side=RIGHT) # domyślnie wyświetlona lista
#========================================================================================================
#ramka 3 - zmiana wprowadzania współczynnika tarcia
#========================================================================================================
frame3=Frame(window, bg="#4C66FF")
frame3.pack(side=TOP, pady=5)
Button_wlasne = Tkinter.Button(frame3,bg="#4E557F", text = u"lub podaj własny", command = statusWlasny)
Button_wybor = Tkinter.Button(frame3,bg="#4E557F", text = u"lub wybierz z listy", command = statusWybor)
Button_wlasne.pack() #domyślnie przycisk na przełączenie w tryb wpisywania
#========================================================================================================
#ramka 4 - czas reakcji kierowcy
#========================================================================================================
frame4=Frame(window, bg="#4C66FF")
frame4.pack(side=TOP, pady=5)
Dane=Label(frame4,width=30,bg="#4C66FF",justify=LEFT,compound = LEFT,text=u"Podaj czas reakcji kierowcy[s]:")
Dane.pack(side=LEFT)
E3=Entry(frame4, bd=5)
E3.pack(side=RIGHT)
#========================================================================================================
#ramki5+ - wyświetlanie wykresów
#========================================================================================================
przykladowe1=IntVar()
przykladowe2=IntVar()
przykladowe3=IntVar()
frame5=Frame(window, bg="#4C66FF")
frame5.pack(side=TOP, pady=5)
Tkinter.Button(frame5, width=40,bg="#4E557F", text=u"Wyświetl wykres s[t]",command = wyswietlWykres1).pack(side=LEFT)
Checkbutton(frame5,bg="#4C66FF", text=u"+ wykresy przykładowych współczynników", variable = przykladowe1, onvalue=0, offvalue=1).pack(side=RIGHT)
frame6=Frame(window, bg="#4C66FF")
frame6.pack(side=TOP, pady=5)
Tkinter.Button(frame6, width=40,bg="#4E557F", text=u"Wyświetl wykres v[t]", command = wyswietlWykres2).pack(side=LEFT)
Checkbutton(frame6,bg="#4C66FF", text=u"+ wykresy przykładowych współczynników", variable = przykladowe2, onvalue=0, offvalue=1).pack(side=RIGHT)
frame7=Frame(window, bg="#4C66FF")
frame7.pack(side=TOP, pady=5)
Tkinter.Button(frame7, width=40,bg="#4E557F", text=u"Wyświetl wykres drogi od prędkości początkowej", command = wyswietlWykres3).pack(side=LEFT)
Checkbutton(frame7,bg="#4C66FF", text=u"+ wykresy przykładowych współczynników", variable = przykladowe3, onvalue=0, offvalue=1).pack(side=RIGHT)
#========================================================================================================
# obliczanie
#========================================================================================================
Tkinter.Button(window, width=60,bg="#4E557F", text=u"Oblicz drogę hamowania i zapisz wynik do pliku", command = helloCallBack).pack(pady=5)

window.mainloop() # wyświetlenie okna