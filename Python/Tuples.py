#A tuple is a collection which is oredered and unchangeable.
thisisTuple = ("apple", "banana", "cherry")
print(thisisTuple)

##################
#Changing tuple value
#You can't change tuple value but we have a work around
x  = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Rest of it is same as a list

