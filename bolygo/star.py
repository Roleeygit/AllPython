from starModel import StarModel
from typing import List

class Star:
    def __init__(self):
        self.file_name = 'stars.txt'
        self.lines = []
        self.stars: List[StarModel] = []
    
    def read_content(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()
        
    
    def convert_content(self):
        for line in self.lines[1:]:
            (name, constellation, 
            distance, mass, temperature, age) = line.split(':')
            
            starModel = StarModel(
                name, constellation, 
                float(distance.replace(',','.')),
                float(mass.replace(',', '.')), 
                int(temperature), 
                float(age.replace(',', '.')))

            self.stars.append(starModel)
    
    def print_out(self):
        for star in self.stars:
            print(star.name, star.constellation)
    
    # Van-e csillag a Göncöl csillagképben
    def star_in_goncol(self):
        ker = 'Göncöl'
        i = 0
        n = len(self.stars)
        while i<n and self.stars[i].constellation.find(ker) == -1:
            i +=1
        if i<n:
            print("van") 
        else: 
            print('nincs')   

    # Legtávolabbi csillag neve, távolsága
    def farthest_star(self):
       max_star = self.stars[0]
       for star in self.stars:
           if star.distance > max_star.distance:
               max_star = star 
       print('Legtávolabbi csillag:', 
        max_star.name,max_star.distance)
        

    # Legalacsonyabb hőmérsékletű csillag
    def lowest_temperature_star(self):
        min_star = self.stars[0]
        for star in self.stars:
            if star.temperature < min_star.temperature:
                min_star = star 
        print("Legalacsonyabb hőmérsékletű csillag:",
        min_star.name, min_star.temperature)

    # A Csillagok átlagéletkor
    def average_age_of_stars(self):
        darab = len(self.stars)
        osszeg = 0
        for star in self.stars:
            osszeg = osszeg + star.age 
            atlag = osszeg / darab
        print("Csillagok átlagéletkora:%.2f" % atlag )

    # a Kepler-18 hány kiloggram tömegű
    def weight_of_kepler18(self):
        for star in self.stars:
            if star.name == 'Kepler-18':
                print( "%f" %
                    (star.mass * 1.8981 * (10**30)))

          
            
    # 150 fényévnél közelbbi bolygók neve és távolsága
    def close_stars(self):
        pass

    # A Szextánok csillagképben található csillagok adatai
    def szextan_datas(self):
        pass

    # A 2 M-nél kisebb tömegű csillagok neve és tömege
    def less_than_two_mass_stars(self):
        pass


star = Star()
star.read_content()
star.convert_content()
star.print_out()
star.star_in_goncol()
star.farthest_star()
star.lowest_temperature_star()
star.average_age_of_stars()
star.weight_of_kepler18()
star.close_stars()
star.szextan_datas()
star.less_than_two_mass_stars()





