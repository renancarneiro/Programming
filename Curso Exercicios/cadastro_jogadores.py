#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#Versão 2: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
jogadores = []
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador:')).upper().strip()
    partidas = int(input('Nº de partidas:'))
    for x in range(0,partidas):
        gols.append(int(input(f'gols da {x+1}º partida:')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Código inválido! Tente novamente\nQuer continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('Cod Nome Gols Total')
for i,x in enumerate(jogadores):
    print(f'{i} {x["nome"]} {x["gols"]} {x["total"]}')
dados = 0
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar):'))
    if dados == 999:
        break
    if dados >= len(jogadores):
        print('Nenhum jogador encontrado! Tente novamente')
    else:
        print(f'Levantamento de jogos | {jogadores[dados]["nome"]}')
        print('='*25)
        for c,x in enumerate(jogadores[dados]['gols']):
            print(f'No {c+1}º jogo fez {x} gols')
print('Programa finalizado!')
