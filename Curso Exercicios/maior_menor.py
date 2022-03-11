#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
a = int(input())
b = int(input())
c = int(input())
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
    
print('Maior valor',maior)
print('Menor valor',menor)
