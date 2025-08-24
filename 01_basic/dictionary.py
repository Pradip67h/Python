# Creating a Dictionary
phones = {
    "John" : 98763,
    "Atanu" : 68922,
    "Ayan" : 98763,
    "Suman" : 88672
}
# Printing the dict
print(phones)

# Checking type of dic
print(type(phones))

# Check the length of dict
print(len(phones))

# Access items of dict
print(phones["Suman"])
print(phones.get("Suman"))

print(phones.keys())

# Upadate value in dict
phones["John"] = 46785
print(phones)

# Add elements in dict
phones["Kia"] = 72689
print(phones)


more_phones = {
    "Pradip" : 76543
}

phones.update(more_phones)
print(phones)

# Remove elments in a dict
phones.pop("Kia")
print(phones)

phones.popitem() #this will remove the last added item
print(phones)

phones.clear()  # this will empty the dict
print(phones)

