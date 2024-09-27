#Construir uma calculadora simples#
#Função de calculo 
def calcular (num1,operacao,num2):
    if operacao == "+":
       return  num1+num2 
    elif operacao == "-":
        return  num1 - num2
    elif operacao == "*":
        return  num1*num2
    elif operacao == "/":
        return num1/num2 if num2 != 0  else  "Erro! Divisão por 0!"
    else: 
        return  "Erro! Operação invalida!"

#pega o input do usuário
num1 = float(input("Digite o primeiro número: "))
operacao = input ("Qual a operação utilizada (+,-,*,/) ?")
num2 = float (input("Qual o segundo número? "))
#Mostra o resultado
print ("Resultado: ",calcular(num1,operacao,num2))
#Pergunta se o usuario quer continuar as operações
continua = input("Deseja fazer mais operações? (S/N) ").upper()
#Loop de operações
while continua == 'S':
    num1 = float(input("Digite o primeiro número: "))
    operacao = input ("Qual a operação utilizada (+,-,*,/) ?")
    num2 = float (input("Qual o segundo número? "))
    print ("Resultado: ",calcular(num1,operacao,num2))
    continua = input("Deseja fazer mais operações? (S/N) ").upper()
else: 
    print ("Operações encerradas!")




