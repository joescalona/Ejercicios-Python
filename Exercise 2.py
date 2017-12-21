
'''
Ask the user for a number. Depending on whether 
the number is even or odd, print out an appropriate 
message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a 
different message.

Ask the user for two numbers: one number to 
check (call it num) and one number to divide by 
(check). If check divides evenly into num, tell 
that to the user. If not, print a different 
appropriate message.
''' 

#-*-coding:utf8;-*-
num1=int(input('Introduce un numero \n')) 
num2=int(input('Ahora uno para dividir a '+str(num1)+'\n'))
if num1%2==0:
    print(str(num1)+ ' Es par')
    if num1%4==0:
        print('Y ademas es multiplo de 4')
else:
    print(str(num1)+ ' Es impar')
if num1%num2==0:
    print(str(num2)+' divide enteramente a '+str(num1))
else:
    print(str(num2)+' no divide enteramente a '+str(num1))