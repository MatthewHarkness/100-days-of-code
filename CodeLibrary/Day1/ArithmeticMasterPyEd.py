# Matthew Harkness
# Day 1 - #100DaysOfCode
# Task: ArithmeticMaster - Generate random Arithmetic for the user to complete!
# Project: ArithmeticMaster Py Edition
import random

#boolean isActive determines when to end loop
isActive = 1
operatorPicked = 0
print('Welcome to Arithmetic Master! Lets do some Arithmetic!')

#Default Values
ans = 0
userAns = 0

while isActive == 1:
    #Generate random ints for operands
    O1 = random.randrange(1, 100)
    O2 = random.randrange(1, 100)
    
    while operatorPicked == 0:
        operator = input('Which operator would you like you use (+, -, *, /): ')
        print()

        #Addition
        if operator == '+':
            ans = O1 + O2
            print(O1, '+', O2, end = '')
            operatorPicked = 1

        #Subtraction
        elif operator == '-':
            ans = O1 - O2
            print(O1, '-', O2, end = '')
            operatorPicked = 1

        #Multiplication
        elif operator == '*':
            ans = O1 * O2
            print(O1, '*', O2, end = '')
            operatorPicked = 1

        #TO-DO: Division
        elif operator == '/':
            #Check numbers can be divided evenly
            while O2 % O1 != 0:
                O2 = random.randrange(2, 150)
                O1 = random.randrange(2, 100)
                #print('O1 = ', O1, ', O2 = ', O2)
                if O1 == O2:
                    print('MATCH')
                    continue

            ans = O2 / O1
            print(O2, '/', O1, end = '')
            operatorPicked = 1
        else:
            print('You inputted an illegal operator. Whoopsie!')
    #End Inner Whhile
    
    userAns = input(' = ')
    
    #Right or wrong?
    if int(userAns) == ans:
        print(':D Correct Answer! Well Done!')
    else:
        print(':( That was wrong, keep tring. Correct Answer is', ans)
    
    #Try again?
    print()
    tryAgain = input('Do you want another question? (Y/N) ')
    if tryAgain == 'N' or tryAgain == 'n':
        isActive = 0
    else:
        operatorPicked = 0
#End Outer While

print('Thank you for using Arithmetic Master!')

#Note to self for later: Python GUI package is called Tkinter