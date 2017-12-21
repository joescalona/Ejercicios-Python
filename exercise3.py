#-*-coding:utf8;-*-
#qpy:3
#qpy:console

''' 
Take a list, say for example this one:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements 
of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

''' 
a=[1,1,2,3,5,8,13,21,34,55,88,]

num=int(input('Dame un numero \n'))
new_list=[]

for i in a:
    if i<num:
        new_list.append(i)

if len(new_list)==0:
    print('Lista vacia')
else:
    print(new_list)