#including the input in the int / float functions to get those specific datatypes while reading input from the user.

userInt = int(input("Please enter an integer."))
print("You have entered '"+str(userInt)+"' and its datatype is "+str(type(userInt)))

ex1 = int(11.9) #takes the nearest integer that is <= Float / decimal value
print("This case the nearest integer value is taken : "+str(ex1))

ex2 = int(11.9+12.3)
print("Even in This case the nearest integer value is taken : "+str(ex2))

#Error Cases
#int("1.59")    String that is a float value passed to int method throws error.
#int("10.1+9.3")    String that is an expression throws an error.


userFloat = float(input("Please enter a float value."))
print("You have entered '"+str(userFloat)+"' and its datatype is "+str(type(userFloat)))

ex3 = float(4)
print("You have entered '"+str(ex3)+"' and its datatype is "+str(type(ex3)))

ex4 = float(4+5)
print("You have entered '"+str(ex4)+"' and its datatype is "+str(type(ex4)))

ex5 = float("4")
print("You have entered '"+str(ex5)+"' and its datatype is "+str(type(ex5)))

#Error Cases
#Float(10+9) String that has an expression throws error
#Float("nub3rs 4and $ymbols") string of letters also throws error

