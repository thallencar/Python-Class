#dados 10 numeros pelo usuário, contar quantos são negativos, positivos ou nulos

positivo = 0
negativo = 0
nulo = 0

for volta in range (1,11, 1):
    n = int(input(("Digite um número: ")))
    if n > 0:
        positivo = positivo + 1
    elif n <0:
        negativo = negativo + 1
    else:
        nulo += 1


if positivo >= 2:
    print (f"Positivos: {positivo}")
else:
    print(f"Positivo: {positivo}")
if negativo >= 2:
    print(f"Negativos:  {negativo}")
else:
    print(f"Negativo:  {negativo}")
if nulo >= 2:
    print (f"Nulos: {nulo}")
else:
    print(f"Nulo: {nulo}")


#desafio: exibir as mensagens no singular e plural