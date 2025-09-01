class Rectangle:
    
    def __init__(self, height, width):
        print(f"A rectangle is created with height: {height} and width: {width}")
        self.height = height
        self.width = width
        
    def set_dimensions(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width    
    
    def perimeter(self):
        return 2*(self.height + self.width)    
    
# Creating objects
rectangle1 = Rectangle(4,3)
rectangle2 = Rectangle(5,7)
rectangle3 = Rectangle(10,2)
print("The height and width are: ", rectangle1.height, rectangle1.width)
print("The area is: ", rectangle1.area())
print("The perimeter is: ", rectangle1.perimeter())
print("The height and width are: ", rectangle2.height, rectangle2.width)
print("The area is: ", rectangle2.area())
print("The perimeter is: ", rectangle2.perimeter())
print("The height and width are: ", rectangle3.height, rectangle3.width)
print("The area is: ", rectangle3.area())
print("The perimeter is: ", rectangle3.perimeter())



