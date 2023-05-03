aprov = 0
reprov = 0
for volta in range(1, 6, 1):
    print(f"--- ALUNO {volta}")
    while True:
        n1 = int(input("Nota 1: "))
        if n1 >= 0 and n1 <= 10:
            n2 = int(input("Nota 2: "))
            if n2 >= 0 and n2 <= 10:
                media = (n1 + n2) / 2
                print(f"Media = {media}")
                break
            else:
                print("Nota inválida! Digite novamente.")
        else:
            print("Nota inválida! Digite novamente.")
    if media >= 5:
        aprov = aprov + 1
    else:
        reprov = reprov + 1

print(f"""\nAprovado:{aprov}\nReprovado:{reprov}""")

