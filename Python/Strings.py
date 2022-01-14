#A variable is just like container in which we can store values.

#Message is a variable and Hello World is it's value.
#Learn more about variables in Variables.py
message = "Hello World"

#len() will show the length of the string.
print(len(message))

#Python is case sensitive so these three are different variables.
this = 1
This = 2
THIS = 3

###########################

#Python also allows to assign values to multiple variables in one line.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#We can alo assign same values to multiple variables.
x = y = z = "Blop"
print(x)
print(y)
print(z)

###########################

#Always use double quotes so it will not mind the apostrophe.
another_message = "Arth's World"
#				   012345 678910

#[] will help us access the string's characters individually.
print(another_message[4])

#We can also access the certain part of the string.
#It will not include the fifth index number.
print(another_message[0:5])
print(another_message[:5])
print(another_message[6:])

###########################
#Negative Indexing
b = "Hello World"
print(b[-5:-2])

###########################
#If we wanted to use multiline in a string we need to use triple double quotes.
third_message = """So this is what you call 
Multiline String"""

#lower() will turn all the string value lowercase.
print(third_message.lower())

#upper() will turn all the string value uppercase.
print(third_message.upper())

#count() will count the times the value is repeated.
print(third_message.count("i"))

#find() will find the certain value in the string and will give the location.
print(third_message.find("what"))

#replace() will replace a value with another one.
third_message = third_message.replace("String", "Strings")
print(third_message)

###########################

#Combining Strings
greeting = "Good evening"
name = "Arth"

#1 way
combined = greeting + ", " + name + ". Welcome!"
print(combined)

#2 way
#{} will work as a placeholder and later we can fill them with any values.
#in the format function greeting is filling the first placeholder and name is filling the second placeholder.
combined = "{}, {}. Welcome!".format(greeting, name)
print(combined)

#3 way
#We can directly fill the placeholder by putting a f in the start.
combined = f"{greeting}, {name}. Welcome!"
print(combined)


