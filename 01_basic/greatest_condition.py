# Taking three positive integer inputs from the user?
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
# Comparing the numbers to find the greatest using nested if-else
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3
 
# Printing the greatest number
print("\nThe greatest number is:", greatest)
