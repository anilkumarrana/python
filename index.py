import math 
import numpy as np
import pandas as pd 
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

# crete array and do reshape 
# arr = np.array([45,57,99,98,34,56,78])
# reshpe = arr.reshape(2,3)
# print(reshpe)

# how to use zeros and ones in numpy

arr = np.zeros((3,4))
print(arr)

# create array with all values = 1
arr = np.ones((3,5))

print(arr)

# Create a array and do arange

arr = np.arange(1,20,3)
print(arr)

#create array ans do linspace 
arr = np.linspace(1,4,5)
print(arr)

# Array operations in numpy

arr = np.array([24,35,76,89,56])
print(arr + 10)
print(arr - 10)
print(arr * 2)
print(arr / 2)
print(arr ** 2)

# Methodmetical function in numpy

arr = np.array([23,45,67,89,56,34])
print("The sum of the array is ", np.sum(arr))
print("The mean of the array is", np.mean(arr))
# Mean is the average of the array 
# sum is the total of the array 

print("The standard deviation of the array is" , np.std(arr))
print("The variance of the array is " , np.var(arr))
# Low variance mean the data is close to the mean 
# High variance mean the data is far from the mean 

data = np.array([200,230,240,250,260,270])

print("The mean of the data is " , np.mean(data))


# Show the version of pandas 
print(pd.__version__)

df = pd.DataFrame({
    "Name": ["Anil" , "Sunaina" , "Dipanshu" ],
    "Age": [23,25.27,24]
})
print(df)