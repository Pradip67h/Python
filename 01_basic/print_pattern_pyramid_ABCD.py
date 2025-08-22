# Print the given pattern Pyramid ABCD

n = int(input("Enter a number: "))

for i in range(n):      # loop for rows
    for j in range(i+1):    # loop for columns
        print (chr(j+65), end = " ")
    print()
    
