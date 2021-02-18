# Matthew Harkness
# Day 1 - #100DaysOfCode
# Task: ArithmeticMaster - Generate random Arithmetic for the user to complete!
# Project: ArithmeticMaster Py Edition
import random

#boolean isActive determines when to end loop
isActive = 1
operatorPicked = 0
print('Welcome to ArithmeticMaster! Lets do some Arithmetic!')

#Default Values
ans = 0
userAns = 0

while isActive == 1:
    #Generate random ints for operands
    operand1 = random.randrange(1, 100)
    operand2 = random.randrange(1, 100)
    
    while operatorPicked == 0:
        operator = input('Which operator would you like you use (+, -, *): ')
        print()

        #Addition
        if operator == '+':
            ans = operand1 + operand2
            print(operand1, '+', operand2, end = '')
            operatorPicked = 1
        #Subtraction
        elif operator == '-':
            ans = operand1 - operand2
            print(operand1, '-', operand2, end = '')
            operatorPicked = 1
        #Multiplication
        elif operator == '*':
            ans = operand1 * operand2
            print(operand1, '*', operand2, end = '')
            operatorPicked = 1
        #TO-DO: Division
        else:
            print('You inputted an illegal operator. Whoopsie!')
    
    userAns = input(' = ')
    
    #Right or wrong?
    if int(userAns) == ans:
        print(':D Correct Answer! Well Done!')
    else:
        print(':( That was wrong, keep tring. Correct Answer is', ans)
    
    #Try again?
    print()
    tryAgain = input('Do you want another question? (Y/N) ')
    if tryAgain == 'N' or 'n':
        isActive = 0
    else:
        operatorPicked = 0
    

print('Thank you for using Arithmetic Master!')