numbers = []   # empty list

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# remove duplicates using set
unique_numbers = list(set(numbers))

# sort in ascending order
unique_numbers.sort()

print("List after removing duplicates and sorting:")
print(unique_numbers)
