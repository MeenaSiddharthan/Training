# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:57:42 2021
@author: m.siddharthan
"""
import numpy as np
import pandas as pd

##SCRIMBA PYTHON TUTORIAL
#hold [shift] + down arrow to highlight
#printing text
print("Hammerboi")
print("Why boys")

dates=8
print("Meena has went on " +dates+ " failed dates")
cute=2
x="Meena has went on "+dates+" failed dates with "+cute+" cute boys."
a='it\'s'
b="it's"
#""/'' - strings [treated as characters not numbers]
#1,2,3,... - integers
#1.24 - floats [integers with decimal points]
#Boolean - take on True or False values

print(type(True))
print(type('hi'))
print(type(1.24))
print(type(1))    

#to change integer to string
print('Meena went on '+str(dates)+' failed dates')

#setting as integer/float/string
a=int(1)
b=int(2.33)
c=int("3")
d=float("1")
e=float(20)
f=float(1.22)
g=str(0.01)
h=str(21)

#passes a string into a float then a integer - cannot do direct string with decimal to integer
i=int(float("2.11"))
print([a,b,c,d,e,f,g,h,i])

name='Hoola'
price=5.69
stock=10
is_in_inventory=True

#below doesn't work since '+' concatenates. So use ','
print(name+price+stock)
print(name,price,stock)

#Basic Arithmatics
a=10
b=3
print('Addition : ', a+b)
print('Subtraction : ', b-a)
print('Multiplication : ', a*b)
print('Division (float): ', a/b)
print('Division (floor): ', a//b)
#Modulus prints reminder after devision
print('Modulus : ', a%b)
print('Exponent : ', a**b)

#Strings
msg='racecar bois'
print(msg*2)
#to insert a space, use ',' in print
print(msg,msg)
#other prints
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
#to get length of string
print(len(msg))
#count the number of rs in string
print(msg.count('r'))
#slicing strings
#print the 5th letter
print(msg[5])
#print the third last letter
print(msg[-3])
#print from 2nd to 10th letter
print(msg[2:10])
#print from 2nd letter
print(msg[2:])

#Exercise
a='Welcome to Python 101: Strings'
print(a)
print((a[-10]+' '+a[0:7]+' '+a[-5:-1]+' '+a[8:10]+' Tyler').title())
b=a[-10]+' '+a[0:7]+' '+a[-5:-1]+' '+a[8:10]+' Tyler'
print(b.title())
#print txt backwards
print(b[::-1].title())

#Print in separate lines use triple quotes
msg="""Dear Boiz,
Y u do be like dat
Y u do me dirty
dawwwwggg"""
print(msg)
#find and replace
print(msg.replace('Boiz','Gucciboiz'))
#check if something exists in message
print('Python' in msg)
print('Boiz' in msg)

#Printing into existing statements
name='dolla'
sign='pounds'
msg=f'{name.title()} bills bills baby we talking {sign.upper()}'
print(msg)
#why rupish not working?
sign='rupiah'
print(msg)

#Capturing user input
name=input('What is your name? ')
print('Hello '+name+'!')
age=input('What is your age? ')
print('Hello '+name+' you be '+age+' years of useless')

#Building a calculator
num1=input('Enter a random number ')
num2=input('Enter another number ')
answer=(float(num1)-float(num2))
print(answer)

#User input exercise
name=input('What is your name? ')
distance=input('How far are u from me in km? ')
miles=float(distance)*0.621
print(f'Hello {name.title()}! You are {distance} km or {round(miles,1)} miles from me.')