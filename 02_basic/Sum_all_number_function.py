# Writing a function for calculating sum from 1 to n
def sumOneToN(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

n = int(input("Enter n: "))
# Call Function
output = sumOneToN(n)
print("Sum of all numbers till n is", output)    
