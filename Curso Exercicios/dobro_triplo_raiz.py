#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input())
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro é: {} \nO triplo é: {}\nA raiz é: {:.2f}'.format(dobro,triplo,raiz))
