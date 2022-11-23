from talon import Talon

class Dolgozok:
    def __init__ (self):
       self.file_name = 'talonkft.txt' 

    def file_read(self):
      
      fp = open(self.file_name,'r',encoding='utf-8')
      
      self.lines = fp.readlines()
      fp.close()
      
      self.dolgozok = []

      for line in self.lines:
            (nev,
            telepules,
            utca,
            szulhely,
            fizetes) = line.split(':')
            dolgozo = Talon(nev, telepules, utca, szulhely, int(fizetes),)
            self.dolgozok.append(dolgozo)  #Itt teszi bele a listába

            
    def tataidolgozok(self):
        osszeg = 0
        for tatai in self.dolgozok:
            
            if tatai.telepules == 'Tata':
                osszeg += 1
        print('Tatai városok összesen:', osszeg)

talon = Dolgozok()
talon.file_read()
talon.tataidolgozok()

