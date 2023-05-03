"""
Dado um número pelo usuário, verificar se ele é “O número é par” ou “O número é impar”,
exibindo sua respectiva mensagem.
"""
num = float(input("Digite um número aqui: "))
if num % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é ímpar.")