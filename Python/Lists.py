#A List is a collection which is ordered and changeable.
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#              0        1         2         3        4        5        6
#             -7       -6        -5        -4       -3       -2        -1
print(thisList)

##################
#Accessing Items
print(thisList[1])
print(thisList[-2])
#Range Indexes
#The search will include 2 and end at 4
print(thisList[2:5])
#If we don't specify the first index it will start from the beginning
print(thisList[:4])
print(thisList[4:])
#The search will include -4 and end at -2
print(thisList[-4:-1])

##################
#Changing Items
thisList[3] = "Guava"
print(thisList)

##################
#Looping
#Learn more about loops on Loops.py
for x in thisList:
    print(x)

##################
#Conditions
#Learn more about Conditions on IfElse.py
if apple in thisList:
    print("Yes, 'apple' is in the fruits list.")

##################
#Adding Items
thisList.append("strawberry")
print(thisList)

##################
#Inserting Items
#This will insert pineapple in seccond position
thisList.insert(1, "pineapple")
print(thisList)

##################
#Removing Items
thisList.remove("banana")
print(thisList)


