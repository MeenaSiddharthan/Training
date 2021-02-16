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

#Dictionaries
#aren't ordered and can contain duplicate values
#key : value
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' :['John','Eric','Michael','George','Terry']
    }
print(movie)
print(movie['title'])
print(movie.get('budget'))

#update dictionary
movie['title'] = 'The Holy Grail'
#add a new key
movie['budget']=250000
print(movie['title'])
print(movie)

#Delete entries
year = movie.pop('year')
#or 
del movie['year']
print(movie)

#Number of keys in a dictionary
print(len(movie))

#Loop through dictionary
for key, value in movie.items():
    print(key, value)


python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here')
    
#Concat several dictionaries together
ppl={}
ppl1={}
ppl2={}

#updates
ppl.update(python)
print(ppl)

#comprehension
for groups in (python, holy_grail, life_of_brian) : ppl1.update(groups)
print(ppl1)

#Unpacking
ppl2={**python,**holy_grail,**life_of_brian}
print(ppl2)
print(sorted(ppl2))
print(sorted(ppl2.items()))
print('The sum of the ages: ', sum(ppl2.values()))

#Exercise
freelancers = {'name':'Freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

department_start = {**freelancers, **antiques, **pet_shop}
print(sorted(department_start.items()))
print('-----'+'\n')

cart = {}
wallet = 1000
for shop in (freelancers, antiques, pet_shop) :
        a = input(f'Welcome to {shop["name"]}! Here is what\'s available: {list(shop.items())} Type what you\'d like to purchase or type exit to move on: ')
        if a not in shop:
            print('\n'+f'You\'ve chosen not to purchase anything from the {shop["name"]}.')
        else:
            cart.update({a:shop.pop(a)})
            wallet = wallet - (cart[f'{a}'])
            print('\n'+f'You\'ve purchased {a} from {shop["name"]} and have ${wallet} remaining!')
        b = ", ".join(list(cart.keys()))
        c = sum(cart.values())
print('\n'+f'You have bought these items: {b}. You spent a total of ${c} and have ${wallet} remaining!')

department_end = {**freelancers, **antiques, **pet_shop}
print('\n'+'-----')
print(sorted(department_end.items()))

#Errors
#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed - runs regardless if there's error or not
try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num >30 or num < 1:
        raise ValueError(num)
except ValueError as err:
    print(err, "Bad Value input!")
except ZeroDivisionError as err:
    print(err, "You can't divide by zero!")
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")

##Classes and Objects
#Classes - are blueprints/abstract
#objects - actual things you build
#Variables - attributes
#function - method
class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
        #Create function within class
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        
#self - keyword refers to object we are creating + convention is to use self
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("Inception",2017,9.0,True)
film_2.nice_print()
#OR
movie.nice_print(film_2)
#To create database of films
films = [film_1,film_2]
print(films[1].title)

#Class Inheritance
#when you have a class that inherits something from another class
class Karens:
    def move(self):
        print('Karen takes 5 steps toward you!')
    def attack(self):
        print('Says she wants to speak to the manager! You are down 3 HP!')
class Male(Karens):
    def rejection(self):
        print('Says he didn\'t find you attractive anyway! You gain 3 HP!')
class Reasonable(Karens):
    def badguy(self):
        print('She has a point! Maybe you are the bad guy. You lose 10 HP!')
    def soft(self):
        print('Says you are just young and gives you candy. 23 y/o you takes it to gain 3HP!')
class Rich(Reasonable):
    def soft(self):
        print('Is being passive aggressive... but she called you darlin so you gain 3HP!')
        
character1 = Karens()
character1.move()
character1.attack()
character2=Male()
character2.move()
character2.rejection()
character3=Rich()
character3.move()
character3.badguy()
character3.soft()

#Modules
#When you write functions - package code in modules + in python can import module or packages to use
#import babyyyyy
import pandas as pd
#gives you list of fuctions in the package/module
print(dir(pd))
#to import multiple packages
import pandas, numpy
#to import just a couple fuctions from a package rather than the whole package
#then don't need to write pd.DataFrame - can just write DataFrame
from pandas import DataFrame as df

#Zip + Unzip command
num = list('69420')
letter = str('m o i s t').split(' ')
names = ['Kayden','Tyler','Christopher','Jay','Mikhail']
wow = zip(num,letter,names)
#to assign num to names
combo = list(zip(num,names))
print(combo)
#can make dict too
combo1 = dict(zip(num,letter))
print(combo1)
combo2 = list(zip(num,letter,names))
print(combo2)
#to unzip and make variables
a,b,c = zip(*combo2)

keys = str('this parrot is deceased').split()
values = str('denna papegojan är avliden').split(' ')
learn = dict(zip(keys,values))
print(learn)

#Lambda functions
#for normal functions need to return and print
def square(x):
    return x*x
print(square(3))
#name = lambda parameter(s): expression
#lambda- like a function *lite*
square1 = lambda x: x*x
print(square1(3))
double_mult = lambda x,y: x*y
print(double_mult(2,4))

#Function and a lambda function to get name and alias
def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()
name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
print(name_and_alias1('rOger fedEREr  ','teNnOS'))
print(name_and_alias('rOger fedEREr  ','teNnOS'))

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
#only sorts by first name
monty_python.sort()
#sort by last name
monty_python.sort(key = lambda names:names.split(' ')[-1])
print(monty_python)

#But why use lambda if you can use function?
#can put lambda in a function so a function returns a new function
def func(n):
    return lambda a: a*n
double = func(2)
print(double(3))

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)

