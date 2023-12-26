# A function is piece of code that performe specified purpose has its own scope and is referred to by name 
# All function may hav Zero or no or more than one parameter. 

# there are two type of function mainly us 
# 1) built-in function :- it is created by system the user can not write it it only has read avaible
# 2) User-define function :- it created by user for reapeted task it can use muliptly
# "def" Keyworld is use for define function 

def PrintString(string):
    return print(string)

PrintString("Abhijeet")


def AreaOfCircle(r):
    A= 2*3.14*r*r
    return A

a=int(input("Enter radius of circle"))
b=AreaOfCircle(a)
print(f"Area of circle is {b}")