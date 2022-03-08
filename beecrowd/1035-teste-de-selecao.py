a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
valido = b > c

#  e se D for maior do que A,
valido = valido and d > a

# e a soma de C com D for maior que a soma de A e B
valido = valido and c + d > a + b

#  e se C e D, ambos, forem positivos
valido = valido and c > 0 and d > 0
#  e se a variável A for par
valido = valido and a % 2 == 0

# escrever a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".
if valido:
    print('Valores aceitos')
else:
