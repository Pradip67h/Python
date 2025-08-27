# Write a program to print numbers from 1 to n

def print_n_to_1(n):
    
    # base case
    if n == 0:
        return
    
   
    # recursive case
    print_n_to_1(n-1)
    print(n)
    
n = int(input("Enter n: "))
print(print_n_to_1(n))    
