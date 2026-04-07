#WAP to test a stoing is palindoame or not ?
x = input("Enter a string: ")
if x == x[::-1]:
    print("Palindrome string")
else:
    print("Not a Palindrome string")