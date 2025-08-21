# Display this AP - 1,3,5,7,9.. upto 'n' terms ?

n = int(input("Enter the number of terms: "))
 
current_term = 1
common_difference = 2
 
print("\nAP:", end = " ")
for _ in range(n-1):
    print(current_term, end=", ")
    current_term += common_difference
print(current_term)
