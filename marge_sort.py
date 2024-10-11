def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    
    for i in range(n1):
        L[i] = a[p + i]
    for j in range(n2):
        R[j] = a[q + 1 + j]

    
    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


a = [12, 11, 13, 5, 6, 7]
merge_sort(a, 0, len(a) - 1)
print("ordenado:", a)
