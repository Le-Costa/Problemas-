# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
numeros = [1,2,3,4,5,6,7,8,9,10]
print (numeros)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
objetos= ['mouse','teclado','Fone','CPU', 'Apoio'] 
print (objetos)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
a = 'Concatenando'
b= ' Strings'
c= a+b
print (c)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

rep = (1, 2, 2, 3, 4, 4, 4, 5)
print(rep.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic ={}
print ('dic vazio',dic)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic_2 ={'arroz':'branco','amora':'roxo', 'melancia':'verde' }
print ('dic2',dic_2)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic_3 = {'bebida1': 'Coca cola', 'bebida2': 'Agua de coco', 'bebida3': 'Pepsi'}
print ("dic3",dic_3)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic_3 ['bebida4'] = 'fanta'
print ('dic 3 alterado', dic_3)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dic_0 = {'a':[23,25], b: 'Pedro', c:'Leticia'}
print (dic_0)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista_2 = [ "string 1", (5,6),{'fruta': 'banana', 'doce': 'banofee'},5.63   ]

print (lista_2 )

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI.'
print (frase [0:18])