#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um 
#e permita que o usuário possa mostrar as notas de cada aluno individualmente.
aluno = []
escola = []
while True:
    aluno.append(str(input('Digite o nome do aluno:')).upper().strip())
    aluno.append(float(input('Nota 1:')))
    aluno.append(float(input('Nota 2:')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    escola.append(aluno[:])
    aluno.clear()
    continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Código inválido! Tente novamente\nQuer continuar? [S/N').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Nº  NOME    MÉDIA')
print('='*20)
for c,x in enumerate(escola):
   print(f'{c:<4}{x[0]:<10}{x[3]:>3.1f}')
while True:
    n = int(input('Mostrar notas de qual aluno? (999 Imterromper)'))
    if n == 999:
        break
    if n <= len(escola):
        print(f'Notas de {escola[n][0]} são [{escola[n][1]}] [{escola[n][2]}]')
print('Finalizado com sucesso')
    
    
