exampleString = "exampleString is Globally scoped variable "

def locScopeExample():
    exampleString = "where as exampleString is Local to the Function"
    return exampleString

print(exampleString)
print(locScopeExample())

#Local Variables cannot be used in global scope, meaning a variable defined in a function cannot be use outside the function.
#Global variables can be accessed in the local scope by passing them as parameters, meaning globally defined variables can be used in the defined functions.
#Based on the assignment done to the variable Python understand if the definition is global or local
    #in the above example Python understands that those are 2 different variables as the assignment is done.
    #The local variable of a function cannot be accessed in another function. The scope of the variable declaration stays to the function in which it is declared.
    #The same variable names can be used as far as the scopes are different.



exampleString = "exampleString is Globally scoped variable "

def locScopeExample(exampleString):
    exampleString = exampleString + "where as exampleString is Local to the Function"
    return exampleString

print(exampleString)
print(locScopeExample(exampleString))
print(exampleString)



#using the Global Statement the global variables can be accessed in the local scope
fruit = "Apple"

def ChangeFruitName(newFruitNAme):
    global fruit
    fruit = newFruitNAme
    print(fruit)
    
print(fruit)
ChangeFruitName("Pear")
ChangeFruitName("Mango")
print(fruit)