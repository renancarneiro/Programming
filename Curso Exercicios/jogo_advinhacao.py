#O computador vai “pensar” em um número entre 0 e 10. 
#o jogador vai tentar adivinhar até acertar.
#mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
computador = random.randrange(1,11)
jogador = int(input('Digite um numero de 1 a 10: '))
contador = 0

while jogador != computador:
    jogador = int(input(f'Você errou! Tente novamente\nO computador escolheu o numero {computador}'))
    contador+=1
    computador = random.randrange(1,10)
    
if contador == 0:
    print(f'Você acertou de primeira, parabens!\nO computador escolheu {computador} também')
else:
    print(f'Você acertou, o computador escolheu {computador} também, mas demorou {contador} vezes até acertar')
    
