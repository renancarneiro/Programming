#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = qntd = n = 0
n = int(input('Digite um numero / [999] Para parar'))
while n != 999:
        soma+=n
        qntd+=1
        n = int(input('Digite um numero / [999] Para parar'))
print(f'A soma dos {qntd} numeros é {soma}')
