# File: main.px
# Author: Juhász Roland
# Copyright: 2021, Juhász Roland 
# Group: Szoft I N
# Date: 2021-11-04
# Github: https://github.com/jani/
# Licenc: GNU GPL

print("Juhász Roland 2021-11-04 Szoft I N")
print("Feladat 1001")
print("Kicsiből nagybetű")
print("--------------------------------------")



szam = str(input('Milyen számokkal szeretnénk dolgozni: „Egész/Valós? E vagy V válasz:'))

if szam == 'E':
    ertek = int(input('Egész szám:'))
if szam == 'V':
    ertek2 = float(input('Valós szám:'))
    eredmeny = ertek2 * 2
    print(eredmeny)

