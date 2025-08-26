# Function which takes 2 numbers as input and returns their sum
def add(n1=0, n2=0):
    print("n1: ",n1)
    print("n2: ",n2)
    sum = n1+n2
    return sum

# 1. Positional Argument
print("The Sum is", add(8,2))

# 2. Keyword Argument (named arguments)
print("The Sum is", add(n1=3, n2=4))

# 3. Default Arguments
print("The Sum is", add(9))

# 4. Arbitrary Arguments
#(i) Non-Keyword Variable-Lendth Arguments(*args):
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
        return sum

output = addAllNumbers(9,6,7,8,5)
print("The Sum is: ", output)   

#(ii) Keyword Variable-Length Arguments(**kwargs)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":" + value)
        
display_info(name="Pradip",age="23",city="Haldia") 
display_info(name="Suman",age="22",city="Kolkata")      
