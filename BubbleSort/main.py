from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def bubbleSort(arr):
	count = 0
	lenght = len(arr)
	for i in range(lenght):
		for j in range(lenght-i-1):
			count+=1
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return count

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

mpl.use('Agg')


def desenhaGrafico(x, y, fileName, labely, labelx):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x, y, label = "BubbleSort")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(labely)
	plt.xlabel(labelx)
	fig.savefig(fileName)
 
x = [10000, 20000, 30000, 40000, 50000]
y = []

swaps = []

for i in range(5):
	lista = geraLista(x[i])
	swaps.append(bubbleSort(lista))
	y.append(timeit.timeit("bubbleSort({})".format(lista), setup="from __main__ import bubbleSort", number=1))



desenhaGrafico(x, y, 'grafico_bubble', 'Tempo', 'Quantidade')
desenhaGrafico(x, swaps, 'grafico_comparacoes', 'Comparacoes', 'Quantidade')
print(swaps)
