# -*- coding: UTF-8 -*-

w = raw_input('Ingresa una palabra = ') 
w_list = list(w[:]) # palabra como lista 
n_w = list(w[::-1]) # palabra al reves 

#print w_list
#print n_w

if w_list == n_w:
	print(str(w)+' es palindroma')
else: 
	print(str(w)+' no es palindroma')

