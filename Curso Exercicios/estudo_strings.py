#len()   #conta o numero de strings 
#count() #conta o numero de determinada string dentro do conjunto de string
#find() #conta o numero de um conjunto de string dentro de um conjunto de string maior
#transformações com replace()
#upper() transforma a string em maiusculo
#lower() transforma a string em minusculo
#capitalize() transforma a primeira palavra da frase em maiusculo
#title()
#strip() elimina os espaços do inicio e fim das strings
#junção com join()
#split() divide a string em uma lista
frase = 'curso em video python'
print('len ->',len(frase))
print('count(o)',frase.count('o'))
print('find(deo)',frase.find('deo'))
print('replace ->',frase.replace('python','android'))
print('upper() ->',frase.upper())
print('capitalize() ->',frase.capitalize())
print('title() ->',frase.title())

teste = '   Aprenda Python  '
print(len(teste))
print(teste.strip())
print(teste.lstrip())
print(teste.rstrip())
print(teste.split())
print('-'.join(teste.split()))
print('-'.join(frase.split()))
