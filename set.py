# A set a python is a collection of unique elements. It is an unordered data sructure. It is mutable and iterable. It is used to store multiple items in a single variable. It is defined by using curly braces {} or the set() funaction. It is not allowed to have  duplicate elements in a set. 

# Different bitween mutables and immutables in python is that mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created.

# Supports fast search, insertion, and deletion operations. It is commonly used for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference. 

s= {10, 20, 30, 40, 50}
print(s)
print(type(s))


name = ["Anil", "Sunaina" , "Sunil" , "Ramesh", "Anil"]
print(name)
print(type(name))
name = set(name)
print(type(name))

num2 = {"Sunil", "Anil", "Sunaina" , "Anil"}
print(num2)

num2.add("Ramesh")

print(num2)

# Use add() method to add an element to thne set. If the element already exists, it will not be added again. 

# Use remove() method to remove an element from the set. If the element does not exist, it will raise a key error. 

num2.remove("Sunaina")
print(num2)

num2.remove("Deepak")
print(num2)

# discard() method to remove an element from the set. If the element does not exist, it will not raise an error.

num2.discard("Deepak")
print(num2)


Story = "Anil is a good boy. He is from hazaribagh Jharkhand and his gf name was Sunaina."
Story2 = "Now she is married to Tinku kumar and they are living in ranchi. Anil is still single and he is working in a software company in Bangalore."

Story3 = Story.union(Story2)
print(Story3)

# Difference is use difference() method to get the differenc between two sets. It will return a new set with elements that are present in the first set but not in the second set.

a = {1,3,3,45,6,6,7}
b = {34,67.79,8,2,3, }
c = a.difference(b)

print(c)

