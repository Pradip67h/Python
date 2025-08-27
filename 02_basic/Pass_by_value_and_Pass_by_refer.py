# Pass by value

def addOne(x):
    x = x + 1
    print("Inside function:", x)

x = 5
addOne(x)
print("Outside function:", x)    

# Pass by reference

def modifyList(lst):
    lst.append(4)
    lst = [4,5,6]
    print("Inside function", lst)

my_list = [1,2,3]
modifyList(my_list)
print("Outside function:", my_list)    
    
