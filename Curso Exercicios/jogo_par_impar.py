#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
cont = 0
resultado = ''
while True:
    impar = par = soma = 0
    computador = random.randrange(1,11)
    jogador = int(input('Digite um numero'))
    escolha = input('Par ou impar [P/I]?').strip().upper()[0]
    soma = computador + jogador
    if soma % 2 == 0:
        par = 1
        resultado = 'Par'
    else:
        impar = 1
        resultado = 'Impar'
    print(f'Você jogou {jogador} e o computador {computador}\nA soma deu {soma} que é um numero {resultado}')
    if escolha == 'P' and par == 1:
        print('Você venceu!')
        cont+=1
    elif escolha == 'I' and impar == 1:
        print('Você venceu!')
        cont+=1
    else:
        print(f'Você Perdeu!!\nVenceu {cont} partidas')
        break
