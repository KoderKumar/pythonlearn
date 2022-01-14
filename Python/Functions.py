#A Function is a block of code which only runs when it it called.
#You can pass data, Known as parameters, into a function.

def myfunction():
    print("Hello from a function")
myfunction()

##################
#Argumants
#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.
#The function expects 2 arguments.
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Tobias", "Great")
my_function("Linus", "TooGreat")
my_function("Emil", "MuchGreat")

#If the number of argument is unknown add a * before the parameter
def my_kids(*kids):
    print("The youngest child is " + kids[2])
my_kids("Emil", "Tobias", "Linus")

#You can also send arguments with the key = value syntax.
def mykids(child3, child2, child1):
    print("The youngest child is " + child3)


mykids(child1= "Emil", child2= "Tobias", child3= "Linus")

def my_list(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_list(fruits)



