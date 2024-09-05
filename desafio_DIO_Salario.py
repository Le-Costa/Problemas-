'''Fazer um programa que calcula e imprime o salario de um funcionário 
Para realizar o calculo receba o valor bruto do salário e o adicional dos benefícios. O salario é calculado da seguinte maneira:

(Valor bruto do salário - percentual de imposto mediante salário) + adicional dos benefícios.

Para calcular o percentual de imposto segue as alíquotas:


de $0.00 a $1.100,00 = 5.00 %
de $1100.01 a $ 2500,00 = 10.00%
maior que $2500,00 = 15.00%
'''

##CÓDIGO##

sal_brut = float (input( "Qual o salario bruto? "))
ad_ben = float (input("Qual o valor do adicional? "))


if (sal_brut >= 0.00) and (sal_brut<= 1100.00) :
    per_imp = 0.05
elif (sal_brut >= 1100.01) and (sal_brut <= 2500.01):
        per_imp = 0.10
else:
    per_imp = 0.15


vlr_liq = (sal_brut - (sal_brut * per_imp) + ad_ben)

print (f"Valor liquido:  {vlr_liq:.2f}") # {} adicionada para formatação da casa decimal




