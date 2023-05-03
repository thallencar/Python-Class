"""
Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5
exibir “Você está reprovado”, senão exibir “Você está aprovado”.
"""
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Diite sua segunda nota:"))
med = (nota1+nota2)/2
if med >=6:
    print(f"Você foi aprovado com média {med}")
else:
    print(f"Você foi reprovado com média {med}")