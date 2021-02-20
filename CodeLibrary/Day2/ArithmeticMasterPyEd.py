# Matthew Harkness
# Day 1 - #100DaysOfCode
# Task: ArithmeticMaster - Generate random Arithmetic for the user to complete!
# Project: ArithmeticMaster Py Edition
import random

#boolean isActive determines when to end loop
isActive = True
operatorPicked = 0
print('Welcome to Arithmetic Master! Lets do some Arithmetic!')

#Default Values
ans = 0
userAns = 0

while isActive == True:
    #Generate random ints for operands (O1 and O2)
    O1 = random.randrange(2, 100)
    O2 = random.randrange(2, 100)
    
    while operatorPicked == False:
        operator = input('Which operator would you like you use? (+, -, *, /): ')
        print()

        #Addition
        if operator == '+':
            ans = O1 + O2
            print(O1, '+', O2, end = '')
            operatorPicked = True

        #Subtraction
        elif operator == '-':
            ans = O1 - O2
            print(O1, '-', O2, end = '')
            operatorPicked = True

        #Multiplication
        elif operator == '*':
            ans = O1 * O2
            print(O1, '*', O2, end = '')
            operatorPicked = True

        #Division
        elif operator == '/':
            #Check numbers can be divided evenly
            questionValid = False
            while not questionValid:
                if O2 % O1 != 0 or O1 == O2:
                    O2 = random.randrange(2, 150)
                    O1 = random.randrange(2, 100)
                    print('O1 = ', O1, ', O2 = ', O2)
                else:
                    questionValid = True

            ans = O2 / O1
            print(O2, '/', O1, end = '')
            operatorPicked = True
        else:
            print('You inputted an illegal operator. Whoopsie!')
    #End Inner Whhile
    
    userAns = input(' = ')
    
    #Right or wrong?
    if int(userAns) == ans:
        print(':D Correct Answer! Well Done!')
    else:
        print(':( That was wrong, keep tring. Correct Answer is', int(ans))
    
    #Try again?
    print()
    tryAgain = input('Do you want another question? (Y/N) ')
    if tryAgain == 'N' or tryAgain == 'n':
        isActive = False
    else:
        operatorPicked = False
#End Outer While

print('Thank you for using Arithmetic Master!')

#Note to self for later: Python GUI package is called Tkinter