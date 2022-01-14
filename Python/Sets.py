#A set is a collection which is unordered and unindexed.
thisisset = {"apple", "banana", "cherry"}
print(thisisset)

#################
#Changing items
#Once a set is created, you cannot change its items, but you can add new items.
#add() will add one item at a time
thisisset.add("orange")
print(thisisset)
#update() will add multiple items at a time
thisisset.update(["orange", "mango", "grapes"])
print(thisisset)

#################
#Removing items
thisisset.discard("banana")
print(thisisset)

#Rest of it is same as a list