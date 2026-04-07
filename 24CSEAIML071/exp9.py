#1
def add(a,b):
    return a+b

res = add(3,4)
print(res)
#2
def product(x,y):
    print("product=",x*y)

product(4,6)

#3
def display(name,age):
    print(name,age)

display(age=20,name="amit")
#4
def student(name,course):
    print("name:", name)
    print("course", course)

student(course = "python",name = "amit")
#5
def greet(name="student"):
    print("hello",name)

greet()
#6
def bill(amount=100):
    print("bill amount:",amount)

bill(500)
bill()

#8
def total(*nums):
    print("sum=",sum(nums))

total(10,20,30)

#9
def employee(**details):
    for k, v in details.items():
        print(k,":",v)
    
employee(name="amit",id=101,dept="it")

#10
l = [1,2,3,4,5]
l1 = list(map(lambda n : n * n , l))
print(l1)

#11
l1 = [1,2,3,4,5]
l2 = [5,10,15,20,25]
l3 = list(map(lambda x,y : x*y ,l1,l2))
print(l3)
