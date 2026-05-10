# python is a programming language . it is a interpreted and high level programming language. it is a also like engliish language.
# it is used backend in development. releaesd in 1991. create by guido van rossum.

# it is simple and readable syntex and language.

# what is interpreted language.
# interpreted in code means that the source code is executed line-by-line by an interpreter.n program at runtime.

#  first code in python.
# like this

print("Hello, Anil")

# This is the first code of pyhton language.

#  print :- it is keyword usde for the print the output.

# variable :- variable is name it is gives location of memory.
# if we You want add two number in pyhton then  first of all You take two variable for value defind 
# lets see how to defind the variable
#  First code 

print ("Hello ,Welcome to Python")

# 02 write the code add two number 

a = 20
b = 30
c = a+b
print(c)

# so here a is variable and b is also is variable for given some value as a location;
# a and b is interger type variable 

#  what is datatype 
# Type is define as the which type of data user given. Bescaly it is defined for which type of data gives 
# There 5 type of datatype in python
# O1 Interger 
# 02 string 
# 03 Float
# 04 Boolean 
# 05 NUll

# Interger :- interger is a datatype is it defined as we can gives interger type data given by user  only
# like a = 20 
# like b = 30 

# here a and b is interger datatype 

# 02 String :- String is a also datatype it is defined string type of data 
# we given like name , sentence and paragrph 

# name = "Anil"
# details = "My name is Anil , I am Hazaribagh Jharkhand"

name = "Anil"
details = "My name is Anil , I am Hazarbagh"

print(name , details)

# if we want find the which type of datatype use type keyword 
# like
username = "Sunain Choudhary"
print(type(username))

#  03 Float :- it is defind as floating data type of data 
# like  a = 2.34
#  like b = 3.50
a = 2.34
b = 3.50
c = a - b
print(c)

# Boolean :- it is defind as a true and false 
# Use like :- Ture and False not use ture and false 

# is_active = True
is_active = False 
print("use is active")


# Salve some questin 
# 01  write the program print the hello word 

print("Hello world")

# 02 Write the code and add two number 

a = 50
b = 30
c = a+b
print(c)

# 03 write the code to given value by user and add two number 
 
a  = int(input("Enter the value of a"))
b= int(input("Enter the value of b"))
sum = a+b

print("The sum value of a and b" ,sum )

#  write the program for print the precentage of student 
phy =  float(input("Enter the number of physic"))
che = float(input("Enter the number of Chemistry"))
math = float(input("Enter the number of math"))

ave = phy+che+math/3 

print ("The precentage of Student",ave)

# write the code print the given number are even and odd 

a = int(input("Enter the number"))

if a % 2 == 0:
    print ("The number is even")
else:
    print ("The number is oss")

# 04 write the code check the number is negative and positive and  zero 

num = int(input("Enter the number"))

if num > 0:
    print ("The number is Positive")
elif num == 0:
    print ("The number is zero")
else:
    print ("The number is Negative")

# write the code print the largest number gives value by the user

num = int(input("Enter the first number"))
num02 = int(input("Enter the second the number"))

if num > num02:
    print ("The number first number is largest number")
else:
    print("The second number is largest number")

# what is the output 

x = "10"
b = 5 

print(x + str(b))

# out is 105

# loops :- The loop is used repaet a block of code multiple times


# Moduls 
# pip
# modules there are two type 
# 01 Built in modules :- All ready in python no need for install in python 
# 02 External modules := Extrnal modules hum usko kahte hai logo ne develop karte hai or hun us import kr ke use kr sakte hai
# print :- it is a function use for print and display any in code 
# And aslo you can say that it is use for output tha data 

# command :- it is very importnd for know the code why write the code 
# command ko hum esliye use karte hai na kyu ki uske use kr ke pata ke skte hai ki jo code hum likhe hai usko hum kyu likhe hai tak pata chale 
# Threre are two type of command 
# singel line command 
# Multi line 

# Escap  sequence charactors
# \n 
# sep and end 
 
print("Hii, This is demo" ,6,7 , sep="~" , end="008\n")
print("Anil")

# variable :- it is like container use for the store tha data.
# Variable me hum data ko save karte ha memory us se hume uska location ka pata chata hai.
# Data type :- Data type is defind as a the which type of data we given.
# list:- list is defind the list of item defind the different type of list of item.
# python me saphi prakar ke datetype sab kuchh object hota hai
# operatores :- Do some task 


# Typecasting :- The conversion one data type to other datatype that is called typecasting.
# There are two type 
# Expilcit Conversion :- Is me khud se Conversion kr sakte hai.
# Implicit Conversuin :- Is me python  khud conversion karta hai 
# if we want to find the type of variable we can use type keyword 
# variable name are case sensitive like 
# a = 34
# A = "Anil"
# This will create two variable
# a will not overwrite a 


# Variable Names 

# A variable can have a short name (Like x and y ) or a more descriptive name (age, carname, total_volume).
# Rule for python variable 

# A variable name must start with a letter or the underscore character.
# A variable can not be start with a number .
# A variable name can only contain alph-numeric character and underscore (A-Z,a-z, 1-9)
# A variable are case sensitive like (age,AGE and Age ) There are three different variable.

# Multi Words variable Names 
# Variable names with more than one word can be difficult to read. 

# Camel Case :- Each word except the first , Starts with a capital letter.
# myVariableName = "john"

# Pascal Case:- Each word starts with a capital letter.
# like :- myVariableName = "john"
# Snake Case :- Each word is separated by an underscore character.


# Many Values to Multiple Variable 
# python allow you to assign values multiple in one line.

# x,y,z = "Orange" , "Banana" , "Cherry"
# print(x)
# print(y)
# print(z)

a,b,c = "Anil" , "Sunil" , "Pawan"
print(a)
print(b)
print(c)



# One value  to Multiple Variable 
# And You can assign the same  value to multiple variable in one  line .
# like a=b=c = "orange"

# Global variables 
# Vriable that are created outside of the of a function.
# Global variable can be used by everyone , both inside of function and outside

x = "Sunaina"

def myfun():
     print("Python is " + x)
 
myfun()


# Local variable :- Local variable defind as inside the function
# Local variable can not used by everyone , inside and outside the function

def demo():
    name = "Anil"
    print("Your name is" , name)
demo()

# Datype :- variable store the data different type, But datatype can defind which type of type data we store in  your code.
# Type of datatype in  python :-
# String :- it is use for store the chatter type data , We can use for defind the datatype use str 
# intiger :- It is use for intiger data data store data in  your code , we can use int for defind tha intiger type data.
# Sequence type :- it is use for list , tuple , range type data 
# Mapping :- it is use for mapping type data , keyword dict
# Boolean type :- it is use for ture and flase type data type.

# Number type :- There are three number type in python 
# int 
# float
# complex like number with chartter 

# specify a variable  type :-
# There may be times when  you want to speclfy a type of variable 
# Casting in python is therefore done  using construcotr funcation 

# int() :- It is type for integer type data 
# float() :- It is used for the float type data type casting 
# str() :- String type data 

# Strirng :- Strings it is also datatype it is use chareter type data store , String i python surrounded  by either single , 
# quotation marks , or double quotation marks.

# 'hello', "hello"

# And you can assign the a multiple string to a variable by using three quotes.
# a = """  write any thing hare """ :- it id defind the multiline string in python.

# Like many programming language , string in python are arrays of unicode characters.
# Square brackets can use to access elements od the string.

# like name = "My Name is Anil kumar rana"
# print(name[1])
# output :- y

# 