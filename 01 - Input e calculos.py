# Algorítimo: Calcular Percentual de desconto

# Ler valor do produto VP
VP = input("Digite o valor do produto: ")
VP = float(VP)

# Ler percentual do desconto PD
PD = input ("Digite o percentual de desconto: ")
PD = float(PD)

# Calcular o desconto
desconto = VP * (PD/100)

# Calcular valor pago
valorpago = VP - desconto


# escrever valor do produto
print("O produto custa " ,VP)

# Escrever percentual de desconto
print("O percentual de desconto foi de " ,PD, "%")

# Escrever valor do desconto
print ("O desconto é  equivalente a " ,desconto) 

#escrever valor total
print("O valor final do produto é " ,valorpago)


#Calcular salário
SH = input("Insira o salário hora: ")
SH = float(SH)

HT = input("Insira a quantidade de horas trabalhadas: ")
HT = float(HT)

PIR = input("Insira o percentual do imposto de renda: ")
PIR = float(PIR)



