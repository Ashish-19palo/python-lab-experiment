def recursive_min(L):
    if len(L)==1:
        return L[0]
    else:
        m = recursive_min(L[1:])
        return L[0] if L[0]<m else m
print(recursive_min([4,2,9,1,5]))
