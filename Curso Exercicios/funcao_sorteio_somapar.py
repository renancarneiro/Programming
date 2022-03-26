#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
#segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
def sorteio():
    cont = 0
    numeros = []
    while cont != 5:
        n = randint(1,10)
        if n not in numeros:
            numeros.append(n)
            cont+=1
    print(f'A lista sorteada foi {numeros}')
    return numeros
        
def somaPar(lst):
    soma = 0
    for x in lst:
        if x % 2 == 0:
            soma+=x
    print(f'A soma dos pares da lista {lst} é: {soma}')
    
lista = sorteio()
somaPar(lista)
