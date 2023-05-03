#Formatações do print
nome = "Thalita"
idade = "18"
salario = 15892.93

#Forma 1 - Separando com vírgula
print(nome, idade, salario)

#Forma 2 - ''
print("Nome: ", nome, "Idade: ", idade, "Salário: ", salario)

#Forma 3 - ''
print("\n Nome: ", nome,"\n Idade: ", idade,"\n Salário: ", salario)
#\n força a mudança de linha

#Forma 4 - Utilizando o format()
print("Nome: {} Idade: {}  Salário: {} ".format(nome, idade, salario))

#Forma 5
print("Nome: {0} Idade: {1}  Salário: {2} - Obrigado {0} ".format(nome, idade, salario))

#Forma 6
print("Nome: {n} Idade: {i}  Salário: {s} - Obrigado {n} ".format(n= nome, i= idade, s= salario))

#Forma 7 - Utilizando o print com a formatação f
print(f"Nome: {nome} Idade: {idade} Salário: {salario}")

#Forma 8
idade = 18
print(f"Nome......: {nome} \nIdade......: {idade:7d} \nSalário......: {salario}")

valor1 = 84.3902
valor2 = 933.6
valor3 = 820421.9
valor4 = 8
print("Extrato:")
print(f"Valor 1: R${valor1:10.2f}")
print(f"Valor 2: R${valor2:10.2f}")
print(f"Valor 3: R${valor3:10.2f}")
print(f"Valor 4: R${valor4:10.2f}")

print(f"""
   Extrato:
   R${valor1:10.2f}
   R${valor2:10.2f}
   R${valor3:10.2f}
   R${valor4:10.2f}
""")
margen = " "*3
resp = input(margen + "Escolha um valor: ")
