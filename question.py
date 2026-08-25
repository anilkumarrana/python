
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


# Set in python is a collection of unique elements. It is unordered and unindexed. It is used to sstore multiple 
# values in a single variable. It is defined by using curly braces {} 
# or by using the set() function.

set_var = {45,23,89,67,45,10,18}
print (set_var)
print (type(set_var))
set_var

# Notes :- Set items are unoredered, Unchangeable but You can remove items and add new items.
# A set is a collection which is unordered, unchangeable, and unidexed. 

# set items are unoredered, Unchangable and  do not allow duplicate values.

# unordered :- Unordered means that the items in a set do not have a defined order.
# Unchnageable :- Unchangeble means that the items in a set cannot be changed.
# Once a set is created, You cannot change its items, but You can remove itema and add new items.

# Duplcicate values :- Duplicate values are not allowed in a set. If You try to add a duplicate value, It will be ingored.

thinkset = {"Anil" , "Sunaina" , "Dipanshu" , "Anil"}
print (thinkset)

# Hare Anil are duplicate values in the set. The duplicate values are ignored and only unique values are stored in the set.

# Accessing items in a set :- You cannot access items in a set by index. 
# You can acess items in a set by using a for loop or by using the in keyword.

# But you can loop through the set items by using a for loop, or you can check if a specified value is present in a set, by using the in keyword.

# Example 

thinkset = {"buchu" , "Anil" , "Sunaina" , "Dipanshu"}

for y in thinkset:
    print (y)


# check if "Anil" is present in the set.

thinkset = {"Buchu" , "Anil","anil" , "Sunaina" , "Dipanshu"}

if "Buchu" in thinkset:
    print ("Yes Buchu is present in the set")
else:
    print ("No Buchu is not present in the set")


# Not in :- The not in keyword is used to check if a specified value is not present in a set.

thinkset = {"Buchu" , "Anil", "Sunil" , "Sunaina" , "Dipanshu"}

if "Anil" not in thinkset:
    print ("Yes Sunil is not present in the set")
else:
    print ("No Sunil is present in the set")


# Add itms in a set :- You cannot change the items in a set, but You can add new items to a set. 
# you can add items to a set by using the add () method.

thinkset = {"Buchu" , "Anil" , "Sunil" , "Sunaina" , "Dipanshu"}
thinkset.add("Shivani")
print (thinkset)

# Update set :- You can add items from another set into the current set by using the update() method.
 
thinkset = {"Buchu" , "Sunaina" , "Sunil" , "Anil"}
thinkset02 = {"Pawan" , "prakash" , "Manoj"}

thinkset.update(thinkset02)
print(thinkset)


# Remove items :-  To remove items in a set by using remove() key and discard() method. 

# Remove the item 

thinkset = {"Anil" , "Sunaina" , "Buchu" , "Sunil"}

thinkset.remove("Sunaina")

print(thinkset) 

# Note :- If remove the items by using remove() keyword and the items does not exist , remove will raise the error.
# Like 

# It is showing error but you are using discard they will be not showing error.

thinkset = {"Anil" , "Sunaina" , "Sunil" , "Dipanshu" }

thinkset.discard("Shimran")

print(thinkset)

# You can also remove the the item by using pop() method , But this method will remove random item, So you cannot be sure what item that gets removed.

thinkset = {"Anil" , "Sunaina" , "Sunil" , "Buchu"}
x = thinkset.pop()
print(x)
print(thinkset)

# Note :- Sets are unordred , So when using the pop () method, You do not which item that gets removed.


# Array in python 

# one diameantion 
# Two diamenation 

# operator in python 

# operator is a symbol that is used to perform operations on variables and values.
# There are many types of operators in python like arithmetic operator, assignment operator, comparison operator, logical operator, identity operator, membership operator.

# Arithmetic operator :- Arithmetic operator is used to perform mathematical operations like addition, subtraction, multiplication, division, modulus, exponentiation and floor division.
 
x = 10
y = 5

