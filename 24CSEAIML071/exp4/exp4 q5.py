num = int(input("Enter a positive integer: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits is:", sum_digits)
