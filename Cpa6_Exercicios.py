# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira 
# potência de cada elemento.
'''
def pot3 (list):
    resultado =[] 
    for i in list:
        pot = i**3
        resultado.append(pot)
    return resultado

numeros=  []

pri= int(input("Qual o primeiro número? "))
numeros.append(pri)

for i in range (1,3):
    num= int(input("Qual o próximo número? "))
    numeros.append(num)

print(pot3(numeros))
'''
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
#palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
#resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
#for i in resultado:
   # print (i)
   
def palavras (string):
    resultado = []
    for w in string:
       resultado.append(w.upper())
       resultado.append(w.lower())
       resultado.append(len(w))
    for i in resultado:
     print( i)       

frase = input("Digite a frase ou palavras: ")
 (list (map(palavras,frase)))
