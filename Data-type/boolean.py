# The bool data type is built-in type .
# it represents the truth values like True and False .
# python prog to illustrate built-in method bool().

# return False as X is not egual to Y 
x=3
y=13
print(bool(x==y))

# Return Fasle as x is None 
x= None
print(bool(x))

# return False as x is an empty sequence 
x=()
print(bool(x))

# return False as x is an empty mapping 
x={}
print(bool(x))

# Return Fasle as x is 0 
x=0.0
print(bool(x))

# Return True as x is a non empty SyntaxWarning 
x= 'Abhijeet'
print(bool(x))