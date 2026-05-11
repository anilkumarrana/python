import math 
import numpy as np

# Write a program to add two number 
num1 = 12
num2 = 23
num3 = num1+num2
print ("The sum of " , num1 ,"and" , num2 , "is" , num3)

# Write a program to input of a square and find the area of the square

side = 5
area = side * side
print  ("The area of the square with side " , side , "is ", area)


#Write the program to input floating point number and print their average
num1 = 12.5
num2 = 3.5

average = (num1 + num2) / 2
print ("The average of " , num1 , "and" , num2 , "is" , average)

#stirng functions

str1 = "My name is Anil . I am a software developer"

print (str1.upper())
print (str1.lower())
print (str1.title())
print (str1.split())
print (str1.replace("Anil", "Suaina"))
print (str1.find("developer"))

print(np.__version__)
print(math.sqrt(16))

arr = np.array([1,2,3,3,4,5])
print(arr)

# what is the mean of the array and numpy 
# Numoy fast calcution 
# working with array 
# numpy is a library for working with arrays and matrices in python. 
# It provides a powerful set of tools for peforming mathematical operations on arrays.
# Write the method to find the mean of the array using numpy 

mean = np.mean(arr)
print ("The mean of the array is ", mean)

# How to print array by using numpy 
arr = np.array([35,56,87,90])
print(arr)

# create array with all values = 0 

arr = np.zeros((2,3))
print(arr)

# create array with all values = 1
arr = np.ones((2,2))
print(arr)

# create array and do reshep 

arr = np.array([45,76,98,67,56,45,])
reshped_arr = arr.reshape(2,3)
print(reshped_arr)

# create array and do reshape
arr = np.array([46,76,89,89,98,89])
reshpes = arr.reshape(3,2)
print(reshpes)