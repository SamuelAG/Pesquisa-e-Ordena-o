import timeit
import itertools as it

def selectionSort(arr):
    
    lenght = len(arr)
    for i in range(lenght-1):
        minIdx = i

        for j in range(i+1, lenght):
            if arr[j] < arr[minIdx]:
                minIdx = j	
                
        if minIdx != i:
            arr[minIdx], arr[i] = arr[i], arr[minIdx]
    


lista = [1, 2, 3, 4, 5, 6]

listaPermutacoes = list(it.permutations(lista,6))

tempos = []

for i in listaPermutacoes:
    tempos.append(timeit.timeit("selectionSort({})".format(listaPermutacoes), setup="from __main__ import selectionSort", number=10))
    
    
maxIndex = tempos.index(max(tempos))
minIndex = tempos.index(min(tempos))

print('maximo = ', maxIndex, 'minimo = ' , minIndex)
print(listaPermutacoes[maxIndex], listaPermutacoes[minIndex])
