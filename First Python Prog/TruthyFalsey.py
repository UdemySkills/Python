stringExample = input("please enter some string other than empty value. ")

if stringExample:
    print("Good job you understood the seriousness of it.")
else:
    print("Very bad that you do not understand the seriousness of it.")


varInt = -10 #any value apart from 0 is truthy 
if varInt:
    print("Good try varInt is truty")
else:
    print("varInt is falsey")


print("(bool(0) is"+str(bool(0)))
print("(bool(10) is "+str(bool(10)))
print("(bool(-10) is "+str(bool(-10)))
print("(bool(-10.123) is "+str(bool(-10.123)))
print("(bool(\"\") is "+str(bool("")))
print("(bool(\"Cool\") is "+str(bool("Cool")))