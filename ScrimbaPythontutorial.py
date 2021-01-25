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
print(f'Meena has went on {dates} failed dates')
cute=2
print(f'Meena has went on {dates} failed dates with {cute} cute boys.')
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

#below doesn't work since '+' concatenates string. So use ','
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
print(f'Hello {name} you be {age} years of useless')

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

#List
friends=['Mary','Jord','Freja','Pyotr']
print(friends)
print(friends[1],friends[3])
print(len(friends))
#find what position an item is at
print(friends.index('Pyotr'))
#count number of instances something is in list
print(friends.count('Jord'))
#lists can contain int/str/bool mixture
#to sort list
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
#min max sum of lists
cars=[911,123,567,393,378,605]
print(max(cars))
print(min(cars))
print(sum(cars))
#add to list
friends.append('Jase')
friends.insert(2,'Lola')
#Below changes an existing value in list
friends[3]='Bin'
#extend list - put two lists together
friends.extend(cars)
print(friends)
#remove from list
friends.remove('Freja')
friends.pop(-1)
print(friends)
#deletes within list
del friends[2]
#to duplicate/copy list
new_friends=friends[:]
new_friends=list(friends)
new_friends=friends.copy()
print(new_friends)

#Exercise
sale_w1=[7,3,42,19,15,35,9]
sale_w2=[12,4,26,10,7,28]
day7=input('How many lemonades did you sell on 7th day of week 2? ')
sale_w2.append(int(day7))
print(sale_w2)
sale_w1.extend(sale_w2)
sales=[i*1.5 for i in sale_w1]
print(sales)
print(max(sales))
print(min(sales))
print(sum(sales))

#using numpy
sale_w1=np.array([7,3,42,19,15,35,9])
sale_w2=np.array([12,4,26,10,7,28])
day7=input('Week 2 7th day sales? ')
np.append(sale_w2,day7)
sales=np.append(sale_w1,sale_w2)
sales=sales*1.5
print(sales)
np.min(sales)
np.max(sales)
np.sum(sales)

#Using split to change message to list
msg='Welcome to Python 101: Split and Join'
print(msg.split())
print(msg.split(' '))
#Make list into string
friend_list=['John','Eric','Mike','Toto','Abel']
print('-'.join(friend_list))

#Exercise
csv='Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(csv)
csv=csv.replace(',',' ').replace(':',' ').replace(';',' ').split(' ')
friends_list=csv
print(friends_list)

#Tuples-faster lists that you can't change
friend_list=['John','Eric','Mike','Toto','Abel']
friends_tuple=('John','Eric','Mike','Toto','Abel')
print(friend_list)
print(friends_tuple)
#can use tuple to ensure no changes to list/data when running script

#Sets - use curly brackets to make sets
#Set is unordered and removes duplicates inside + sets are faster at finding members
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends_set)
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
#prints common in sets
print(friends_set.intersection(my_friends_set))
#give all elements with no duplicates
print(friends_set.union(my_friends_set))
#cannot create set using just curly brackets must be x=set()

#Exercise
friends = {'John','Michael','Terry','Eric','Graham'}
if 'Eric' in friends:
    print('True')
else: 
    print('False')
if 'Eric' and 'Terry' in friends:
    print('True')
else:
    print('False')
#Or simply
print('Eric' and 'Terry' in friends)
my_friends = {'Reg','Loretta','Colin','John','Graham'}
all_friends=friends.union(my_friends)
all_friends=(friends | my_friends)
print(all_friends)
#Get only common names
common_friends=friends.intersection(my_friends)
common_friends=(friends & my_friends)
print(common_friends)

# Functions
#always decalre function before using it
def greet(x,y):
    print(f"Hello {x}, you are {y}!")
          
greet("brian","21")

#to set default age greet(x,y=28)
x=input("Enter your name: ")
y=input("Enter your age: ")
greet(x,y)

#Exercise
def greeting(name, age=28, color="red"):
    print(f'Hello {name.title()}, you will be {age+1} next year')
    print(f'We hear you like the color {color.lower()}!')
    
color=input("Enter your favorite color: ")
greeting("Nat",color=color,age=22)

#Return
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount *1.25
    return f"{amount},{tax},{total_amount}"
# OR return [amount, tax, total_amount] to get list
# OR return amount, tax, total_amount to get tuple

print(value_added_tax(111))

#Comparisons
a=7
b=3
# check if a=b
print(a==b)
# check if a is not b
print(a!=b)
# check if a lesser than b
print(a>b)
print(a>=b)
# check if something is in something
print('o' in 'bay')
#check if something is not in something
print('o' not in 'boy')
a=3
#check if a is b
print(a is b)
#Bool - true is 1 and false is 0
print(bool(5))
#all empty values becomes false

#If else code
is_raining=False
is_cold=True
if is_raining and is_cold:
    print("Bring an umbrella + jacket")
elif is_raining and not(is_cold):
    print("Bring umbrealla")
elif is_cold and not(is_raining):
    print("Bring jacket")
else:
    print("Umbrella no need")

#Exercise
equation=input("What sum would you like to solve? ")

if "+" in equation:
    print