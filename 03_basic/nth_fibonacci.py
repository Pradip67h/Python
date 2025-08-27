# Write a function to calculate the nth fibonacci number using recursion.

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(7)
print(result)  
