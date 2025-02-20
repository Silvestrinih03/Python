# Vetor
dados = [15, 17, 1, 9, 64, 32, 41, 7, 2]

# Dado um vetor numérico, encontrar o maior e o menor valor
maior = 0
menor = 10000000
for i in dados:
    if i>maior:
        maior = i
    if i<menor:
        menor = i
print(f"maior = {maior}\nmenor = {menor}")

# Organizar vetor em ordem crescente
flag = True
while flag == True:
    flag = False
    for i in range(len(dados)-1):
        if dados[i] > dados[i+1]:
            aux=dados[i]
            dados[i]=dados[i+1]
            dados[i+1]=aux
            flag = True
print(dados)
        