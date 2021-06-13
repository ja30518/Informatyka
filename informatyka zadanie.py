# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = input('Wpisz liczbę z przedziału od 0-1 ')
x = float(x)
if 0<x<=1:
    wyniki= []
    print ("Liczba jest poprawna")
    for a in range (0,1001):
        for b in range (1,1001):
            y = a / b
            if abs(x-y)/abs(x)<0.01:
                #print(x,y,a,b)
                c = len(str(a))+len(str(b))
                wyniki.append((c,x,y,a,b))
    wyniki = sorted(wyniki)
    c,x,y,a,b = wyniki[0]
    print(f'{x} = {a}/{b} ')