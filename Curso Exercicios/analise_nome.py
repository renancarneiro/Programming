# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = input()
print(nome.upper())
print(nome.lower())

letras = len(nome) - nome.count(' ')
print(letras)

lista = nome.split()
print(len(lista[0]))
