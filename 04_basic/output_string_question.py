''' quantity = 3
    item_number = 567
    price = 49.95
    Replace the variables in this string with their values and print the output string:
    I want quantity pieces of item_number item for price dollars. '''
    
quantity = 3
item_number = 567
price = 49.95
 
output_string = "I want %d pieces of item %d for %.2f dollars." % (quantity, item_number, price)
print(output_string)    
