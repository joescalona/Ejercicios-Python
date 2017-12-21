#-*-coding:utf8;-*-
#qpy:3
#qpy:console
''' 
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that 
number. (If you don’t know what a divisor is, it is 
a number that divides evenly into another number
''' 

x=int(input('Ingresa un numero y te dare sus divisores = ' ))
#for i in range(1,x+1):
#    if x%i==0:
#        print(i)
rang_num = list(range(1,x+1))
list_divisores = [] 

for i in rang_num: 
    if x%i == 0:
        list_divisores.append(i)
print('Los divisores son ' + str(list_divisores))