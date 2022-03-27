#Faça um programa que tenha uma função chamada ficha(), 
#que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, 
#mesmo que algum dado não tenha sido informado corretamente.
def ficha(n='<Desconhecido>',g=''):
    if n.strip() == '':
        n = '<Desconhecido>'
    if g.strip() == '':
        g = '0'
    if g.isnumeric():
        g=int(g)
    print(f'O jogador {n} fez {g} gols')

nome = str(input('Nome do jogador:')).upper().strip()
gols = str(input('gols:'))
ficha(nome,gols)
    
