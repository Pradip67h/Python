class Animal:
    def __init__(self, species):
        self.species = species
 
    def make_sound(self):
        return "Some generic sound"
 
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name
 
    def make_sound(self):
        return "Woof!"
 
class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name
 
    def make_sound(self):
        return "Meow!"
 
# Creating instances of subclasses
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
 
# Accessing attributes and methods of subclasses
print(dog1.name)             # Output: Buddy
print(cat1.species)          # Output: Cat
 
print(dog1.make_sound())     # Output: Woof!
print(cat1.make_sound())     # Output: Meow!
