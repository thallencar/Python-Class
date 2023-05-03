"""
Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, caso uma (ou as duas)
nota seja inválida exibir “Nota inválida!” e terminar o algoritmo; senão, calcular e exibir a média e
exibir se está aprovado
"""

nota1 = float(input("Digite sua primeira nota: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Diite sua segunda nota: "))
    if nota2 >= 0 and nota2 <= 10:
        med = (nota1 + nota2) / 2
        if med >= 6 and med < 11:
            print(f"Você foi aprovado com média {med}")
        else:
            print(f"Você foi reprovado com média {med}")
    else:
        print("Nota inválida!")
else:
    print("Nota inválida!")





