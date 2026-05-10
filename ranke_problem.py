import math
import os
import random
import re
import sys

n = 3
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print ("Not Weird")



# Given  the array of integers sum and interger target , return  incices od the two number 
num = [2 , 7 , 11 , 15]
print(len(num))
print([0,1])
sum = num[0] + num[1]
print (sum)

# Write the program to reverse a string 
str = "AnilSunaina"
new = str
print(new)
print(str[::-1])

# Write the program to find the factorial of a number
num = 2
factorial = 1
if num <0:
    print ("The factorial does not exist for negative number")
elif num == 0:
    print ("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial * i
        print ("The factorial of" , num , "is" , factorial)



# Write the program to find thne largest number in the list
num = [1,2,100,4,5]
largest = max(num)
print ("The largest number in the list is" , largest)

