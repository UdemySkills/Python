exStrings = "Strings can be declaried using either single quote or double quotes like in JavaScript"
print(exStrings)
print("Accessing the Char in the string using index : "+str(exStrings[0]))

#string Slicing to access substring
print("1st Approach of stringSlicing : "+ exStrings[:7])   #  (start point empty indicates begining of the string index which is 0) 0 to 7 chars
print("1st Approach of stringSlicing : "+ exStrings[8:11])   #  start index and closing index this gives 3 chars "can"
print("1st Approach of stringSlicing : "+ exStrings[8:])   #  (End point empty indicates begining of the string index which is the end of the string ) 8 to complete string

firstName = "Venkatesh"
spouse = "Deepika"
print (firstName+ " "+spouse)