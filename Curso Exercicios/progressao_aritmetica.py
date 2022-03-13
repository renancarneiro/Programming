#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.
p = int(input())
r = int(input())
decimo = p + (10-1) * r
for x in range(p,decimo+r,r):
    print(f'{x}', end=' -> ')
print('Acabou')
