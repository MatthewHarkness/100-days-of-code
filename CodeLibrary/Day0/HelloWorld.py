# Matthew Harkness
# Day 1 - #100DaysOfCode
# Task: What is python?
# Project: N/A
import random

#Print hello world
print('Hello World!')

#NOBODY TOLD ME PYTHON DOESN'T USE SEMICOLONS
#Python uses implicit variables.
int = 10
floatingPoint = 5.5

string = 'Hello World'
stringConcat = ', I love you!'
string = string + stringConcat

print ('4 + 6 = ', 4 + 6)


#for loop 0 - 5
#Note: as there are no brackets or semicolons, Python uses indentation to determine scope of code.
#   In other words, CODES MUST BE NEATS
for x in range(6):
    if x < 5:
        print(x, ', ', end = '')
    else:
        print(x)

#for loop 2 - 5
for x in range (2, 6):
    if x < 5:
        print(x, ', ', end = '')
    else:
        print(x)

#booleans
#Why use bool when int 0 & 1 work just as well?
x = 0
print(bool(x))
if bool(x) == 'false':
    print('Bool x is false!')
else:
    print('Bool x is true!')

#Generate random number between 1 and 100
#You must import the module 'random', this has been done at the top of the script
randNum1 = random.randrange(1, 100)
print('A random number', randNum1)

#user input
username = input('Please Enter Name: ')
print('Your name is', username, '!')
print()