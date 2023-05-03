#Dado o salário de um funcionário, calcuçar o INSS correspondente segundo a tabela:
"""
Salário (de)  Salário (até)  Alíquota
0,00          1.302,00       7,5%
1.302,01      2.571,29       9,0%
2.571,30      3.856,94       12,0%
3.856,95      7.507,49       14,0%
"""
#Caso o funcionário ganhe acima de 7.507.49, não será calculado 14%, sim ele pagará o teto
#(1051,04) que nada mais é do que 14% em cima do limite da última faixa.
"""
Salário: 1000
Salario bruto: 1000
INSS: 75
Salário líquido: 925
"""
sal= float (7507,49)
inss = sal*0.86
print("O salário líquido obtido pelo funcionário é de: ", inss)
