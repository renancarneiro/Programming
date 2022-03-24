aluno = {}
aluno['nome'] = str(input('Nome do aluno')).upper().strip()
aluno['media'] = float(input('Media do aluno'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'- {k} do aluno: {v}')
