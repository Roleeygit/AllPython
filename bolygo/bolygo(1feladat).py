#Juhász Roland 2022.01.19 Szoft I N
bolygo = input('Bolygó neve:')

if bolygo == '':
  exit()

bolygo_lista = ["Ceres","Haumea","Eris","Makemake"]
if bolygo in bolygo_lista:
  print('törpebolygó')
else: 
  print('Nem besorolt')


