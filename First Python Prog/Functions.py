def py_function():
    print("Python is ")
    print("a Hero")


print("This code is not considered as part of the function as this does not have a tab space")

py_function()
py_function()



#defining a function

#def says it is a function
#name with (): after def says it is a name given to the function
#the function code must mandatorily start after a tab space in order for python to know it is the code belonging to the function.
#Leave atleaset 2 lines of gap after the end of the function code this is the guideline, if 2 line space is not left there is no issue or error.
#NOTE : Functions must be defined first and then called later as this is sequential.


def py_Function1(parameter):
    print(parameter+2)

py_Function1(8)


def py_Function2(p1, p2, p3):
    print(p1+str(p2)+p3)

py_Function2("The Number ", 5 ," is an integer.")


#Default values for parameters
def py_Function2(p1, p3, p2=5): #like in c# we just assign the value to the parameter to make it a default valued parameter.
    print(p1+str(p2)+p3)

py_Function2("The Number "," is an integer.")


#return from method
def py_FuncReturn(num1=5, num2=2):
    return (num1*num2)

returnValue = py_FuncReturn() + 10
print ("Value returned from function and added another 10 to it : "+str(returnValue))