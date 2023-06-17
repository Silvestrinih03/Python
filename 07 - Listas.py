# Listas
# Início posição 0 - Identador (chave)
notas = [10, 8, 9, 5]
for i in range (0,4):
    print(i, "= Identador", " ", notas[i], "= Nota")

# Média
notas = [10, 8, 9, 5]
soma = 0
cont = len(notas)
for i in range(0,4):
    soma+=notas[i]
media = soma/cont
print("Média = ",media)

# Calcule a média
notas = [10,6,9,3,5,7]
soma = 0
print("Notas = ",notas)
for i in range(len(notas)):
    soma+=notas[i]
print("Soma = ", soma)
media = soma/len(notas)
print ("Média = ", media)

# Solitar as notas e fazer a média
notas=[0,0,0,0,0,0]
soma=0
for i in range(len(notas)):
    print("Digite a nota ", i)
    vl = float(input("Digite um valor: "))
    notas[i] = vl
    soma+=notas[i]
print ("Notas = ",notas)
print("Soma = ", soma)
media = soma/len(notas)
print("Média = ", media)

# Exemplo 01 >> Inserir (nome, idade, CPF) em uma única lista e calcular a média das idades
dados = []
soma = 0
cont = 0
for i in range(3):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    CPF = str(input("CPF: "))
    cadastro = [nome, idade, CPF]
    soma+=idade
    cont+=1
    dados.append(cadastro)

for i in range(3):
    print(f"\nDados [{i}] \n Nome: {dados[i][0]}\n Idade: {dados[i][1]} \n CPF: {dados[i][2]}")
media = soma/cont
print(f"Média = {media:.2f}")

# Exemplo 02 >> Criar uma lista com a chave(nome) e os atributos(idade, altura, peso)
agenda = {
    "ENDRYU": [75, 1.72, 190],
    "LUYDIDJE": [18, 1.78, 80],
    "NYCOLY": [100, 1.90, 60]}

print(f"Agenda = {agenda}")
print({agenda["NYCOLY"]})

for i in agenda:
    print(i, " ", agenda[i])

# Adicionar mais uma pessoa a lista
nome="PANTURRYLYA"
idade = 55
altura = 1.78
peso = 125
aux={nome:[idade, altura, peso]}
agenda.update(aux)
print(f"Agenda atualizada: ")
for i in agenda:
    print(i, " ", agenda[i])

# Consultar nome na lista
nome = input("Digite o nome para consulta: ")
for i in agenda:
    if agenda[i]==nome:
        print(i, " ", agenda[i])