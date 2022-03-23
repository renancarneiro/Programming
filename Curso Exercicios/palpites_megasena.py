#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados 
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
n = int(input('Digite a quantidade de jogos'))
sorteio = []
lista = []
for x in range(0,n):
    for i in range(0,6):
        sorteio.append(randint(1,61))
    sorteio.sort()
    lista.append(sorteio[:])
    sorteio.clear()
sleep(1)
print('='*30)
print('PALPITES MEGA SENA')
print('='*30)
for c,x in enumerate(lista):
    sleep(1)
    print(f'Jogo {c+1}: {x}')
