#EXERCICIOS (utilizar laço em todos)
# 1 - Dado um número e um múltiplo, exibir o próximo multiplo a partir do número
#------------------------

# if n % m == 0:
   #print('é múltiplo')
#else:
   #print ('não é múltiplo')

#digitar o numero (nao)
n = int(input("Digite um número: "))
#digitar o multiplo (nao)
m = int(input("Digite um múltiplo: "))

while n % m != 0:
    n = n+1


#procurar o próximo multiplo (sim)


#exixbir o multiplo(nao)
print("Próximo múltiplo: ", n)