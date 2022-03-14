#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite seu sexo! [M] ou [F]').upper().strip()

while sexo not in ('FfMm'):
    sexo = input('Sexo inválido! Tente novamente').upper().strip()

print(f'Sexo {sexo} | Registrado com sucesso!')
