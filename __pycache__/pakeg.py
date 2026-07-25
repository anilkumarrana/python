import numpy as np
# Here we will learn library of python and how we can use
# 01 Numpy
# 02 Pandas
# 03 Scipy
# 04 Scikit-lear


# 01  Numpy :- Numpy is a general-processing packege. It provides a high performance multidemesional 
# array object, and tools for working with these array, It is fundamental packege for sentific computing with python.

# What is Array :- Array is data structure that stores value of same data type , 
# in python this is main  different between array and list,While python lists can 
# contain  values corresponding to different data type, and  array in python can only 
# contain values corresponding to same type.

# Numpy array are stored at one continous place in memory unlike list, So processes can acces and manipulate.

arr = np.array([34,56,78,98,67,56])
print(arr)

# checking the verison for numpy 

print(np.__version__)

# Numpy is used to work with arrays. The array in  numpy is called ndarray.
# we can create a  Numpy ndarray object by using array() function.

arr = np.array([24,57,78,98,35,90])
print(arr)
print(type(arr))

#type() :- This build python function tells us the type of the object passed to it, Like in above code it shows that arr is numpy.ndarray type.

# To create an ndarray , We can pass s list, tuple or any array like object into the array array () method, It will convert into an ndarray.

arr = np.array((33,55,77,99,100))
print(arr)
print(type(arr))

# Dimensions in array

# A dimension in  array is one level of array depth(nested arrays).
# Nested array are array that have arrays as their elements 

# Array :- Array is data structure that can store same data type,
# There type of srray 
# 0 - D Array 
# 1 - D Array 
# 2 - D Array 
# 3 - D Array 

# 1 - D Array 

# An array that has 0 - D array its elements is called uni-dimensional or 1 - D array.
# There are the most common and basic arrays

arr = np.array([54,67,98,67,45,34])

print(arr)

# An Array that 1 - D array as its elements is called a  2 -D array.
# These are often used to represent matrix or 2nd order tensors.

# Numpy has a whole sub module dedicated towards matrix operations called numpy.mat

# create 2-D Array containing two arrays with the value 1,2,3 and  4,5,6

arr = np.array([[1,2,3] , [4,5,6]])

print(arr)
print(type(arr))

# 3-D An array has 2-D array (matrices) as its elements is called 3-D array.

# These are often used to represents a 3rd order tensor.

arr = np.array([[34,67,98],[78,98,67],[56,34,12]])

print(arr)
print(type(arr))

# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
b = np.array([1,2,3])
c = np.array([[34,56,89] , [13,45,89] , [24,89,90]])
d = np.array([[[45,67,12,14,15], [45,78,90,54]],[[56,78,23,45],[56,78,34,23]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Array
# An Array can have any number of dimensions

# When the array is created , You can define the number of dimensions by using the ndmin argument.

# create an array with 5 dimension and verify that it has 5 dimension.

arr = np.array([1,2,3,4] , ndmin=5)
print(arr)
print('Number of dimension :', arr.ndim )
