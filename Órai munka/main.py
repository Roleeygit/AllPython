# -------------------------------------------------------- #
#bevi

print ("Név:", end=' ')
name = input()
print("Üdvözöllek:",name )
age = input("Életkor:")
print("Huhaa", age, "Tényleg?")
newAge = int(age) * 2 
print("Ha eléred:", newAge, "basszameg nagyon öreg leszel!")

print("--------------------------------------")
#--------------------------------------------------------- #
#301-es feladat:
#terkúp 

# File: main.px
# Author: Juhász Roland
# Copyright: 2021, Juhász Eoland 
# Group: Szoft I N
# Date: 2021-10-22
# Github: https://github.com/jani/
# Licenc: GNU GPL

import math
print("Juhász Roland 2021-10-22 Szoft I N")
print("Feladat 0301")
print("Kör alapú kúp térfogata")
print("--------------------------------------")

radius = float(input("Sugár:"))
height = float(input("Magasság:"))

volume = 1/3 * pow(radius, 2) * math.pi * height 
print("Térfogat:", volume)

#--------------------------------------------------------- #

num1 = int(input("Szám1: "))
num2 = int(input("Szám2: "))


if num1 > num2 : 
  print("Az első szám nagyobb")
else:
  print("A második szám nagyobb.")


#--------------------------------------------------------- #
#304-es feladat:
#autokoltseg

print('Juhász Roland, 2021-10-22, Szoft I N')
print('0304 feladat megoldása:')
print('Jármű Költség')
print("----------------------------")
print("Mennyit költünk km-enként az adó,garázs költség, javítás, és a benzín ára alapján?")
ado = float(input("Adó:"))
garazs = float(input("Garázs:"))
javitas = float(input("Javítási:"))
benzin = float(input("Benzin:"))

ut = float(input("Út (km):"))

osszkoltseg = ado + garazs + javitas + benzin; 
egykilometer = osszkoltseg/ ut 
print("1km költség a hónapban:%.3f" %egykilometer)

#--------------------------------------------------------- #
#302-es feladat:
#részescske számítás

print('Juhász Roland, 2021-10-22, Szoft I N')
print('0304 feladat megoldása:')
print('részescske számítás')

so_molban = float(input("Só:(mol)"))
so_reszecske = 6 * pow(10,23) * so_molban

print("Részecskék száma :", end = '')
print("%f"% so_reszecske)

#--------------------------------------------------------- #
#272-es feladat:
#Számítás

import math 
print('Juhász Roland, 2021-10-22, Szoft I N')
print('0304 feladat megoldása:')
print('Számítás')

a = 48
b = 51

eredmeny = (a/b) * math.pow(2, 3)
print ("Végeredmény: %.4f "% eredmeny)

#--------------------------------------------------------- #

