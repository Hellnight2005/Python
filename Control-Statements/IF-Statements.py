# The if Statement executes the block of statements by using the logical expression. 
# Logical expression compares the data and it made the decision  based on the result of the comparison . 

#  If-Syntax:-
#     if<expression>:
#   statement 1
#   statement 2
#   .........


#  eg:-
num = 10
if num>5:
    print(num,"is greater than 5")
    num=-1
if num==-1:
    print(num,"is negative number")



#  If ..else-Syntax:-
#     if<expression>:
#        statement 1
#      .........
#     else:
#       statement 2

#  eg:-
num =20
if num%2==0:
    print("Number is divisible by 2")
else:
    print("number is not divisible by 2")


#  If ..else-Syntax:-
#     if<expression1>:
#        statement 1
#    elif<expression>:
#        statement 2
#      .........
#     else:
#       statement 2

# eg:-
money=int(input("Enter Amount :"))

if(money<1000):
    discount=money*0.100
    print("Discount",discount)
elif(money<500):
    discount=money*0.200
    print("Discount",discount)
else:
    discount=money*0.300
    print("Discount",discount)
print("Net payable:",money-discount)
