#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from time import sleep
jogador = {}
jogador['nome'] = str(input('Nome:')).upper().strip()
partidas = int(input('quantas partidas jogos?'))
gols=list()
for x in range(0,partidas):
    gol = int(input(f'gols feitos na {x+1}º partida:'))
    gols.append(gol)
    jogador['gols'] = gols.copy()
    jogador['total']= sum(gols)
print('='*25)
for k,v in jogador.items():
    print(f'{k}: {v}')
print('='*25)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i,x in enumerate(gols):
    sleep(1)
    print(f'Na {i+1}º partida fez {x} gols')
    
