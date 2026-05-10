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

arr = np.array([1,2,3,4,5])
print (arr)