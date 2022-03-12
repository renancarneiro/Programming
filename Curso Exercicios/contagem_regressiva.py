#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
sleep(0.5)
print('-='*10)
sleep(0.5)
print('CONTAGEM REGRESSIVA!')
sleep(0.5)
print('-='*10)
for x in range(10,0,-1):
    sleep(1)
    print('       ',x)
print('-='*10)
print('  Feliz ano novo!!')
print('-='*10)
