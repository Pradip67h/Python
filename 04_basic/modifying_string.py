# Modifying String 

text = "Hello, World!"
 
# Convert the entire string to uppercase
uppercase_text = text.upper()
 
print(uppercase_text)  # Output: HELLO, WORLD!

# Convert the entire string to lowercase
lowercase_text = uppercase_text.lower()

print(lowercase_text)   # Output: hello, world!

# Convert the entire string to Capitalize
capitalize_text = lowercase_text.capitalize()

print(capitalize_text)  # Output: Hello, world!

# for stripping/removing any trailing whitespaces
name = "     Hello, Pradip       "

print(name.strip())    # Output: Hello, Pradip

# Replace substring
sentence = "Hello world, what a beatiful world this is!"
print(sentence.replace("world", "earth"))


# Splitting string
str1 = "suman,ayan,atanu,avi,koushik,jitu"
list = str1.split(",",3)
print(list)


# Concatenation string
str2 = "Hello World!"
str3 = " What a geat place this is."
print(str2+str3)


# Format string
student_name = "Pradip"
student_marks = 96

str5 = "The student is {s}, and marks is {m}".format(s = student_name, m = student_marks)
print(str5)


 
