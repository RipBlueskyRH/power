a=int(input("enter a number: "))
b=int(input("enter an exponent: "))
print("the answer is ", a**b)


a=int(input("enter a number: "))
b=int(input("enter an exponent: "))
c=1
for i in range (1, b+1):
    c=a*c
    print ("the answer is", c)