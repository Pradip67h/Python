# Write a Python function that checks if te given string is a palindrome or not in user input.

def check_palindrome(str):
    
    # Cleaning the String
    clean_str = (str.replace(" ", "")).lower()
    
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

# User input
str = input("Enter a string: ")
if check_palindrome(str):
    print("It is a Palindrome String")
else:
    print("It is not a Palindrome String")    
