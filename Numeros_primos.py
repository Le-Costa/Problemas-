# EXERCICIO: criar um porgrama em que  encontre  os números primos de uma coleção de números.

#Define os numeros da Range
pri_num= int (input ('Qual o primeiro numero da sequencia que você quer analisar? '))
seg_num= int (input ('Qual o segundo numero da sequencia? '))

#variavel para armazenar os número primos

primos =[]
for num in range (pri_num, seg_num):
    eh_primo = True  #variavel de controle. 

    i=2 
    while i <= num //2:
        if num % 1 ==0:
            eh_primo = False
            break
        i += 1
    if eh_primo: 
        primos.append(num)
print (primos)  

















