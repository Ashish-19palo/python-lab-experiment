#WAP to input 3 coefficient values and Find their real roots?
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"One real root (repeated): {root}")
else:
    print("The equation has no real roots (roots are complex).")
