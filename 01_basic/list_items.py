# list items with Array:

fruits = ['apple', 'banana', 'mango', 'cherry']

print(fruits)   # print a list

print(type(fruits))  # check type of list

print(len(fruits))   # check length of list

# checking if an item is  present in the list
if "banana" in fruits:
  print("Banana is part of the list")
  
# checking if an item is not present in the list
if "kiwi" not in fruits:
  print("kiwi is not part of the list")  
  
  
# indexing in list
print(fruits[1])    # banana

# negative indexing in list
print(fruits[-3])   # banana

# Range of indexes in list
print(fruits[1:3])     # ['banana', 'mango']

# Range of negative indexes in list 
print(fruits[-3:-1])   # ['banana', 'mango']
  
