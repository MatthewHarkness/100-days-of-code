
def incrementFunct(i):
    i += 1
    return i

def decrementFunct(i):
    i -= 1
    return i

def squared(i):
    i *= i
    return i

#def toPower

print('Today we will use an incrementFunction. It does not need a class to run.')

i = 0
print(i)

#i++
i = incrementFunct(i)
print(i)

#i++
i = incrementFunct(i)
print(i)

#i++
i = incrementFunct(i)
print(i)

#i--
i = decrementFunct(i)
print(i)

#i**?
i = squared(i)
print(i)

i = squared(i)
print(i)

i = squared(i)
print(i)

i = squared(256)
print(i)

#A function is simply a code block that you can refer back to anywhere in the file
#A function is different to a method, which work like how a method would in java and
#   requires a class