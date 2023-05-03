"""""
EXERCÍCIO 02:
Dado uma venda pelo usuário, calcular 12% de desconto caso a venda seja maior do que 500, senão o desconto será de 6%.
"""
n= float(input("Digite o valor total da compra: "))
if n > 500:
    n = n*0.88
else:
    n = n*0.92
print("Com o desconto, o valor total da compra foi de: ", n)