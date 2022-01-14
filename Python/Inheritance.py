#Inheritance allows us to define a class that inherits all the methods and properties from anothe class
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class alse called derived class

################
#Parent Class
#Creating a class named Person, with firstname and lastname properties
class Perdon:
    def __init__(self, fname, lname):
        self.firstname = fname
        self,lastname = lname

    def printname(self):
        print(self.firstname, self.lastnme)

#Use the Person class to create an object, and then execute the printname method
x = Person("John", "Doe")
x.printname()

###############
#Child class
#Creating a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
    pass

#__init__() function
#The __init__() function is called automatically every time the class is being used to create a new object.
class Student2(Person):
    def __init__(self, fname, lname):
        #Add properties etc.





