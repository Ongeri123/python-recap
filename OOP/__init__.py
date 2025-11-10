# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)

print(p1.name)
print(p1.age)

# method is called automatically every time the class is being used to create a new object.
# Without the __init__() method, you would need to set properties manually for each object
# Using __init__() makes it easier to create objects with initial values

# You can also set default values for parameters in the __init__() method

class Car:
    def __init__(self, brand , model='corolla'): # default value for model
        self.brand = brand
        self.model = model

car1 = Car('Toyota')
car2 = Car('Honda', 'Civic')

print(car1.brand, car1.model)
print(car2.brand, car2.model)

# The __init__() method can have as many parameters as you need


class Car:
    def __init__(self, brand , model, year,color):# multiple parameters
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

car1 = Car('Toyota',2020,'corolla','red')
car2 = Car('Honda', 'Civic',2019,'blue')

print(car1.brand, car1.model, car1.year, car1.color)
print(car2.brand, car2.model, car2.year, car2.color)
