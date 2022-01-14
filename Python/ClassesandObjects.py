#Python is an object oriented programming language.
#Almost everything in python is an object, with its properties and methods

#################
#Class
#Creating a class named MyClass
class MyClass:
    x = 5
#Object
#Creating an object named p1, and printing the value of x
p1 = MyClass()
print(p1.x)

#################
#__init__() function
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#__init__() function is used to assign values to object properties, or other operations that are necessary.
#Creating a clas named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Arth", 15)

print(p1.name)
print(p1.age)

#################
#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object
#Inserting a function that prints a greeting, and execute it on the p1 object
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)
p2 = Person2("Arth", 15)
p2.myfunc()

#################
#Self parameter
#The self parameter is a reference to the current instance of the class, 
#And is used to access variables that belongs to the class.
#Using mysillyobject instead of self
class Person3:
    def __init__(mysillyobject, name, age):
        self.name = name
        self.age = age
    
    def myfunc(abc):
        print("Hello my name is " + self.name)
p3 = Person3("Arth", 15)
p3.myfunc()
#It will give an error



