"""
Um caixa eletrônio dispensa cédulas de 50,20 e 10 reais. Considerando que a quantia seja múltiplo de 10, fazer um 
algoritmo que exiba um relatório com quantas cédulas de cada cédula são necessárias para compor essa quantia.

Entrada: 130
Saída: 50=2 | 20=1 | 10=1
"""

#Entrada de dados - Cédulas do Saque
valor= int(input("Digite aqui o valor a ser sacado: \n > "))
#Processamento de dados - Contagem de Cédulas

n50 = int(valor/50)
r50 = int(valor%50)

n20 = int(valor/20)
r20 = int(valor%20)

n10 = int(valor/10)
r10 =  int(valor%10)
#Saída de dados - Saque de cédulas
print("\n Cédulas de 50 a serem recebidas: ", n50)
print("\n Cédulas de 20 a serem recebidas: ", n20)
print("\n Cédulas de 10 a serem recebidas: ", n10)