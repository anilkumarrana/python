# write the a program that print the hello world 
print("Hello, welcome to python programming ")

# write a program that ask user for their name amd age then print a greeting 
name  = "Anil"
age = 23 
print ("Hii, your name is ",name , "and your age is ",age ,"You are from jharjhand ")

# create a calculator that takes two number and an  operator (+,-,*,%)
a = 20
b = 30
c = a+b
print ("The sum value of a and b is ",c)
d = a-b
print ("The substraction value of a and b is ",d)
e = a*b
print ("The multiplicationl value of a and b is ",e)
f = a/b
print ("The division value of a and b is ",f)
g = a%b
print ("The modulus value of a and b is ",g)

# level two question 

# write a program that check if a number is odd and even
a = 15
if a % 2 == 0:
    print("The number is even")
else:
    print ("The number is odd")

# write a program that check the number is greater and not
a= 20
b= 30
if a>= b:
    print ("The greater number is a")
else:
    print ("The greater number is b")

# write a program that check the prime number 
num = 15
if num % 2 == 0:
    print("The number is prime number ")
else :
    print ("The number is not prime number")

# write a program that check the number is positive and negative and zero
num = int(input("Enter the number"))
if num >0 :
    print ("The number is positive")
elif num == 0 :
    print ("The number is zero")
else :
    print ("The number is negative")


# write a program that check the largest number gives value by the user 
num = int(input("Enter the first number: "))
num02 = int(input("Enter the second number:"))
if num > num02:
    print ("The first numnber is largest number")
else :
    print("The second number is largest number")


# What is the output 
x = "10"
b = 5
print(x + str(b))

# String :- A string is a sequence of characters enclosed in single quotes ("") or double quotes ('). it is used to represention textual data in python. syring can contain letters, number, and special characyers. 

# print  a srting 
# write the program that print the srting 
print("Hello, welcome to python programming")

# write a program find the length of string 
str = "Hello , Welcome to python programming"
print(len(str))
print(str[2])

# write a program that check the string is palindreome or not 
str = "madam"
if str == str[::-1]:
    print("The string is polindrome ")
else:
    print("The string is not polindrome")

# String mathods
# There are many string methods available in python that can be used to manipulate and work with string data.
# 1. upper() :- This method converts all character in a string to uppercase.
str = "hello , welcome to python programmmimg"
print (str.upper())

# 2. lower() :- This method converts all characters in a string to lowercase.

str = "HELLO , WELCOME TO PYTHON PROGRAMMING"

# 3. strip() :- This method removes any leading and trailing whitespace from a string.
str = "   hello , welocome to python programming"
print (str.strip())

# 4. replace() :- This method replaces all occurrences of a specified substiring with another substring in a string.
str = "Anil is a good boy"
print (str.replace("Anil","sunil"))