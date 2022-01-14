#Loops in python
#While loop
#With while loop we can execute a set of statements as long as a condition is true.

i = 1
#While i is less than 6 it will run
while i < 6:
    #This will print i everytim it runs
    print(i)
    #This will add i with 1 everytime it runs
    i += 1

#################
#Continue
#With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

################
#Else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

################
#For loop
#For loop is used for iterating over a sequence  (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

################
#Looping through a string
for x in "banana":
    print(x)

###############
#Break
for x in fruits:
    print(x)
    if x == "banana":
        break

###############
#Continue
for x in fruits:
    print(x)
    if x == "banana":
        continue
    print(x)

###############
#Range
for x in range(6):
    print(x)

###############
#Else
for x in range(6):
  print(x)
else:
  print("Finally finished!")
