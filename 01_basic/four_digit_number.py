# take positive integer input and tell if it is a four digit number or not ?

number = int(input("Enter any four digit number: "))
                   
if number >= 1000 and number <= 9999:
    print("It is a 4 digit Number")
else:
    print("It is not a 4 digit Number")    
