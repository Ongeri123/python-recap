# Properties are variables that belong to a class. They store data for each object created from the class

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # property brand
        self.model = model  # property model

car1 = Car('Toyota', 'Corolla')
# print(car1.brand)  # Accessing property brand using dot notation
print(car1.model)  # Accessing property model using dot notation

car1.brand = 'Honda'  # Modifying property brand using dot notation
# print(car1.brand)  # Output: Honda

del car1.brand  # Deleting property brand using del keyword

# Class Properties vs Object Properties
# Class properties are defined within the class and are shared by all instances of the class.
# Object properties are specific to each object and can have different values for each instance.

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")
p1.age =25  # Adding new instance property 
Person.species = "Mammal" # Modifying class property

print(p1.name, p1.age)
print(p2.name)
print(p1.species)
print(p2.species)

# Adding properties this way only adds them to that specific object, not to all objects of the class
