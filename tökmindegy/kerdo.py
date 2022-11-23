

nev = input ('nev:')
if nev == "erno":
    print('szia ',nev)
else:
    exit()

def vizsgalAbetu(szo):
    if szo [0] == 'a':
        return True
    else:
        return False

szo = 'valami'
darab = 0
while szo !="end":
    szo = input('Szó:')
    if vizsgalAbetu(szo):
        darab += 1
        #darab = darab + 1

print('A betűs darab:',darab)
