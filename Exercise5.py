# -*- coding: UTF-8 -*-

import random 

#list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
#list3 = []
#list4 = []

#for i in list1:
#	if i in list3:
#		continue
#	if i in list2: 
#		list3.append(i)

#print('Los numeros repetidos son '+str(list(set(list3))))

# ------------------------------------------------------------ 

list1 = random.sample(range(100),5) #Escoger aleatoreamente 10 elementos entre 0 y 99 
#print('lista 1 = '+str(list1))
list2 = random.sample(range(100),99)
#print('lista 2 = '+str(list2))
list3 = []

for i in list1: 
	if i in list2: 
		if i not in list3:
			list3.append(i)

print ('Los numeros repetidos son = '+str(list(set(list3)))) 
