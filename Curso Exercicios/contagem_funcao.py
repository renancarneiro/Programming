#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
#início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
#ex (12,-10,7)
aux = 0
from time import sleep
def contagem(i,f,p):
    print(f'\nContagem de {i} até {f} passo {p}')
    sleep(0.5)
    if p == 0:
        p = 1
    if i < f:
        if p < 0:
            aux = f
            f = i - 2
            i = aux
        for x in range(i,f+1,p):
            sleep(0.5)
            print(x,end=' ')
    else:
        if p > 0:
            p = -p
        for x in range(i,f-1,p):
            sleep(0.5)
            print(x,end=' ')
        print()
contagem(1,10,1)
contagem(10,0,2)
sleep(0.5)
print('='*25)
print('Contagem personalizada')
print('='*25)
sleep(1)
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contagem(inicio,fim,passo)
