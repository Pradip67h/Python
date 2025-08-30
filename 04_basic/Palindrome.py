# Write a Python function that checks if te given string is a palindrome or not.

def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase
    clean_string = input_string.replace(" ", "").lower()
 
    # Compare the original string with its reverse
    return clean_string == clean_string[::-1]
 
# Test the function
test_string1 = "radar"
test_string2 = "Python"
test_string3 = "A man a plan a canal Panama"
 
print(is_palindrome(test_string1))  # Output: True
print(is_palindrome(test_string2))  # Output: False
print(is_palindrome(test_string3))  # Output: True
