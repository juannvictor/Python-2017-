lista = [99, 44, 25, 4, 3]

def bubbleSort(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
    return l

print(bubbleSort(lista))
