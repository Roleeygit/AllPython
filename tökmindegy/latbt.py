from dolgozo import Dolgozo

class Latbt:

  def olvas_fajl(self):
    fp = open('latbt.txt', 'r', encoding='utf-8')
    lines = fp.readlines()
    fp.close()


    self.dolgozok = []
    for line in lines:
      (nev, telepules, fizetes) = line.split(':')
      dolgozo = Dolgozo(nev, telepules, fizetes)
      self.dolgozok.append(dolgozo)

  def szamitAtlag(self):
     osszeg = 0  
     for dolgozo in self.dolgozok:
         osszeg = osszeg + dolgozo.fizetes 

  def kiirTelepulesek(self):
    volt_telepules =  []
    for dolgozo in self.dolgozok:
        if dolgozo.telepules not in volt_telepules: 
            print(dolgozo.telepules)
            volt_telepules.append(dolgozo.telepules)


  def bekerDolgozo(self):
    new_dolgozo = []
    uj_dolgozo = input('dolgozo neve: ')
    uj_telepules = input('telepules neve:')
    uj_fizetes = input('fizetes')
    for line in new_dolgozo:
      (uj_dolgozo, uj_telepules, uj_fizetes) = line.split(':')
      dolgozo = Dolgozo(uj_dolgozo, uj_telepules, int(uj_fizetes))
      self.dolgozok.append(dolgozo)


  def kiirFajlba(self,dolgozo):
    fp = open('uj.txt', 'w', encoding='utf-8') 
    fp.write(dolgozo.nev)
    fp.write(':')
    fp.write('\n')
    fp.write(dolgozo.telepules)
    fp.write(':')
    fp.write('\n')
    fp.write(dolgozo.fizetes)
    fp.write('\n')

    fp.close()

latbt = Latbt() #peldányositás(5 os feladat)
latbt.olvas_fajl()          
latbt.szamitAtlag() # (objektum meghivás 6-7 feladat)
latbt.kiirTelepulesek()
latbt.bekerDolgozo()
latbt.kiirFajlba()

