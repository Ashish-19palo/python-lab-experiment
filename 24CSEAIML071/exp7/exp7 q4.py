def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    
num = int(input("enter a number:"))
result = factorial(num)
print("the factorial of the num,ber is", result)