print(walkin_cost(2))

#Lambda exercise
f = lambda a: a+5
print(f(2))

strip = lambda a: ''.join(a.split(' '))
strip('maybe baby im wonderwall')

list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
lists = lambda a,b: list(set(a+b))
print(lists(list_a,list_b))

def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c
f = create_quad_func(2,4,6)
print(f(2))

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
#write sorting by integer
signups.sort(key = lambda names: int(names[3: ]))
print(signups)

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

#Exercise: Sort this by score using lambda!
player_list.sorted(key = lambda playyer: playyer)

#Comprehensions 
#Creates lists, sets, tuples, dict with less code - anything that can be done with comprehensions, can do with for loops
numbers = [1,2,3,4,5,6,7,8,9]

new_list = []
for num in numbers:
    a = num**2
    new_list.append(a)
print(new_list)
#using comprehension
new_list = [num**2 for num in numbers]
print(new_list)

new_list1 = [num**2 for num in numbers if num%2 == 0] #% sign is like division but checks for remainder so if reminder is 0, number is even
print(new_list1)

new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)

# Dictionary comprehensions
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']
print(list(zip(movies, year)))
# give me a dict('movies': year) for each movies, year in zip(movies, year)
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict)
n1 =[(name,movie,yr) for name,movie,yr in zip(names,movies,year) if yr < 1981]
print(n1)

#Randomness
import random as rd
#pseudo radomness vs secure randomness
for i in range(5):
    print(rd.random())
    print(rd.uniform(1,6)) #geerates between 1 and 6
    print(rd.randint(1,6)) #generates integer between 1 and 6
    print(random.randrange(1,100,2)) #generates random between 1 and 100 with steps of 2 (e.g. 1,3,5)
    
#to shoose at random
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(rd.choice(friends_list))
#to choose random sample - each case drawn only once
print(rd.sample(friends_list,3)) #creates sample of 3

#Timeit and performance of code
#to test which code runs faster import timeit
import timeit as tt

#codes to find prime numbers within a certain range
print([x for x in range(2,150) if not ([x%y == 0 for y in range(2,150)])])
#why can't I change x to 150 for y range? and why do i need "any" in front?

def test1():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
def test2():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(1)

print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))

#Project Crypto machine
# create keys string
# autogenerate the values string by offsetting original string
# create two dictionaries
#user input 'the message' and mode
# run encode or decode
# return result
# clean and beautify the code 

