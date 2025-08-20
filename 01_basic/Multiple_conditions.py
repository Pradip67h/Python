eng_marks = int(input("Enter marks in English: "))
math_marks = int(input("Enter marks in Math: "))

# if both are more than 80, print A grade
if eng_marks > 80 and math_marks > 80:
    print("GRADE-A")
    
# if either of marks are more than 80, print B grade
elif eng_marks > 80 or math_marks > 80:    
    print("GRADE-B")
    
# if neither of marks are more than 80    
else:
    print("GRADE-C")
