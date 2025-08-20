# Take 3 Positive integers input and print the greatest of them ?

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# if n1 is the greatest
if n1 >= n2 and n1 > n3:
    print("Greatest = n1")
    
# if n2 is the greatest    
elif n2 >= n1 and n2 > n3:
    print("Greatest = n2")

#if n3 is the greatest
else: 
    print("Greatest = n3")        
