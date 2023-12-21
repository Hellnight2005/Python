# A set is nothing but the unordered collection of the items or elements .
# the use of set is done to deal with set theory .
# Which mathematical operation like union, difference, intersection and symmertic different.
# set are also used to eliminate duplicate entries. 

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
b=[ 9, 8, 6, 5, 4, 3, 2, 1, 11, 12, 13]
x=set(a) 
y=set(b)
print(x)
print(y)
print("Abhijeet")
# It print union betwwen X and Y 
print(x|y)
# It will print different between x and y 
print(x^y)
#  It will print missing number 
print(x-y)