#Crie um programa que faça o computador jogar Jokenpô com você.
import random
jokenpo = ['pedra','papel','tesoura']
x = int(input('Escolha:\n[1]Pedra\n[2]Papel\n[3]Tesoura'))
x = x - 1

computador = random.choice(jokenpo)
print(f'O computador escolheu {computador.upper()} e você {jokenpo[x].upper()}')

if jokenpo[x] == 'pedra' and computador == 'tesoura':
    print('Você ganhou do computador')
elif jokenpo[x] == 'papel' and computador == 'pedra':
    print('Você ganhou do compuador')
elif jokenpo[x] == 'tesoura' and computador == 'papel':
    print('Você ganhou do computador')
elif jokenpo[x] == computador:
    print('Escolhas iguais! Joguem novamente!')
else:
    print('Você perdeu para o computador!')

