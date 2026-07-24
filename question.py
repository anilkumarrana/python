# Write the program print "Hello world"
print("Hello, World")

# Ask user for thire name and age , then print a greeting 
name = "Anil"
age = 23 

print ("Hii, Your name is " , name , "and your age is " , age ,"You are from Jharkhand.")

# Create a calculator that takes two number and an operator(+,-,*,%)
a = 20
b = 30
c = a+b
print ("Tha sum value of a and b" , c)

# level two question 
# write a program that check if a number is odd and even 
a = 15
if a % 2==0:
    print("The number is even")
else:
    print("The number is odd")


# write the program that check the number is greather and not 

a = 20 
b = 30
if a >= b:
    print("The greather number is a")
else:
    print("The greather number is b")

# write the program that check tha prim number

num = 10

if num % 2 ==0 :
    print("The number is prime numner")
else:
    print("The number is not prime number")


# condition statement 
# The condition statement is used to check the condition and execute the code accoding to the condition.
# if statement is used to check thne condtion and execute the code if the condtioo is true.
# like
# if condition :
 
# write a program that check the number is positive and negative and zero 

num = int (input("Enter the number:"))

if num > 0:
    print ("The number is positive")
elif num == 0:
    print ("The number is zero")
else:
    print ("The number is negative")
    
# write a program that check the number is divisible by 5 and 11

num =  int (input ("Enter the number "))
if num % 5 == 0 and  num % 11 == 0 :
    print ("The number is divisible by 5 and 11")
else:
    print ("The number is not divisible by 5 and 11")




list = ["Anil", "Ravi" , "sunaina choudhary"]

print (type(list))
print (len(list))

# indexing in list is defined as the position of the element in the list. The index starts from 0.

# Append the element in the list 

list01 = ["Anil" ,"suniana" ]
list01.append("Buchu")
print (list01)
print (list01.append(["Sonika"]))
list01.append("Sonika")

print (list01)
# count the element in  the list 
lst = [45,65,989,56,98,90]
print (lst.count(2))


# Boolean and list 

# Bolean is a data type that can have two value: True or false. It is used to represent the true or false value. 
# It is used in conditional statement to check the condition and execute the code according to thne condition.

# print a message weather the condition is true or false.

a = 10
b = 5

if a < b:
    print ("The condition is true")
else:
    print ("The condition is false")


# Evalute value and variable in python 

print (bool("Anil"))
print (bool(15))
print (type(15))