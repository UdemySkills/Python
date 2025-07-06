celsius = float(input("Enter the Celsius Temperature to convert to Fahrenheit : "))

def ConvertToFahrenheitRound(celsius):
    return (round(1.8*celsius,1)+32)


print("using Round() : "+str(celsius)+" in Fahrenheit is : " +str(ConvertToFahrenheitRound(celsius))+".")

def ConvertToFahrenheitManual(celsius):
    return(((18*celsius)+320)/10)


print("using ManualCalculation :"+str(celsius)+" in Fahrenheit is : "+str(ConvertToFahrenheitManual(celsius))+".")
