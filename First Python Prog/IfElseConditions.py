
# Simple if Condition.
veg = input("Type vegetable name.")
if veg == "corn":
    print(str(veg=="corn")+" The a Vegetable is "+veg)
else:
    print("The Vegetable "+veg+" is not Corn.")


#Nested Condtions
gpa = 4.8
instantApproval = "Y"

if (gpa >= 3.7):
    if(instantApproval == "Y"):
        print("The application qualifies for a low APR student loan.")
    else:
        print("Not Qualified.")
else:
    print("Not Qualified.")
