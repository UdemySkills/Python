lowerCaseString = "there are no capital letters here."
upperCaseString = "THIS IS A SHOUTOUT."
print(lowerCaseString.upper())
print(upperCaseString.lower().upper())
print("isupper() of string returns true/false. does upperCaseString variable have all upper case chars ? : "+str(upperCaseString.isupper()))
print("isupper() of string returns true/false. does lowerCaseString variable have all upper case chars ? : "+str(lowerCaseString.islower()))
print("This is just a string".isalnum())
print("This is a string".startswith("t"))


#Other handy string functions are
#.isalpha() #only letters
#.isalnum() #only numbers and letters
#.isdecimal() #only numbers
#.isspace() #only spaces
#.istitle() #only titleCase
#.startswith() #checks the sequence of test startingwith and is case sensitive
#.endswith() #check the sequece of the text ending with and is case sensitive
#.join() #joins with the string the string.
#.split() #returns the split string

print("".join(["one","two","three"]))
print(" ".join(["one","two","three"]))
print(",".join(["one","two","three"]))
print(", ".join(["one","two","three"]))
print("...".join(["one","two","three"]))


print("Milk, Curd, Carrots, beetroot".split(" "))
print("Milk, Curd, Carrots, beetroot".split(","))
print("Milk, Curd, Carrots, beetroot".split(", "))
print("Milk, Curd, Carrots, beetroot".split(", "))

#.rjust() and .ljust()
print("hello world".rjust(15))   #15 indicates the length of string from left, hence after the length of the string whitespaces are added.
print("hello world".rjust(15,"*"))   #15 indicates the length of string from left, hence after the length of the string whitespaces are added. 
                                     #Second parameter is filler and can be only 1 char length
print("hello world".ljust(15,"*"))   #15 indicates the length of string from left, hence after the length of the string whitespaces are added. 
                                     #Second parameter is filler and can be only 1 char length
print("hello world".rjust(5))   #15 indicates the length of string from left, if the length is less than string, there is no impact to be seen
print("hello world".center(15,"*")) #By Default spaces are added at the begining and ending of the string to make the string center aligned
                                    #if the filler char is provided the same is considered instead of spaces.

#.strinp(), #removes all spaces from begining and ending
#.rstrip(), #removes all spaces from the end
#.lstrip() #removes all spaces from begining
print("                Python ROCKS !!!                ")
print("                Python ROCKS !!!                ".strip())
print("                Python ROCKS !!!                ".rstrip())
print("                Python ROCKS !!!                ".lstrip())
(print("\n\n\n"))
print("aaaaaa        Python ROCKS !!!       aaaaaa")
print("aaaaaa        Python ROCKS !!!       aaaaaa".strip("a"))
print("aaaaaa        Python ROCKS !!!       aaaaaa".rstrip("a"))
print("aaaaaa        Python ROCKS !!!       aaaaaa".lstrip("a"))
(print("\n\n\n"))
print("aaaaaa Python ROCKS !!! aaaaaa")
print("aaaaaa Python ROCKS !!! aaaaaa".strip("aaaaaa"))
print("aaaaaa Python ROCKS !!! aaaaaa".rstrip("aaaaaa"))
print("aaaaaa Python ROCKS !!! aaaaaa".lstrip("aaaaaa"))


#Important
print("juice, bread, cheese, vegetable, milk, bread".rstrip(",ed arb")) #the truncation happens for the first char that is identified in this case it is comma.
print("blueblueyellowblueeulb".strip("eulb")) #strip removes the characters from left and right as well.

#.replace takes 2 arguments 1st one the string to find, 2nd one the replacement string
print("Good Morning.".replace("Morning", "Evening"))

#.len()
print(len("this is a sample string"))
print(len("this is"+" a sample"+"Concatinated string"))

#programming Challange - String Reverser

regularString = "This is a regular string"
reversedString = ""
for item in range(len(regularString)-1,-1,-1):
    reversedString+=regularString[item]
print(reversedString)


#Programming Challange Word Counter
str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
 
 
# This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to
# the variable spaces_and_letters so that the number of words in it can by found by counting spaces between words.
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
 
 
print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))


#.format()
name = "Venkatesh"
degree = "BCA"
job = "Software Architect"
experience = "20 Years"
print(name+" Majored in "+ degree+" works as a "+job+" and has "+experience+" in the industry")
print("{} majored in {}, works as a {} and has {} of experience".format(name, degree, job, experience))
