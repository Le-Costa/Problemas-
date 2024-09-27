# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números  
lista_pares = []
def pares ():
    for x in range (0,21):
        if x %2 == 0:
         lista_pares.append(x)
pares()
print (lista_pares)   

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def maiusculo (frase):
  return frase.upper()

frase = input ("Qual a frase usada? ")
frase_maiusculo = maiusculo(frase)

print (frase_maiusculo)

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def adiciona_elementos (lista):
    el1 = input ("Qual o primiero elemento a adicionar ?")
    el2 = input ("Qual o primiero elemento a adicionar ?")  
    lista.append(el1)
    lista.append(el2)

frutas = ['laranja','limao','mamao','melao']

adiciona_elementos(frutas)
print (frutas)

# Exercício 4 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x+ 32,celsius)
print (list(Fahrenheit))

