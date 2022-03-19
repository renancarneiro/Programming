#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
'nove','dez','onze','doze','treze','quatorze','quinze',
'dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Digite um numero de 0 a 20'))
while n > 20 or n < 0:
    n = int(input('Tente novamente! Digite um numero entre 0 e 20'))
print(f'Você digitou o numero {numeros[n]}')
