#Generic Import
import random
print("Usint Generic Import : "+str(random.randint(1,100)))


#Function Import
from random import randint
print("Usint Function Import : "+str(randint(25,75)))


#Universal Import
from random import *
print("Usint Universal Import : "+str(randint(50,60)))