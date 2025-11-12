# The self parameter is a reference to the current instance of the class
# It is used to access properties and methods that belong to the class

class Car:
     def __init__(self, brand, model):
         self.brand = brand  # using self to refer to the instance variable
         self.model = model  # using self to refer to the instance variable

     def display_info(self):
         print(f"Car Brand: {self.brand}, Model: {self.model}")  # using self to access instance variables
    
car1 = Car('Toyota', 'Corolla')
car1.display_info() #  # Output: Car Brand: Toyota, Model: Corolla


## Calling methods with self

class Person:
    def __init__(self,name):
        self.name = name 

    def greet(self):
        return f"Hello, my name is {self.name}"  # using self to access instance variable
    
    def farewell(self):
        message = self.greet() # using self to call another method
        print(message + ", goodbye!")

p1 = Person("Bob")
p1.farewell()  # Output: Hello, my name is Bob, goodbye!