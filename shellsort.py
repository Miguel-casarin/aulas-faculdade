a = []

n = len(a)
gap = n / 2

j = (gap + 1)

while gap > 0:
    for j in range(n):
        key = a[j]
        i = j - - gap
        while (i > 0) and (a[j] > key):
        a[i + gap] = a[i]
        i = i - gap
        a[i + gap] = key
    gap = gap / 2         
    

