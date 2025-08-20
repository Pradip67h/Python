# Determine whether the year is a leap year or not ?

# Taking a year input from the user
year = int(input("Enter a year: "))
 
# Checking if the year is a leap year
print()
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
 
