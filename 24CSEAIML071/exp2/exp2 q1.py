#DISPLAY SIMPLE INTREST AND COMPOUND INTREST
p=int(input("enter principle"))
t=int(input("enter the time "))
r=int(input("enter the rate of intrest"))
si=(p*t*r)/100
print(si)


#COMPOUND INTREST
amt=p*((1+r/100)**t)
ci=amt-p
print("the compound intrest is",ci)