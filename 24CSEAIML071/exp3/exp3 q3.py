
#greatest of three numbers
a = int(input("enter first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
if(a>b and a>c):
    print("the greatest is a",a)
elif(b>a and b>c):
    print("the greatest is b",b)
else:
    print("the greatest is c",c)
            