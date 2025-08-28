# Assigning Stringto a variable

name1 = 'Hello My name is Pradip Hazra,'

name2 = "I'm from Haldia,"

name3 = '''I'm a Mechanical Engineer student'''

print(name1, name2, name3)
print(type(name1))
print(type(name2))
print(type(name3))


# Array-like indexing in string

text = "Hello, World"
print(text[0])
print(text[4])
print(text[-1])


# Traversing a string

# using for loop
text1 = "Hello, Ji"
for i in text1:
    print(i)
    
#  using list comprehension
list = [char for char in text1]
for i in list:
    print(i)


# find the length of a string
text2 = "Hii, i'm Pradip!"
length = len(text2)
print(length)   

   
    
