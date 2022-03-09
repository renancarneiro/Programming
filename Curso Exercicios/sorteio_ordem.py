#leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a = input()
b = input()
c = input()
d = input()
lista = [a,b,c,d]
ordem =['1','2','3','4']
random.shuffle(lista)
print('Ordem de apresentação:')
for x in range(0,4):
    print('{}º {}'.format(ordem[x],lista[x]))
