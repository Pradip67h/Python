# List Comprehension 
fruits = ["apple", "banana", "mango", "kiwi", "orange"]

new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# Coping a list
new_fruits = fruits.copy()
print(new_fruits)

# Concatenation of lists
new_fruits = new_fruits + fruits
print(new_fruits)

# Nested Lists
list = [10, 20, 60, 70, 80]
print(list)

list.insert(2, [30, 40, 50])
print(list)
print(list[2][1])
