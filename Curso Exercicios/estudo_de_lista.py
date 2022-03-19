#Estudo de listas
lista = [1,2,3,4,5]
#adicionar elemento a lista
lista.append(6)
print(lista)
#adicionar um novo elemento na posição 0
lista.insert(0,8)
print(lista)
#deletar elemento
del lista[3]
lista.pop[3]
lista.remove[3] # remove o primeiro numero 3 que aparecer
lista.pop() <- apaga o ultimo elemento
print(lista)
#criar uma lista usando list()
valores = list(range(4,11)) 
print(valores)
#inverte a ordem dos numeros
valores.sort(reverse=True) 
print(valores)
#criar um for com inputs em uma lista
valores = list()
for x in range(0,5):
valores.append(int(input('Digite um numero')))
#printa a lista com suas respectivas posições
for c, i in enumerate(valores):
print(f'A posição do numero "{i}" é {c+1}')
#essa forma cria uma copia da lista
a = [2,3,5,6,8]
b = a[:] 
b[2] = 4
print(a)
print(b)
