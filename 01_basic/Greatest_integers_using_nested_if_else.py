# Take 3 positive integers input and print the greatest of them ?

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# using nested if else statement
# comparing n1 and n2
if n1 > n2:
    # either n1 or n3 is greatest
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(n3, "is the greatest element")
else:
    # either n2 or n3 is greatest
    if n2 > n3:
        print(n2, "is the greatest element") 
    else:
        print(n3, "is the greatest element")
               
