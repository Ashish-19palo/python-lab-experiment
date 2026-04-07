#write a program to swap two numbers by using third variable
def swap_numbers(a, b):
    # Print original values
    print(f"Original values: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"Swapped values: a = {a}, b = {b}")
    return a, b
num1 = 5
num2 = 10
swap_numbers(num1, num2)
