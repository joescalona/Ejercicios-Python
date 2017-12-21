# -*- coding: UTF-8 -*-

# PROBLEMA: ESCRIBIR UN PROGRAMA QUE RECIBA NOMBRE Y EDAD Y DECIR
# EN QUÉ AÑO EL USUARIO CUMPLIRÁ 100 AÑOS

Nom=raw_input('Hola, cual es tu nombre? \n')
print('Hola '+Nom+' !')
x=int(input('Que edad tienes?'))
y=int(input('En que año estamos?')) #y=año actual 
print('Entonces en el año '+str((100-x)+y)+' cumpliras 100 años')


