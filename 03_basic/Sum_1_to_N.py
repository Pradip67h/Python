# Write a program to print sum from 1 to n.

def sum_1_to_N(n):
    
    # base case
    if n == 1:
        return 1
    
    # recursive case
    ans = n + sum_1_to_N(n-1)
    return ans

n = int(input("Enter n: "))
print("The Total number of Sum:",sum_1_to_N(n))    
