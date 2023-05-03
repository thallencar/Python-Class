"""
Dado um número pelo usuário, verificar se ele é positivo, exibindo a mensagem “O numero é
positivo” ou “O numero não é positivo”
"""

num = float(input("Informe um número: "))
if num >= 1:
    print("Seu número é positivo.")
else:
    print("Seu número não é positivo.")

