word = "Deepika is Amazing"

for char in word:
    print(char)


#Find number of characters in the string

countOfChars=0
for char in word:
    countOfChars +=1

print(countOfChars)


#Range example

oneInput = range(5)

for num in oneInput:    #prints number from 0 to 4 range(0, end/length)
    print(num)

twoInputs = range(5,11)
for num in twoInputs:   #prints numbers from 5 to 10 range(start, end) 
    print(num)


threeInputs = range(1,20,3)
for num in threeInputs:     #prints numbers from 1 to 20 incrementing by 3 range(start, end, incrementor / add this value to previous value)
    print(num)