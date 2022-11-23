from kiadas import Kiadas

class Koltsegek:     


    def beiras(self):
        fp = open('kiadas.txt','a', encoding='utf-8')
        #Bekérjük az adatokat, minden egyes alkalommal az adat egy txt-fileban rögzül.
        honap = (input('Melyik havi kiadást szeretnéd rögziteni?'))
        fizetes = int(input("fizetés:"))
        viz = int(input('Viz:')) 
        villany = int(input('Villany:'))
        szemet = int(input('Szemét:'))
        telefon = int(input('Telefon:'))
        internet = int(input('Internet:'))
        kaja = int(input('Kaja:'))
        ruha = int(input('Ruha:'))
        szorakozas = int(input('Szórakozás:'))
        osszesen = viz + villany + szemet + telefon + internet + kaja + ruha + szorakozas
        print("Kiadások összesen:",osszesen,'Ft')
        vegosszeg = fizetes - osszesen
        print('Ebben a hónapban megspórolt pénz:', vegosszeg,'Ft')

        #Kiiratjuk a txt file-ba az adatokat amiket az imént bekértünk
        fp.write(honap,':')
        fp.write('\n')
        fp.write('Fizetés:')
        fp.write(str(fizetes))
        fp.write('\n')
        fp.write('Viz:')
        fp.write(str(viz))
        fp.write('\n')
        fp.write('Villany:')
        fp.write(str(villany))
        fp.write('\n')
        fp.write('Szemét:')
        fp.write(str(szemet))
        fp.write('\n')
        fp.write('Telefon:')
        fp.write(str(telefon))
        fp.write('\n')
        fp.write('Internet:')
        fp.write(str(internet))
        fp.write('\n')
        fp.write('Kaja:')
        fp.write(str(kaja))
        fp.write('\n')
        fp.write('Ruha:')
        fp.write(str(ruha))  
        fp.write('\n')
        fp.write('Szórakozás')
        fp.write(str(szorakozas))     
        fp.write('\n')
        fp.write('Ebben a hónapban ennyit költöttél:')
        fp.write(str(osszesen))
        fp.write('\n')
        fp.write('Ebben a hónapban ennyit spóroltál:')
        fp.write(str(vegosszeg))
        fp.write('\n')
        fp.write('')
        fp.close()    
     
 

koltsegek = Koltsegek()
koltsegek.beiras()
