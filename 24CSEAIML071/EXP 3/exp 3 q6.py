#write a program to check whether a character is vowel or consonant
x = input("Enter an alphabet")
if x.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")