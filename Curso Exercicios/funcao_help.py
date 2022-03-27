def ajuda(com):
    help(com)
    
    
while True:
    comando = str(input('Funcão ou biblioteca >')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    
    
