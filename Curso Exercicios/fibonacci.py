#Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#0 – 1 – 1 – 2 – 3 – 5 – 8
n = int(input())
t1 = t2 = 1
contador = 0
print('0 1 0 ',end='')
while contador < n-3:
    contador+=1
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2 
    t2 = t3
