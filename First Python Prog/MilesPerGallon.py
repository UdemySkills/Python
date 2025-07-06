import random 
gallons = random.randint(10, 20)
miles = random.randint(200,400)

def GetEconomy(gallons, miles):
    return (miles/gallons)


print(str(gallons)+" Gallons of fule can drive you "+str(GetEconomy(gallons,miles))+" Miles.")