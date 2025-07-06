ex_var = 5
ex_var = ex_var +7
floatExVar = 4.589
boolExVar = True

print("hello world")
print("when displaying the math operation / different datatype with the string str() method must be used as below.")
print("Simple Int variable value is : "+str(ex_var))
print("Floating value is : "+ str(floatExVar))
print("Boolean value is : " + str(boolExVar))
print("Addition : " + str(5+4))
print("Subtraction : " + str(5-4))
print("Multiplication : " + str(5*4))
print("Division : " + str(5/4))
print("Addition : " + str(5+4))
print("Exponentiation : " + str(5**4))     #5*5*5*5
print("Floor Division : " + str(16//5))    #Return the wholenumber of the division result and ignores the decimal
print("Modulo : " + str(5%4))              #reminder of the division
print("Python follows BODMAS")

# Dealing with decimals in python
print(1.23+2.80)    #Python has errors while using float or decimal types for aerthamatic operations. Solution avoid using float / decimal and use integers and perform workaround as belwo

alternateToDecimals = (123 + 280) / 100 #using this approach instead of adding 1.23+2.80
print("Alternate approach to use math op for decimals : " + str(alternateToDecimals))

secondAlternate = (1.23 + 2.80) 
print("Second Alternate approach to use math op for decimals : "+ str(round(secondAlternate,2)))
