def chek_planet(bolygo):
  torpek = ['Ceres','Pluto','Haumea', 'Makemake', 'Eris']
  bolygok = ['Vénusz', 'Mars', 'Jupiter', 'Szaturnusz', 'Uránusz' ,'Neptunusz']
  nagybolygo = ['Föld']
  if bolygo in torpek:
    return 'törpegolygó' 
  elif bolygo in bolygok:
    return 'bolygó'
  elif bolygo in nagybolygo:
    return "nagybolygó"
  else: 
    return 'ismeretlen'

#print(chek_planet("Pluto"))
bolygo = ""
while bolygo != "vege":
   bolygo = input("Bolygó neve:")
   uzenet = chek_planet(bolygo)
   print(uzenet)

