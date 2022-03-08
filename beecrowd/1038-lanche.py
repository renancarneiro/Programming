codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

if (codigo == 1):
        total = 4 * quantidade 
elif (codigo == 2):
        total = 4.5 * quantidade 
elif (codigo == 3):
        total = 5 * quantidade
elif (codigo == 4):
        total = 2 * quantidade
elif (codigo == 5):
        total = 1.5 * quantidade
        
print("Total: R$ {:.2f}".format(total))
