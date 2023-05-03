"""""
EXERCÍCIO 03:
Dado uma venda pelo usuário, e se ele tem ou não um cupom de desconto, calcular 12% de desconto caso a venda seja
maior do que 500, senão o desconto será de 6%. Caso ele tenha o cupom, efetuar mais 50 reais de desconto.
"""
n= float(input("Digite o valor total da compra: "))
c= int(input("Você possui cupom? \n [1] - Sim \n [2] - Não \n > " ))
if c== 1:
    n= n-50
else:
    n = n+0
if n > 500:
    n = n*0.88
else:
    n = n*0.92
if c== 1:
    print("Com os descontos aplicados, o valor total da compra foi de: ", n)
else:
    print("Com o desconto aplicado, o valor total da compra foi de: ", n)
