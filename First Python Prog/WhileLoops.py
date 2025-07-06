counter = 0

while counter < 5:
    counter += 1
    print(counter)



#Programming challange
# Tried to get more concepts included in this tiny program. :) 

intVal = int(input("Enter a +ve Number to get the total till 1."))
localVal = 0

def getTotal(intVal):
    global localVal
    while intVal > 0:
        localVal += intVal
        intVal -= 1
    #return localVal
getTotal(intVal)
print (localVal)
