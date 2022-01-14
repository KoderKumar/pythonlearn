#A dictionary is a collection which is unordered, changeable and indexed.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

###################
#Accessing Items
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

###################
#Changing Values
thisdict["year"] = 2020
print(thisdict)

##################
#Looping
for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x in thisdict.items():
    print(x, y)

#################
#Conditions
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary.")

################
#Adding and Removing items
thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

################
#Copying dictionary
mydict = thisdict.copy()
print(mydict)

###############
#Nesting
myfamily  = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


