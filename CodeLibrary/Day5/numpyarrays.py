#A basic python file for figuring out the NumPy package
# NumPy is installed through pip in cmd: "pip install numpy"
# it then imported to the file: (the as statement works as it does in SQL)
import numpy as np

#some aspects of numpy need to imported seperately, like the random module
from numpy import random

#Basics
#-----------------------------------------------------------------------------------------------
#print NumpPy version
print('NumPy v' + np.__version__)

#NumPy makes Arrays :)
#1D
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print()

#2D
arr2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr2)
print()

#3D - remember XD arrays is simply an array of arrays. NumPy takes that literally.
arr3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]])
print(arr3)
print()

#Array Tools
#-----------------------------------------------------------------------------------------------

#check how many dimensions in array
print('arr3 has', arr3.ndim, 'Dimensions')

#Array with empty dimensions
arr4 = np.array([1, 2, 3, 4, 5], ndmin = 4)
print('arr4 has', arr4.ndim, 'Dimensions')
print()

#You can access elements in arrays exactly how you'd expect (called indexing)
print(arr1[0], arr2[0, 1], arr3[0, 0, 2])
#pick from end with negatives
print(arr1[-1], arr2[0, -2], arr3[0, 0, -3]) 
print()

#Create a 1D Array of 50 random ints between 0-100
arr5 = random.randint(100, size = (50))
print(arr5)





#https://numpy.org/doc/stable/
#https://www.w3schools.com/python/numpy_intro.asp
