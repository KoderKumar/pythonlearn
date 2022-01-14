#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
import re

txt = "The rain in Spain"
#Searching if the sectence starts with "The" and ends with "Spain"
x = re.search("^The.*Spain$", txt)
print(x)

################
#Functions in RegEx
#Findall()
print("\n")
x = re.findall("ai", txt)
print(x)

#Search()
print("\n")
x = re.search("^The.*Spain$", txt)
print(x)

#Split()
print("\n")
x = re.split("\s", txt)
print(x)

#Sub()
x = re.sub("\s", "9", txt)
print(x)









