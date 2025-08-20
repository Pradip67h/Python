# Take positive integer input and tell if it is divisible by 5 and 3 ?

# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking if the number is divisible by both 5 and 3
if number % 5 == 0 and number % 3 == 0:
    print("The number is divisible by both 5 and 3.")
else:
    print("The number is not divisible by both 5 and 3.")
 
