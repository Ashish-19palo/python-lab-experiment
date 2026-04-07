m = int(input("enter the starting of natural number"))
n = int(input("enter thwe ending of natural numbers"))
l = [ x for x in range(m,n+1)]
print("the sum of the list is :-",sum(l))
print("the average of the list is:",(sum(l)/len(l)))
print("the largest element is:", max(l))
print("the smallest element is:", min(l))
l2 = [x for x in l if x%3!=0]
print("the element which are not divisible by 3 are:", l2)

