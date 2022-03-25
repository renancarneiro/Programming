#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1':randint(1,6),
             'Jogador 2':randint(1,6),
             'Jogador 3':randint(1,6),
             'Jogador 4':randint(1,6)
            }
for k,v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('='*30)
for c,x in enumerate(ranking):
    sleep(1)
    print(f'{c+1}º lugar {x[0]} que tirou {x[1]}')
    
