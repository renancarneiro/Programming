#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for x in range(0,5):
    n = int(input('Digite um valor: '))
    #Primeiro numero
    if x == 0:
        print('Adicionando o primeiro valor da lista...')
        lista.insert(0,n)
    #Segundo numero
    if x == 1:
        if n <= lista[0]:
            print(f'Adicionando {n} na primeira posição')
            lista.insert(0,n)
        else:
            print(f'Adicionando {n} na posição 1')
            lista.insert(1,n)
    #Terceiro numero
    if x == 2:
        if n < min(lista):
            print(f'Adicionando {n} na primeira posição')
            lista.insert(0,n)
        elif n >= min(lista) and n <= max(lista):
            print(f'Adicionando {n} na posição 1')
            lista.insert(1,n)
        else:
            print(f'Adicionando {n} na última posição')
            lista.insert(2,n)
    #Quarto numero
    if x == 3:
        if n <= min(lista):
            print(f'Adicionando {n} na primeira posição')
            lista.insert(0,n)
        elif n >= min(lista) and n <= lista[1]:
            print(f'Adicionando {n} na posição 1')
            lista.insert(1,n)
        elif n >= lista[1] and n <= max(lista):
            print(f'Adicionando {n} na posição 2')
            lista.insert(2,n)
        else:
            print(f'Adicionando {n} na último posição')
            lista.insert(3,n)
    #Quinto numero
    if x == 4:
        if n <= min(lista):
            print(f'Adicionando {n} na primeira posição')
            lista.insert(0,n)
        elif n >= min(lista) and n <= lista[1]:
            print(f'Adicionando {n} na posição 1')
            lista.insert(1,n)
        elif n >= lista[1] and n <= lista[2]:
            print(f'Adicionando {n} na posição 2')
            lista.insert(2,n)
        elif n >= lista[2] and n <= max(lista):
            print(f'Adicionando {n} na posição 3')
            lista.insert(3,n)
        else:
            print(f'Adicionando {n} na última posição')
            lista.insert(4,n)
print('Os valores digitados em ordem foi: ',lista)
        
    
