# Escreva uma função em Python chamada verifica_bissexto(ano)
# que recebe um número inteiro representando um ano e retorna se esse ano é bissexto ou não.

# Um ano é bissexto se for divisível por 4.
# Porém, se for divisível por 100, ele não será bissexto, exceto se também for divisível por 400.

# P ser bissexto tem ue ser divisil por 4, 100 e 400


def verBissexto(ano):
    if (ano % 4 == 0) and (ano % 100 == 0 and ano % 400 == 0):
        return True
    else:
        return False


ano = int(input("Qual ano deseja verificar? "))
print(verBissexto(ano))
