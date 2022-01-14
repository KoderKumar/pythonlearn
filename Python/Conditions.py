#Conditions in python
#a == b    Equals
#a < b     Less than
#a > b     Greater than
#a >= b    Greater than or equal to
#a <= b    Less than or equal to
#a != b    Not Equals

###################
#If
a = 33
b = 200
#It is checking if b is greater than a
if b > a:
    #Then print "b is greater than a"
    print("b is greater than a")

##################
if b > a:
    print("b is greater than a")
#Elif is nested so it will run too
elif a == b:
    print("a and b are equal")

################
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#If the first two statements are not true else will execute
else:
  print("a is greater than b")

################
#And
c = 500
#If both statements are not true it will not execute
if a > b and c > a:
    print("Both conditions are True")

################
#Or
#If one of them is true it will execute
if a > b or c > a:
    print("Both conditions are True")