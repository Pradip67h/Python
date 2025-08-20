# Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15?

num = int(input("Enter a positive Number : "))

# checking whether it is divisible by 15
if num % 15 == 0:
    print("Number is divisible by 15")
else:
    # checking if divisible by 3 or 5
    if num % 3 == 0 or num % 5 == 0:
        print("Number is not divisible by 15 but divisible by 3 or 5")  
    else:
        print("Number is neither divisible by 3 nor by 5")      
