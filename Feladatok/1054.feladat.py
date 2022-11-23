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


s = str(input('Karakter:'))

def reverse(s):
    s2 = ""
    for ch in s:
        s2 = ch + s2
    return s2


print(reverse(s))

