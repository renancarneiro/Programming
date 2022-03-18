#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
cont = cont_idade = cont_homens = cont_mulheres = 0
while True:
    idade = int(input('Digite sua idade'))
    sexo = input('Sexo: [M/F]?').strip().upper()[0]
    cont+=1
    if idade > 18:
        cont_idade+=1
    if sexo == 'M':
        cont_homens+=1
    elif sexo == 'F' and idade < 20:
        cont_mulheres+=1
    continuar = input('Quer finalizar o cadastro? [S/N]').upper().strip()[0]
    if continuar == 'S':
        break
print(f'Das {cont} pessoas cadastradas:\n{cont_idade} tem mais de 18 anos')
print(f'{cont_homens} homens foram cadastrados\n{cont_mulheres} mulheres com menos de 20 foram cadastradas')
