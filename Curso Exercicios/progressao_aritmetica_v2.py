p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pa = p + (10 - 1) * r

while p <= pa:
    p+= r
    print(p, end=' ')
