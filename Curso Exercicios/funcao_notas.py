#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
#e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*n, sit=False):
    maior = menor = soma = 0
    for c,x in enumerate(n):
        if c == 0:
            maior = menor = x
        if x > maior:
            maior = x
        if x < menor:
            menor = x
        soma+=x
    media = soma / (len(n))
    if sit == True:
        if media < 5:
            situacao = 'Ruim'
        elif media >= 5 and media < 6.9:
            situacao = 'Regular'
        elif media >= 7 and media <= 8.9:
            situacao = 'Boa'
        elif media >= 9:
            situacao = 'Excelente'
    print(f'Foram apresentadas {len(n)} notas\nNotas: {n}')
    print(f'A maior nota foi {maior:.2f}\nA menor foi: {menor:.2f}')
    print(f'A media da turma é {media}')
    if sit == True:
        print(f'A situação da turma é: {situacao}')
        
        
notas(3,2,5,10,10,10,10,1,sit=True)
