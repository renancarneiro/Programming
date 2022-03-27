#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
#e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)
def notas(*n,sit=False):
    turma = dict()
    maior = menor = soma = media = 0
    turma['total'] = len(n)
    for c,x in enumerate(n):
        if c == 0:
            maior = menor = x
        if x > maior:
            maior = x
        if x < menor:
            menor = x
        soma+=x
    situacao = ''
    turma['maior'] = maior
    turma['menor'] = menor
    media = soma/len(n)
    turma['media'] = media
    if sit == True:
        if media < 5:
            turma['situacao'] = 'Ruim'
        elif media >= 5 and media < 6.9:
            turma['situacao'] = 'Regular'
        elif media >= 7 and media <= 8.9:
            turma['situacao'] = 'Boa'
        elif media >= 9:
            turma['situacao'] = 'Excelente'
    return turma
print(notas(1,23,3,0.5,sit=True))
