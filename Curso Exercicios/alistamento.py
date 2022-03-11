#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou 
#se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input())
idade = 2022 - ano

if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade < 18:
    print(f'Você deverá se alistar daqui a {18-idade} anos')
else: 
    print('Já passou o tempo de você se alistar!\nProcure regularizar sua situação!')
