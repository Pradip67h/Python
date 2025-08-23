# Creating a tuple
colours = ("red", "yellow", "green", "black", "blue")

# Creating a tuple with 1 item
fruit = ("apple",)        # <class 'tuple'>
fruit = ("apple")           # <class 'str'>
fruit = tuple("apple")     # <class 'tuple'>

# Check type of tuple
print(type(colours))

print(type(fruit))

# Check length of tuple
print(len(colours))

# Accessing items of a tuple
print(colours[1])   # positive indexing

print(colours[-4])  # negative indexing

print(colours[1:3])   # range of index

print(colours[-4:-2])  # range of negative index

# Check if item exists in a tuple
if "green" in colours:
    print("Green is part of tuple")

# Traversing through a tuple
for i in colours:
    print(i)

# Concatenation of Tuples
more_colours = ("orange", "brown", "yellow")
colours = more_colours + colours
print(colours)

# Unpacking a tuple
colour1, colour2, colour3, colour4, colour5 = colours
print(colour1, colour2, colour3, colour4, colour5)
