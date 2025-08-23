# Creating a set
names = {"Pradip", "Suman", "Ayan", "Atanu", "Koushik", "Suraj"}

# Print set
print(names)

# Check length of set
print(len(names))

# Check data type of set 
print(type(names))

# Accessing items of set
for x in names:
    print(x)
    
# Check if an item exists in a set
if "Atanu" in names:
    print("Atanu is in the set")    
    
# Adding item to a set (add element in set)    
names.add("Jitu")
print(names)

# Add another sequence in a set
names_list = ["Sujit", "Sudip"]
names.update(names_list)
print(names)

# Removing element from a set
names.remove("Sujit")
print(names)

names.discard("Tumpa")  # this function will not throw an error if value is not present in set
print(names)


# Joining 2 Sets
set1 = {'a', 'b', 'c', 'x'}
set2 = {'x', 'y', 'z'}
# print(set1, set2)

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

# Keep only duplicates while joining
set1.intersection_update(set2)
print(set1)

# Keep all except duplicates
set1.symmetric_difference_update(set2)
print(set1)
