class MyClass:  # create a class named MyClass
    x=5
p1 = MyClass() # create an object p1 of class MyClass
print(p1.x)
p2 = MyClass()
print(p2.x)

del p2 # delete object p2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class World:
    pass


# You can create multiple objects from the same class
#  Each object is independent and has its own copy of the class properties.
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

