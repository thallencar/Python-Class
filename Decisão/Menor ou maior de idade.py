"""
Dada uma idade pelo usuário, verificar e exibir a mensagem “Você é menor de Idade” ou “Você é
maior de Idade”.
"""
user = float(input("Digite aqui a sua idade: "))
if user > 17:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")