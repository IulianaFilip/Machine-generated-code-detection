def fquicksort(L):
    print(L)
    if len(L) == 0:
        return []
    else:
        pivot = L.pop()
        S = quickapi(L,pivot,[],[])
        return fquicksort(S[0]) + [pivot] + fquicksort(S[1])

def quickapi(L,p,left,right):
    print(L,left,right)
    if len(L) == 0:
        return [left,right]
    else:
        if L[0] < p:
            left.append(L[0])
        else:
            right.append(L[0])
        return quickapi(L[1:],p,left,right)

L = [3,7,2,5,8,4,9,1,6]

print(fquicksort(L))