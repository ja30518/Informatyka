# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:03:56 2021

@author: Aga
"""

ILOSC_LAT = 7
ILOSC_MIESIECY_W_ROKU = 12
PROCENT = 0.07

WPLATA_MIESIECZNA = 150

stan_konta = 0.0

for rok in range(1, ILOSC_LAT + 1):
    for miesiac in range(1, ILOSC_MIESIECY_W_ROKU + 1):
        stan_konta += WPLATA_MIESIECZNA
        print(stan_konta)
        stan_konta += stan_konta * PROCENT
        
print(stan_konta)
        