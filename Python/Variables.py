#Variables arecontainers for sorting data values.
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.
#x is a variable and 5 is it's value.
x = 5
#Printing x
print(x)

#A variable can change after declaring it.
x = 4 #x is of type int
x = 9 #x is of type str
print(x)

###########################

#Global Variables
#Variables that are created outside of a function are known as global variables.
#Global variables can be use by everyone, both inside of functions and outside.
#Learn more about functions in Functions.py
x = "awesome"

def myfunc():
	print("Python is " + x)

myfunc()

y = "awesome"

def myfunc2():
	#The variable created inside the function 
	#remain in the function.
	x = "fantastic"
	print("Python is " + y)

myfunc2()
#This will print "Python is awesome"
print("Python is " + y)

#Global Keyword
#Global Keyword will help us create global variables inside a function.

def myfunc3():
	global x
	x = "fantastic"
myfunc3()
print("Python is " + x)





