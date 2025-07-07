#STRINGS ARE IMMUTABLE
#But Lists are.
#Lists are reference types
#Use Deepcopy function to make a copy of the list.

import copy

#Item in list can be accessed using index but not in the string.
listEx = [1,2,3,4,5]
listEx[0] = 100
print(listEx)

listEx1 = listEx
listEx1[4]=6    #both the lists are modified as they are reference type
print(listEx)
print(listEx1)


#using the deep copy method does not modify the original list when the deep copied list is modified.
original = [1,2,3,4,5]
deepCopiedList = copy.deepcopy(original)
deepCopiedList[0] = 99
print(original)
print(deepCopiedList)

#List can be split to multiple lines, unlike for other statements Python ignores indentation for lists
multiLineList = ["Ant","Bat",
                 "Cut","Dart",
                 "Eat","Feet",
"Greet","Heat"]
print(multiLineList)


#Strings cannot be modified using indexes
stringEx = "This is a funny try"
#stringEx[0] = "A"
#print(stringEx)


#Line Continuation

lcString = "This is  \
        Kind of Cool"
lcStringConcat = "This one is"\
" Interesting tooooo"
lcCalc = 5+\
    8+\
    10
print(lcString)
print(lcStringConcat)
print(lcCalc)