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

#if elif statements
mode = input("Enter what you'd like to do (+,-,*,/): ")
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
             
if mode == '+':
    print(f'Answer: {num1+num2}')
elif mode == '-':
    print(f'Anser: {num1-num2}')
elif mode == '*':
    print(f'Answer: {num1*num2}')
elif mode == '/':
    print(f'Answer: {num1/num2}')
else:
    print('Input Error :(')

#Conditionals
#sets for in run way faster than tuple or list
def num_days(month):
    if month.lower() in {'jan','mar','may','jul','aug','oct','dec'}:
        days=31
    elif month.lower() == 'feb':
        days=28
    else:
        days=30
        print(f'Number of days in {month} is {days} days')

month=input('What month is it?: ')
num_days(month)

#Loops
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#Main structure:
    # while condition:
    #     code
    #     iterator
i=0
while i < 5:
    i+=1 #adds 1 to i
    print(f"*"*i + "Loops are awesome" + "*"*i)

#Excercise while loops
i=0
while i<10:
    num1=int(input('Guess a number between 1-100: '))
    num1
    if num1 == 25:
        print('You Win! That is correct!')
        i+=12
    elif num1 <= 25:
        print(f'Your guess is too small. You have {9-i} attempts left')
    elif num1 >= 25:
        print(f'Your guess is too big. You have {9-i} attempts left')
    i+=1
    
#Break or continue loops:
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue
    print(friend)
print("For Loop done!")    

#exercise for loops
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
more=input('Who else do you want to invite? Please seperate names by a comma: ').split(',')
names.extend(more)

for name in names: 
    print(f'{name.title()}! You are invited to the party!')
    continue

for name1 in names1:
    print(f'{name1.title()}! You are invited to the party!')
    continue

#Enumerate
#can be used to index 
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for num, friend in enumerate(friends,51): #to enumerate from a starting number
    print(num,friend)

for friend in enumerate(enumerate(friends,51),-100): #makes a tuple inside a tuple
    print(friend)  
    
#Sorted function
my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_llist, key = lambda item :item[2])) #lambda - function inside a function

#sorted - returns a new sorted list vs sort - changes existing list
#dictionaries
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print(movie['cast'])
print(movie.get('budget'))
movie['title'] = 'The Holy Grail'
print(movie.get('title'))
movie.update({'title' : 'The Holy Grail','year':1975})
movie['budget'] = 250000
print(movie)
year = movie.pop('year') #removes year from dictionary and saves as new variable
