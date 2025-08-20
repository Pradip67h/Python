''' Take input percentage of a student and print the Grade according to marks:
1> 81-100 Very Good
2> 61-80 Good
3> 41-60 Average
4> <=40 Fail '''

marks = int(input("Enter Your Marks: "))

# if marks are between 81 and 100 
if marks>80:
    print("Very Good")
    
# if marks are between 61 and 80    
elif marks>60:
    print("Good")

# if marks are between 41 and 60     
elif marks>40:
    print("Average")
    
# if marks are less than or eaual to 40    
else:
    print("Fail")            
