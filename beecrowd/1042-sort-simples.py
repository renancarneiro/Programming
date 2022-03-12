a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = a
#para o maior
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
    
menor = a
#para o menor
if a > b < c:
    menor = b
elif a > c < b:
    menor = c
    
meio = a
#para o meio 
if maior > b > menor:
    meio = b
elif maior > c > menor:
    meio = c

print(f'{menor}\n{meio}\n{maior}\n')

print(f'{a}\n{b}\n{c}')
