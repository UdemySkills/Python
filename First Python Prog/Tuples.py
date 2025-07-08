#Tuples can contain same data type or different datatypes
#Tuples can contain duplicate values.
#Tuples are immutable
#Tuples are used when we need a static data which would never chage
#Tuples takes up less memory.

#1st way to create tuple
tuple1 = ("a","b","c","d","e")
tuple2 = (2.45, False, [1,2,3,4])
tuple3 = (1,1,2,3,5,6,6,6,)

print(tuple1)
print(tuple2)
print(tuple3)

#2nd way to create a tuple
#tuple4 = tuple("asdfs","asdfsadf","asdfsaf")    #not allowed
tuple4 = tuple("abcdefghijklmnop")     #when string is passed each char will be taken as 1 tuple item.
tuple5=tuple([2.34, 4.234, 10,5])
tuple6 = tuple({"a":1, "b":"asdf", "c":"aaaa"})     #Dictionaries can be used in tuples, but no point as the values will be omitted and just keys will be considered
tuple8 = (1,2,3,4,5,6,7,8,9,10)         #Tuples can be accessed using index

print(tuple4)
print(tuple5)
print(tuple6)
print(tuple4[5])        #Tuple items can be accessed using indexes and can be sliced as well.
print(tuple4[:4])
print(tuple4[2:5])
print(tuple4[6:])


tupleT = (1,2,3)        #Tuples take up less memory than dictionaries or lists
listL = [1,2,3]
dictD = {1:1,2:2,3:3}
print(tupleT.__sizeof__())
print(listL.__sizeof__())
print(dictD.__sizeof__())


#Looping through Tuples

majorCities = ("Tokyo","London","Paris","Bangalore","NewYork","Sydney","Singapore")

for item in majorCities:
    print(item)

count = 0
while count < len(majorCities):
    print (majorCities[count])
    count +=1


#Tuple Step()       #when 3 parametr
inits = (1,2,3,4,5,6,7,8,9,10)  
print(inits[::3])    #takes first 3 chars as the start and end is not provied [startIndex:endindex:increment]
print(inits[1::2])
print(inits[7::-1])
print(inits[8::-2])     
print(inits[1:7:2])

#Tuple methods 
nested = (1,2,3,(4,5,6),(7,8,9),(10,11,12,13))  #nestedTuples
print(nested)
print(nested[4])
print(nested[5][2]) #accessing nested tuple and an item in the nested tuple

#count() and index()
repeat =(1,1,1,2,3,4,5,6,6,6,8,9,10)
print (repeat.count(7))
print (repeat.count(6))
print (repeat.count(3))

print("Below statement prints the index of the value provided in the tuple")
print(repeat.index(1))
print(repeat.index(9))