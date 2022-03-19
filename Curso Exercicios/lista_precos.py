#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('lapis', 1.50, 'borracha', 1.75, 'caderno', 20.90, 'apontador', 3.50,
            'lapiseira', 5.80, 'mochila',35.90 ,'livro', 15.75, 'caneta',1.80)
for x in range(0,len(produtos)-1,2):
    print(f'{produtos[x]:.<30}R${produtos[x+1]:6.2f}')
