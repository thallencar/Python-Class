"""""
Dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e o tempo em anos que a pessoa fuma, 
calcular o quando esta pessoa já gastou fumando:
"""""
#Entrada: 10|1|3
# Saída: 10950

#Preço do maço
prma= float(input("Quanto custa o maço? \n > "))
#Quantidade de cigarros fumados por dia
qtdpd= int(input("Quantos cigarros são consumidos por dia? \n > "))
#Anos que fuma
anosf= float(input("Quantos anos fuma? \n > "))

#Calculo
qtdaf = anosf*365
qtdg= prma*qtdpd*qtdaf

#Saída de dados
print("A quantia em dinheiro em que foi gasta na compra de maços, é igual à: ", qtdg)
if qtdg >= 2000:
    print("Você ainda tem pulmão?")
elif qtdg >= 1000:
    print("Cuidado! Ainda há tempo de reverter a situação.")
elif qtdg >= 500:
    print("Diga não ao vício!")
elif qtdg >= 100:
    print("Não vá por esse caminho...")
else:
    print("Parabéns, você é saudável!")


