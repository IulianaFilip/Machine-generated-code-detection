def iquicksort(L):
    if len(L) <= 1:
        return L
    pivot = L.pop()
    left = []
    right = []
    for n in L:
        if n <= pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
    return iquicksort(left) + [pivot] + iquicksort(right)