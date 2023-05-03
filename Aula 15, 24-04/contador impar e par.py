# contar quantos n pares e impares foram digitados pelo usuario ate que ele digite zero
# ler numeros (sim)
#verficar se é par ou impar (sim)
#contar os pares e impares (sim)
# exibir a quantidade de pares e impares (nao)
par = 0
impar = 0

while True:
    n = int(input(("Número: ")))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    if n ==  -1:
        break
print(f"""
    Pares: {par}
    Impares: {impar}
""")



