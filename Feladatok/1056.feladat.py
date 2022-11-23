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

szam = input("Karakter:")
string = szam.lower()
count = 0
list1 = ["a","e","i","o","u"]
for char in szam:
    if char in list1:
        count = count+1

print('magánhangzók száma:',count)
