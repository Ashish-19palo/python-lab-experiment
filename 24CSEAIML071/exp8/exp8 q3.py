n = input("enter a paragrapgh : ")
l = n.split()
print("the paragraph contains", len(l),"words .")
count = 0
for i in l:
    if i == i[::-1]:
        count = count+1
print("pallindrome = ", count)
print("printing the words in reverse order :-")
for i in l:
    print(i[::-1])
