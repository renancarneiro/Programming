x = int(input())
y = int(input())
soma = 0

for z in range(x-1,y,-1):
    if z % 2 == 1:
        soma+= z
print(soma)
