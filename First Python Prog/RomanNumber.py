from random import randint
intVar = randint(1,10)

def GetRomanNumber(intVar):
    if (intVar == 10):
        return "X"
    elif(intVar == 9):
        return "IX"
    elif(intVar == 8):
        return "IIX"
    elif(intVar == 7):
        return "VII"
    elif(intVar == 6):
        return "VI"
    elif(intVar == 5):
        return "V"
    elif(intVar == 4):
        return "IV"
    elif(intVar == 3):
        return "III"
    elif(intVar == 2):
        return "II"
    elif(intVar == 1):
        return "I"


print("The Roman number for the randomly generated Digit "+str(intVar)+ " is "+GetRomanNumber(intVar))