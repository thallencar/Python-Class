"""
Dado o número pelo usuário, verificar se o ano é bissexto
"""
b = float(input("Digite o ano para informar-se: "))
if b % 4 == 0:
    print("Ano bissexto")
else:
    print("Não é bissexto")