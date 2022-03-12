#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#e que se encontram no intervalo de 1 até 500
soma= 0
contador= 0
for x in range(1,500,2):
    print(x)
    if x % 3 == 0:
        contador+=1
        soma+= x
print(f'A soma dos {contador} numeros é {soma} ')