def crypto():
    a = input('Enter sentence to be decrypted/encrypted: ').lower().split(' ')
    b = input('Enter decrypt or crypt mode: ').lower()
    new_lang = ['chat','et','chaud', 'tres', 'comme', 'ton', 'mamau']
    eng = ['cat','is','fat', 'very', 'like', 'your', 'mom']
    decrypt = dict(zip(new_lang,eng))
    crypt = dict(zip(eng,new_lang))
    translate = []
    try:
        if b == 'crypt':
            for word in a:
                translate.append(crypt[word])
                continue
        elif b == 'decrypt':
            for word in a:
                translate.append(decrypt[word])
                continue
        elif b != 'crypt' or 'decrypt':
            print('You have entered an incorrect mode!')
    except KeyError as err:
        print(err, "is not recognized!")
    c = ' '.join(translate)
    return(print('Here is your message: '+c.title()))
    
def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
# OR create 1 and then flip 
    #dict_e = dict(zip(keys,values))
    #dict_d = {value:key for key, value in dict_e.items()}
#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()
print(enigma_light())

#Math tutor project
#ask how many questiona want to answer
#show multiplication table and ask for input
#at the end state number of correct answers/greetings/% correct
#total time taken and time taken per question
#show all questions with answers
import random as rd
import time

answer_list = []
def calculations():
    number = int(input('How many equations do you want to solve?: '))
    limits = int(input('What\'s the highest number you want to solve?: '))
    d=0
    e=0
    while number > 0:
        a,b = rd.randint(1,limits), rd.randint(1,limits)
        c = a*b
        start = time.time()
        answer = int(input(f'What is {a} x {b}?: '))
        end = time.time()
        if answer == c:
            d+=1
            answer_list.append(f'Q: {a} x {b} A: {c} Your A: {answer}')
            print(f'That is correct! That took you {round(float(end - start),2)} seconds!')
            print(f'You have {number-1} equations left.')
        elif answer != c:
            e+=1
            answer_list.append(f'Q: {a} x {b} A: {c} Your A: {answer}')
            print(f'That is correct! That took you {round(float(end - start),2)} seconds!')
            print(f'You have {number-1} equations left.')
        number-=1
    print('\n')
    for answer in answer_list:
        print(answer)
    return(print(f'\nThank you for playing! You were {round((d/(e+d)*100),1)}% correct.\nYou got {d} question(s) right and {e} question(s) wrong.'))
    
#Answer
from  random import randrange as r 
from time import time as t
def sol1():
    no_questions = int(input('How many questions do you want?: '))
    max_num =int(input('Highest number used in practice?: '))
    score = 0
    answer_list = []
    start = t()
    for q in range(no_questions):
        num1,num2 = r(1,max_num+1),r(1,max_num+1)
        ans = num1 * num2
        u_ans =int(input(f'{num1} X {num2} = '))
        answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
        if u_ans == ans:
            score += 1
        end = t()
    return(print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_questions,1)}seconds/question)'))

for a in answer_list:
    print(a)
    
#Marble trading game
#draw marble from bag at random
#if green - win, if red - lose
#before draw decide how much you want to bet
#number of rounds/draws must be random
#game over if you lose half money
import random as rd
wallet = 1000
marbles = ['green','green','green','green','green','green','red','red','red','red']
drawn = []

i = rd.randint(1,10)
while i > 0:
    if wallet > 500:
        bet = int(input('How much would you like to bet?: '))
        a = rd.choice(marbles)
        drawn.append(a)
        if a == 'red':
            wallet-=bet
            print(f'Damn! You drew a {a} marble, so you lose! You have ${wallet} left.\nThere are {i-1} rounds left.')
        elif a == 'green':
            wallet+=bet
            print(f'You drew a {a} marble, so you win! You have ${wallet} left.\nThere are {i-1} rounds left.')
    else:
        print('Sorry, you do not have enough money to continue!')
    i-=1
print(f'\nYou drew marbles in this order: {", ".join(drawn)}. You have ${wallet} left.')