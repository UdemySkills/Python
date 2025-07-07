#All lists below are valid ones.

exList1 = [1,2,3,4,5]
exList2 = [2.15, 9.16]
exList3 = ["white","Blue","Black","Green"]
exList4 = [True, False, True, True, False, True]
exList5 = [[1,2,],[5,6,8,],[1,4,7,8],[9,5,8,7,4,2,6]]   #this kind of lists are called list of lists.
exList6 = [10,13.4, "tree",True,[1,7,8,5]]

print(list("sometext"))

#in and not in operators
checkedList = [1,2,3,4,5]
oneExistsInList = 1 in checkedList
TenNotExistsInList = 10 not in checkedList
print(oneExistsInList)
print(9 in checkedList)
print(TenNotExistsInList)


#Indexs and List Slicing

indexesExample1 = ["carpet","Hardwood","linoleum"]
print(indexesExample1[2])
print(indexesExample1[2][0])

indexesExample2 = [[1,2,],[5,6,8,],[1,4,7,8],[9,5,8,7,4,2,6]]
print(indexesExample2[1])
print(indexesExample2[1][0])

indexesExample3 = [1,2,3,4,5]   #negetive indexes still work do not throw error
print(indexesExample3[-1])
print(indexesExample3[-2])
print(indexesExample3[-3])
print(indexesExample3[-4])
print(indexesExample3[-5])
#print(indexesExample3[-6])  #Negetive index can go only up to the length of the list size hence all lines from here throw error
#print(indexesExample3[-7])
#print(indexesExample3[-8])
#print(indexesExample3[-9])
#print(indexesExample3[-10])

mixed = [False, 5, 6.98, "this is a string"]
print(mixed[2]+1.76)
print("I have used \""+mixed[-1]+"\"as an example too many times.")
#print("I have used \""+mixed[-2]+"\"as an example too many times.") #string convertion must be done in this case.

#List slicing

sliced = [0,1,2,3,4,5,6,7,8,9]
print(sliced[:4])   #startIndex and endIndex empty start index indicate beginning of the list
print(sliced[3:9])
print(sliced[6:])   #startIndex and endIndex empty end index indicate the end of the list


#Reassigning a list's items
reAssign = [0,1,2,3,4,5]
print(reAssign)
reAssign[4] = 10    #number in square bracket indicates index
print(reAssign)
reAssign[0:3] = [1,2,3] #numbers in the first square brackets indicates startindex and endindex, on the right hand side are the new replacement values.
print(reAssign)
reAssign[5:5] = [11]    #the reassigning is capable of increasing the length of list, meaning the index provided can be greater than the length.
print(reAssign)
reAssign[15:15] = [11]  #When providing the index number beyond the last+1 by default python takes last+1 index.
reAssign[7:15] = [11,12,13]  #When the start and end index is higher than the values provided, python is smart enough to just consider the values provided and ignore the rest of the positions.
print(reAssign)     
reAssign[10:11] = [11,12,13,14,15]  #Python, gives priority for the values provided and the start index, end index looks to have less priority.
print(reAssign)     



#del statements and list methods
planets = ["Mercury","Venus","Earth","Mars","Urenus","Jupiter","Saturn","Neptune","Pluto","Carla"]
print(planets)
del planets[-1] #hard delete and the index of the following elements will be rest if the element is removed from 0 to last but 1 index
print(planets)
#planets.remove("pluto") #the values are case sensitive, hence no item removed and error displayed
planets.remove("Mercury") #
print(planets)
planets.append("Carla")
print(planets)
planets.insert(0,"Mercury")
print(planets)
planets.sort()
print(planets)
planets.sort(reverse=True)
print(planets)

mixedSort = [True,1,3.6,"Abc", "Amazing",["try","this","out"],["lets see what happens"]]
#mixedSort.sort()    #Sorting is not allowed for mixed types
#print(mixedSort)

boolAndNumericType = [False,-2,-8,5,6.9]
boolAndNumericType.sort()   #Sorting can be done on the numeric types along with bool
print(boolAndNumericType)


#ASCIIbetical Order.
ASCIIbeticalList= ["Kishan","Pranav","Deepika","Venkatesh","Ellur","alpha","Alpha","Beta","beta","yulu","Zulu"]

#.index()   #gets the index of the item, in case of repeated items the index of the item first found is returned
print(ASCIIbeticalList.index("Alpha"))  #index() is case sensitive
print(ASCIIbeticalList.index("alpha"))

ASCIIbeticalList.sort() #Sort always goes by ASCIIbetical Order i.e Capital letters comes first and then comes the lower case letters.
print(ASCIIbeticalList)
ASCIIbeticalList.sort(key=str.lower) #This key ignores the case and gives the results in actual alphabatical order.
print(ASCIIbeticalList)


poppedItem = ASCIIbeticalList.pop()
print(poppedItem)
poppedByIndex = ASCIIbeticalList.pop(-1)
print(poppedByIndex)