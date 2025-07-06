score = int(input("Provide the score obtained. "))

def getGrade(score):
    if (score >= 90):
        return "A"
    if(score >= 80 and score <90):
        return "B"
    if(score >=70 and score < 80):
        return "C"
    if(score >=60 and score < 70):
        return "D"
    else:
        return "F"
        

print ("Using general if Condition : For the secured score of "+str(score)+ " you get "+getGrade(score)+" Grade")


def getGradeUsingElif(score):
    if(score >= 90):
        return "A"
    elif(score >= 80 and score <90):
        return "B"
    elif(score >=70 and score < 80):
        return "C"
    elif(score >=60 and score < 70):
        return "D"
    else:
        return "F"


print ("Using general elif Condition : For the secured score of "+str(score)+ " you get "+getGradeUsingElif(score)+" Grade")