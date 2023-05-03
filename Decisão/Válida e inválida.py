"""
 Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
“Nota válida”, senão “Nota inválida”.
"""
nota = float(input("Digite sua primeira nota: "))
if nota >=6 and nota <11:
    print(f"Nota válida.")
else:
    print(f"Nota inválida")