m = int(input("enter the starting of natural numbers "))
n = int(input("enter the ending of natural numbers"))
print("the prime numbers are:")
for i in range(m,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i, end=" , ")