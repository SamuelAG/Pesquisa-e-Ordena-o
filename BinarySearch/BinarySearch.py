import timeit

def geraLista(tam):
    lista = []
    i = 0
    while i < tam: 
        lista.append(i)
        i+=1
    return lista

def buscaBinaria(lista, chave):
  inicio = 0
  fim = len(lista)
  
  while inicio <= fim:
    meio = (inicio + fim)//2
    if lista[meio] == chave:
      return meio
    elif lista[meio] > chave:
      fim = meio - 1
    else:
      inicio = meio + 1

  return -1

def buscaBinariaRecursiva(lista, inicio, fim, chave):
  if inicio > fim:
    return -1
    
  meio = (inicio + fim)//2

  if lista[meio] == chave:
    return meio
  elif lista[meio] > chave:
    return buscaBinariaRecursiva(lista, inicio, meio - 1, chave)
  else:
    return buscaBinariaRecursiva(lista, meio + 1, fim, chave)

def buscaSequencial(lista, chave):
  i = 0
  tam = len(lista)
  while i < tam:
    if lista[i] == chave:
      return i
    i+=1
  return -1

# Problema Soma das casas, https://www.urionlinejudge.com.br/judge/pt/problems/view/2422
# resolver com força bruta, depois com busca binária e comparar os resultado 


bb = timeit.timeit("buscaBinaria({}, {})".format(geraLista(1000000), 733338),setup="from __main__ import buscaBinaria",number=100)
bbr = timeit.timeit("buscaBinariaRecursiva({}, {}, {}, {})".format(geraLista(100000), 0, 10000, 73338),setup="from __main__ import buscaBinariaRecursiva",number=100)
bs = timeit.timeit("buscaSequencial({}, {})".format(geraLista(1000000), 733338),setup="from __main__ import buscaSequencial",number=100)

print("Busca binária iterativa: ", bb)
print("Busca binária recursiva: ", bbr)
print("Busca sequencial: ", bs)