#  Loop 
# Loop is used to repeat a block of code multiple times 
# There are two type of loop 
# 01 for loop
# 02 while loop

# for loop :- for loop used when the number is iteration is known for loop 
# syntax  for variable in sequence
#   code 

#  write the code print 5 number 

for i in range(1,6):
    print(i)

# write the code print the table value given by the user 

# num = int(input("Enter the number"))

# for i in range(1,11):
#     print ("x" ,i, "=", num*i)

# write the code prind the 5 number 
num = 5
for i in range (1, 11):
    print ("num" , i , "=" ,num *i )


# write the code find even number of range 10 

for i in range(1,10):
    if i % 2 == 0:
        print("The even number" , i)
    else:
        print("The odd number " , i)

# write the code print the sum of number 

n = int(input("Enter the number "))

total = 0

for i in range(1 , n+1):
    total += i 

    print("sum" , total)

 
