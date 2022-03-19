from random import randint

#sorteio das tuplas
computador = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'O computador sorteou {computador}')

#ordenação dos numeros 
ordem = sorted(computador)

#definir o tamanho do index para identificar o ultimo valor
maximo = len(ordem) - 1

#repetição dos numeros em ordem com o maior e menor valor
print(f'Numeros em ordem:', end = ' ')
for x in ordem:
    print(f'{x}', end = ' ')
maior = ordem[0]
menor = ordem[maximo]
print(f'\nMaior = {maior}\nMenor = {menor}')
