# Adding elemenet to a list
list = [10, 20, 30, 40, 50]
print(list)      # [10, 20, 30, 40, 50]

list.append(60)
print(list)      # [10, 20, 30, 40, 50, 60]

list.insert(2, 70)
print(list)     # [10, 20, 70, 30, 40, 50, 60]

list2 = [100, 200, 300]
list.extend(list2)
print(list)   # [10, 20, 70, 30, 40, 50, 60,100, 200, 300]

# Removing element from a list
fruits = ["apple", "banana", "mango", "kiwi"]
fruits.remove("banana")
print(fruits)            # ['apple', 'mango', 'kiwi']

fruits.pop(0)
print(fruits)           # ['mango', 'kiwi']

fruits.pop()
print(fruits)      # ['mango']


# Changing item in a list
mylist = [10, 20, 30, 40, 50]
mylist[1] = 40
print(mylist)    # [10, 40, 30, 40, 50]

mylist[1:3] = [100, 200]
print(mylist)
