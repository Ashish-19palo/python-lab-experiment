#Accept a digit within O to 6 & display the week day such as 0 as sunday and 1 For monday?
n = int(input("Enter a number (0-6): ")) # Corrected input syntax

if (n == 0):
    print("Sunday")
elif (n == 1):
    print("Monday")
elif (n == 2):
    print("Tuesday")
elif (n == 3):
    print("Wednesday")
elif (n == 4):
    print("Thursday")
elif (n == 5):
    print("Friday")
elif (n == 6):
    print("Saturday")
else:
    print("Invalid Input")
