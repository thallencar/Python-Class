# 2 - dado um numero, exibiir o seu fatorial: 4! = 4.3.2.1 = 24

#pegar um numero (nao)
n = int(input("Digite um número: "))

fat = 1
for volta in range(n, 1, -1): #inicio - fim - incremento
    fat = fat * volta


#exibir o fatorial (sim)
print("Fatorial = " ,fat)