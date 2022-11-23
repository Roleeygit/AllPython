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


a = str(input("Első karakter:"))
b = str(input("Második karakter:"))

betű1 = ord(a)
betű2 = ord(b)


if betű1 > betű2:
    print(a,'Előtt van az.,',b)
else:
    print(b,'Előtt van az.',a)    

