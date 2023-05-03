"""""
EXERCÍCIO 01:
Dado uma venda pelo usuário, calcular 12% de desconto caso a venda seja maior do que 500.
"""
n = float(input("Digite aqui o total da compra: "))
if n > 500:
    n = n*0.88
print("Com o desconto, o valor total de sua compra foi de: ", n)