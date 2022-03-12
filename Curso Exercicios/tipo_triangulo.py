#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

a = float(input())
b = float(input())
c = float(input())

if (a-c) < a and a < (b+c):
    if (a-c) < b and b < (a+c):
        if (a-b)< c and c < (a+b):
            print('Pode formar um triangulo!')
            
            if a == b and b == c and c == a:
                print('Triangulo Equilátero!')
    
            if a == b or b == c or c == a:
                if a!= b or b != c or c!= a:
                    print('Triangulo Isósceles!')
            else:
                print('Triangulo Escaleno!')
        else:
            print('Não pode formar um triangulo')
    else:
        print('Não pode formar um triangulo')
else:
    print('Não pode formar um triangulo')