z = y + x
a = y - x
print("The sum of x and y is:" , z)
print("The Subtraction of x and y is:" , a)
print("The multiplication of x and y is:" , x*y)
print("The modulus of x and y is:" , x%y)
print("The exponentiation of x and y is:" , x**y)
print("The floor division of x and y is:" , x//y)

# Assignment operator :- Assignment operator is used to assign values to variables. The assignment operator is represented by the equal sign (=). 

# Write a code for assignment operator in python.

days = str(input("Enter the name of days:"))

if days == "Sunday":
    print("It's party night")
else:
    print("It's not party night")

    

# logical opertors 
# There are three type of logical opertors 
# 01 And :- returns ture value if both condition will be ture.
# 02 or :- returns ture valuse if one statements will be ture.
# 03 not :- reverse the result 


# Write a Python program to check if a number is greater than 10 and less than 50 using and .

num = 14 

if num > 10 and num < 50:
    print("The number is greather")
else:
    print("The number is not greather")

# Write a program to check whether a person is eligible for vote.
# condition :- Age must be 18 or above.

age = int(input("Enter the age: "))

if age > 18:
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote.")

# Write the program to check whether a number is divisible by both 3 and 5

num = int(input("Enter the number"))

if num % 3 == 0 and num % 5 ==0 :
    print("The number is divisible by 3 and 5" , num)
else:
    print("The number is not divisible by 3 and 5" , num)


# Write the program whether a student has passed or not ?
# condition :- marks must be 40 or above in both subject.

sub01 = int(input("Enter Maths subject marks"))
sub02 = int(input("Enter Hindi subject marks"))

total = sub01 + sub02 

if total > 40 and total > 100 :
    print("The student has passed! Happy ")
else:
    print("The student has not passed ! Sad")




# List :- List are used for store multiple data in a sigle variable.
# List is changeable and allow duplicate value. 


# List are one of 4 build in data type in python used to store collection of data, The other 3 are Tuple, set and dictionnary.

# List are creatind using the square brackets.


cars = ["Ranult","Nissan", "Toyota", "Maruti" ]

print(cars)


# list itema are ordered , changeable and allow duplicate values.

# List item are indexed, the first item had index[0] , the second item has index[1] etc .

# when we say that lists are ordered , it means that the item have a defind order, and that order will not change.

# Allow duplicate value 

name = ["Anil", "suniana" ,"Sunil", "Sunaina", "Anil", "Buchu", "Sunaina"]

print(name)
print(type(name))




# Function :- Function is a block of code which only runs when it is called.
# Function can return data as a result.
# in python a function defind using def keyword , following by a function and paranthese.

def my_Function():
    print("Welcome to python function")

my_Function()


def greet():
    print("Hello, function!")

greet()


def get_greeting():
    return("Hello from a function")

message = get_greeting()
print(message)

# Function can send data back to the code that called them using the return statement.
# When the function reaches a retur  statement , it stop executing and send the result back.



# You can use return directly.

# Using the return value directly 

def get_value():
    return("return using directly")

print(get_value())



# Write a program that takes a number from the user and checks whether it is even and odd.

num = int(input("Enter the number:"))

if num % 2 == 0:
    print ("The number is even" , num)

else:
    print("The number is odd" , num)

# Write the program that takes three numbers and find largest number.

num1 = int(input("Enter the number one"))

num2 = int(input("Enter the number two "))

num3 = int(input("Enter the number three "))

if num1 > num2 :
    print("The number one are greather then number two")
elif num2 > num3:
    print("The number two are greather then numbre three")

else:
    print("The number three greather then both one and two")


# write a program that takes a string and count how many vewels (a,e,i,o,u) it contains.
# Enter text 

text = str(input("Enter the text "))

velwo = "aeiou"
count = 0

for char in text.lower():
    if char in velwo:
        count +=1 


print("Number of vowels:",count)


# Write the program that takes a string and count how many vewels consonants it contains.

text01 = str(input("Enter the text and word !"))

velwels = "aeiou"
count = 0

for char in text01.lower():
    if char.isalnum() and char not in velwels:
        count +=1 

print("Number of consonants" , count)



# Funcation :- If a function does not return statment, It return None by defalut.

# Argumrnt :- Informtion can be passed into as argument.

# Argument are specified after the function name, Inside the parenthese. You can add as many argument as you want, Just saparate them with comma. 

# Call by function 
def my_Fun(name):
    print("Your name is ", name )

my_Fun("Anil")


def details(a,b):
    c = a + b 
    print ("The sum of two number", c)

details(20,30)


# call by variabe 

def  my_details(name = "Anil" , age = 23 ):
    print ("This is my details", name , age)

my_details()


# Parametera vs argument 

# The terms parameter and argument can be used for same thing: Information that are passed into a funcction.

# A Parameter is the variable listed inside the parethese in the function definition.
# A Argument is the actual value the is sent to the function when it is called.


def my_fun(name): # This is parameter 
    print ("Your name is " , name)

my_Fun("suniana") # This is argument.


# Positional argument :- When you call a function with argument without using keyword are called positional argument.

def my_fun(name, collge):
    print("My name is", name)
    print("I have complete B.tech from ", collge)


my_fun("Anil" , "SIT Jaipur")


# can a funcction return the multiple value 
# yes 


def cal(a ,b):
    return a + b , a - b

x, y = cal(23,34)

print(x)
print(y)


# Local variable:- The local variable is defind the inside of the function

def my_fun():

    a = 10
    print(a)

my_fun()

# global variable :- The global variable is defind the outside of the funaction.

a = 20 

def test():
    print(a)

test()


# write a program to take two number and print their sum.
# input 10 , 20
# output = 30

def my_fun(a,b):
     
     c = a + b

     print("The sum of two number" , c)

my_fun(10 ,20)

# write a program that take a number and returns whether it is even and odd.

def my_fun():

    a = 7 

    if a % 2 == 0:
        print("The number is odd" , a)
    else:
        print("The number is even" , a)

my_fun()


# write a  program and take number by the user and check given number is even and  odd.

def my_fun():
    num = int(input("Enter the number"))

    if num % 2 == 0:
        print("The given number is even" , num)

    else:
        print("The given number is odd" , num)

my_fun()


# write a function that take two number and return the larger number.
# Input = 15,25
# output = 25

def my_fun(a , b):

    if a > b:
        print("B is the greather then to A" , a)
    else:
        print("A is the greather then to B" , b)

my_fun(15 , 25)



# Write the function and print the given number of square.

def my_fun():

    num = int(input("Enter The number"))

    num2 = num * num 

    print("The square of" , num2)

my_fun()


