lista = [99, 44, 25, 4, 3]

def InsertionSort(l):
    i = 1
    for i in range(len(l)):
        d = l[i]
        j = i - 1
        while (j >= 0) and (l[j]>d):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = d
    return l

print(InsertionSort(lista))
