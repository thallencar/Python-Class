"""
Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).
"""
num= float(input("Insira um número: "))
if num >= 0:
    print("Seu número é positivo.")
elif num <0:
    print("Seu número é negativo.")
else:
    print("Nulo")