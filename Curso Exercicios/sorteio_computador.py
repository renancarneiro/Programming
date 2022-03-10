#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
numero = int(input())

lista = [1,2,3,4,5]
sorteio = random.choice(lista)

if numero == sorteio:
    print('processando...')
    sleep(3)
    print("Você acertou o numero!")
    print(f"O computador escolheu: {sorteio}")
else:
    print('processando...')
    sleep(3)
    print("Você errou!!")
    print(f"O computador escolheu: {sorteio}")

