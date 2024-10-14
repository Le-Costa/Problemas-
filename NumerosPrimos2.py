##Fazer um programa pra retornar se o numero é primo ou não
##  Numero divisivel apenas por 2 numeros, 1 e ele mesmo!!
cont_div = 0
num = int(input("Qual numero deseja verificar? "))
for i in range (1,num+1):
    if num % i == 0:
            cont_div += 1
    else: 
            continue
    if cont_div == 2:
        print ("O número é primo! ")
    else: 
        print ("Não é primo!")



            



    




            


          
