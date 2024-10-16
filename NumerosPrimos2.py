# Fazer um programa pra retornar se o numero é primo ou não
# Numero divisivel apenas por 2 numeros, 1 e ele mesmo!!
cont_div = 0
num = int(input("Qual numero deseja verificar? "))
for i in range(1, num+1):
    if num % i == 0:
        cont_div += 1
    else:
        continue
    if cont_div == 2:
        print("O número é primo! ")
    else:
        print("Não é primo!")

### range##

first_num = int(input("Qual o primeiro numero da lista que deseja verificar? "))
sec_num = int(input("Qual o segundo numero da lista que deseja verificar? "))

primos = []

for i in range(first_num, sec_num+1):
    tot_div = 0
    for j in range(1, i+1):
        if i % j == 0:
            tot_div += 1
    if tot_div == 2:
        primos.append(i)

print("Primos = ", primos)
