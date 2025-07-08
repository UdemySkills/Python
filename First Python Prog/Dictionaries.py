#Simple Dictionary

#NOTE : Dictionaries are reference types.

console = {"Name":"Venkatesh",
           "Age":"forever 24"}
print(console)
print(console["Name"])

dictValExtracted = console["Age"]
print(dictValExtracted)

#Dictionaries can be of any data type
#Dictonaries are not ordered / un ordered
floatsDict = {1.1:100, 2.34:899, 3.09:6976}
mixedDict = {"string":1,1234:2,4.856:3,False:4}
randomDict1 = {9:"abc",10:"xyz"}


#Dictionaries unordered example 
#Meaning the data in the dictonary is compared but not at the same position (position indipendent data comparision)
dict1 = {1:0.1, 2:0.2}
dict2 ={2:0.2,1:0.1}
print(dict1 == dict2)
print(dict2[1])     #1 is the kne not index
print(1 in dict1)   #1 is the key not index

#.keys(), .values(), .items() and .get() functions

personDetail = {"Name":"Venkatesh",
               "Age":"24 forever",
               "Location":"Entire World",
               "Profession":"Anything and Everything"}

print(personDetail.keys())
for a in personDetail.keys():
    print(a)

print(personDetail.values())
for value in personDetail.values():
    print(value)

print(personDetail.items())
for item in personDetail.items():
    print(item)

for key,value in personDetail.items():
    print("The Key : "+key+" ---- has Value : "+value)

for key,value in personDetail.items():
    print(key,value)


print(type(personDetail.keys()))        #type() gets the data type of the return type of the object / function / method passed as parameter
print(type(personDetail.values()))
print(type(personDetail.items()))

print(list(personDetail.keys()))        #converts the data to type list
print(list(personDetail.values()))
print(list(personDetail.items()))

#using in and not in 
print("Name" in personDetail.keys())
print("venkatesh" in personDetail.values())     #like in any other case even values in dicts are case sensitive
print("Quality" not in personDetail.keys())

if "Name" in personDetail:
    print(personDetail["Name"])
else:
    print("Key not found")

print(personDetail.get("Age","No Age Found"))   #the first parameter for the get method is the key and the 
                                                #second parameter is the value to return if the value is not found, if found returns value for the key.

print(len(personDetail))    #displays the number of key value pairs in the dictionary.



#fromKeys(), pop() and popitem()
print(personDetail.fromkeys(["Name"],"Venkatesh"))  #first parameter is key which can be a list.

ex1 = {}.fromkeys("address","RiverchaseTrail Alabama NE")   #note when using fromKeys if the string in keys parameter has repated chars,
print(ex1)                                                  #python considers those only once and the following ones are omitted

ex2 = {}.fromkeys(["None"],)    #when the second argument is not provided, from key uses none as the default second argument.
print(ex2)


#pop is the same like in list, except that you need to provide the key to remove 
ex3 = {"Make":"Honda", "Model":"Civic", "Year":2025}
print(ex3)
poppedVariable = ex3.pop("Model")
print(poppedVariable)

#popitem removes the last item from the Dictionary

poppedItem = ex3.popitem()
print(poppedItem)


#.clear(), .copy() and .update()
trialDictionary ={"Name":"Venkatesh",
               "Age":"24 forever",
               "Location":"Entire World",
               "Profession":"Anything and Everything"}
nationality = {"BirthCountry":"India", "CurrentLivingCountry":"USA"}


copiedTrialDictionary = trialDictionary.copy()      #Deep copy as by default dictionaries are reference types
copiedTrialDictionary["Name"] = "Venkatesh Ellur"
print(trialDictionary)
print(copiedTrialDictionary)

trialDictionary.update(nationality)     #The Sorce Dictionary is appened with the dictionary passed as parameter
                                        #Note : if there is duplicate keys, the one in source is overwritten with the the one coming from the parameter
print(trialDictionary)
trialDictionary.clear() #just clears the dictionary and takes no arguments
print(trialDictionary)


#.setdefault(), .dict()
#setdefault() is used to set a default key in case does nto exist
computers = {"google":"chromebook","apple":"mac","microsoft":"surface"}
if "lenovo" not in computers:
    computers["lenovo"] = "thinkpad"

print(computers)

computers.setdefault("samsung","galaxy")    #if not found, it will add the key and value, NOTE : if the key already exists it will not overwrite
print(computers)

computers.setdefault("google","chbk")       #in this case the setdefault does no impact as the value already exists for the key.
print(computers)

#.dict()

empty = dict()
withValues = dict(Name="Venkatesh",
                  Age="24")   #NOTE : no space after the key or = or value
print(withValues)