#write a program to Find the area & perimeter of triangle? 
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c
s = perimeter / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Perimeter:", perimeter)
print("Area:", area)
