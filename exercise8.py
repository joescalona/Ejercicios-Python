#-*-coding:utf8;-*-

import random
import os

def limpia():
    os.system("clear")

print('***PIEDRA PAPEL O TIJERA***')
nom1=raw_input('ingresa el nombre del player 1 = ')
nom2=raw_input('ingresa el nombre del player 2 = ')

list_nomb=[nom1,nom2]
primerplayer=[random.choice(list_nomb)]
segundoplayer=[]

for i in list_nomb:
    if i not in primerplayer:
        segundoplayer.append(i)

pp=primerplayer[0]
sp=segundoplayer[0]

print( pp + ' comienza')
x=raw_input('piedra, papel o tijera = ') 
limpia()
print('Es turno de '+ sp)
y=raw_input('piedra, papel o tijera = ') 
limpia()

def final(w,z):
    if w==z:
        return('Empate')
    elif w == 'piedra':
        if z == 'papel':
            return(sp +' gana') 
        if z == 'tijera': 
            return(pp +' gana')
    elif w == 'papel': 
        if z == 'tijera':
            return(sp +' gana')
        if z == 'piedra':
            return(pp +' gana')
    elif w == 'tijera':
        if z == 'piedra': 
            return( sp +' gana')
        if z == 'papel':
            return(pp +' gana')
print(final(x,y))
  
