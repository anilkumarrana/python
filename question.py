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

