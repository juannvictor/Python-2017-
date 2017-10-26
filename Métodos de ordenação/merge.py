def mergeSort(l):
    print("Lista desordenada:",l)
    if len(l)>1:
        mid = len(l)//2
        esquerda = l[:mid]
        direita = l[mid:]

        mergeSort(esquerda)
        mergeSort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                l[k] = esquerda[i]
                i += 1
            else:
                l[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            l[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            l[k] = direita[j]
            j += 1
            k += 1
    print("Lista ordenada por Merge:", l)

lista = [99, 44, 25, 4, 3]
print(mergeSort(lista))
            
