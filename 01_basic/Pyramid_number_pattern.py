# Print the Given pattern Pyramid

n = int(input("Enter the value of n: "))
 
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
