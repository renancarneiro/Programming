#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: 
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
mais_velho = 0
nome_mais_velho = ''
contador = 0
for x in range(1,5):
    print(f'====PESSOA={x}=====')
    nome = input('Nome')
    idade = int(input('Idade:'))
    sexo = int(input('[1] Masculino\n[2] Feminino'))
    soma+= idade
    if sexo == 1:
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    elif sexo == 2:
        if idade < 20:
            contador+=1
    else:
        print('Gênero não identificado')
    
media = soma / 4
print(f'A media de idade do grupo é {media}')
print(f'O mais velho é o {nome_mais_velho} ele tem {mais_velho}')
print(f'Dentre as 4 pessoas {contador} mulher(es) tem menos de 20 anos')
