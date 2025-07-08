#Sets
#sets ignore the duplicate items
#Items in the sets are un orderd, hence the values are printed in different order every time. print(set2)
#Sets are useful when we need collection of items and do not want duplicates and do not care of the order


set1 = {9,9,8,7,7,9,8,7,6}
set2 = set({"a","a","b","c","d","e"})
emptySet =set({})
setRange = set(range(1,12,2))   #in this case we always get the values in sequence as we are using the range function which dynamically generates the value in this sequence
print(set1)
print(set2)     
print(setRange)

for item in set1:
    print(item)

print( 9 in set1)


cities = ["bangalore","hydrabad","bangalore","chennai","mumbai","delhi","calcutta","delhi","kochi"] #this list contains duplicate values

setCities = set(cities)
print(setCities)
print(len(cities))
print(len(setCities))

# .add()
scienceFi = {"Star Trek","Star wars","halo"}
scienceFi.add("mass effect")
print(scienceFi)
scienceFi.add("Star Trek")  #this item will not be added to the sets as sets are smart enough to ignore the duplicates
print(scienceFi)
scienceFi.remove("Star Trek")   #trying to remove the item that does not exists throws an error
print(scienceFi)
scienceFi.discard("Star Trek")   #discrd deletes the item if exists else graceflly handles the error and does not throw to user while remove throws error to user.
print(scienceFi)
scienceFi.clear()   #clears the complete set
print(scienceFi)


#.copy()
mountains = {"Everest","Kilimanjaro","Fuji"}
set2 = mountains.copy()

print(set2 is mountains)    #though the copy is made sets are going to be treated different hence returns false.

#.union()
set1 = {1,2,3,4,5,6,7}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)     #regular union operation.
set4 = set1 | set2           #another way to perform union
print(set3)    
print(set4) 

#.intersection()
setIntersection = set1.intersection(set2)   #gets the common values in both the sets. 
setIntersection1 = set1 & set2              #another way to perform intersection
print(setIntersection)
print(setIntersection1)


#.subraction() and .difference()
subtraction1 = set2-set1    #gets the unique values in set 2
subtraction2 = set1-set2    #gets the unique values in set 1
differenceSet = set1.difference(set2)   #another way to perform subtraction
differenceSet1 = set2.difference(set1)  #another way to perform subtraction

print(subtraction1)
print(subtraction2)
print(differenceSet)
print(differenceSet1)


#Set Comprehensions
setComprehention = {even+2 for even in range(2,20,2)}   #Note there should be no spaces in the math operation even+2
print(setComprehention)

setComprehention1= {char.lower() for char in "ALLCAPS"}
print(setComprehention1)