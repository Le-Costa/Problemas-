# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.
# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.

#musica somos tao jovens- legioa urbana 
#1
import re

with open ("C:/Users/10391/Desktop/arquivos txt/Legiao urbana.txt",'r' ) as arquivo: 
    musica = arquivo.read()

resultado1 = len (re.findall('a',musica))
print(resultado1)

# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
with open ("C:/Users/10391/Desktop/arquivos txt/Legiao urbana.txt",'r' ) as arquivo: 
    musica = arquivo.read()

resultado2= len (re.findall('tempo',musica) )
print (resultado2)

# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
with open ("C:/Users/10391/Desktop/arquivos txt/Legiao urbana.txt",'r' ) as arquivo: 
    musica = arquivo.read()

resultado3= (re.findall(r'\b\w+!',musica) )
print (resultado3)

# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse"
# e o sucessor seja a palavra "amargo" em um texto.
with open ("C:/Users/10391/Desktop/arquivos txt/Legiao urbana.txt",'r' ) as arquivo: 
    musica = arquivo.read()
    
resultado3= (re.findall(r'\besse\s(\w+)\samargo\b', musica))
print(resultado3)

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que 
# são anteriores ao caracter com acento.
with open ("C:/Users/10391/Desktop/arquivos txt/Legiao urbana.txt",'r' ) as arquivo: 
    musica = arquivo.read()
    
resultado5 = re.findall(r"(\w+)[\u00C0-\u017F]+", musica) 
print(resultado5)