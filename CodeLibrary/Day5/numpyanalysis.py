import numpy as np
from numpy import random

#Welcome back to high school
#Generate a random array that is easy to analyse has a human
arr = random.randint(50, size = (10))
print(arr)

#NumPy has tools for finding the Mean and Median of an Array.
#mean - the average. All values added up and divided by the total amount of values.
print('Mean =', np.mean(arr))

#median - the 'middle' value. Despite the fact it does it itself, you should sort the array
# first
np.sort(arr)
print('Median =', np.median(arr))

#module SciPy has a method for finding the mode of an array.
#mode - the most repeated value

#Standard Deviation - how 'spread out' the numbers are (number density?)
#Note: Unlike density, a high deviation means numbers are further spread
print('Standard Deviation =', np.std(arr))

closeArr = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
#closeArr std = 1
print(np.std(closeArr))