# Estudando dicionario
# Estrutura Vetor
vetor = ["Nicole", "Manu", "Marcela", "Júlia"]
print(vetor)

# Estrutura Dicionário
dicionario = {"Nicole": [19, "Campinas"], "Júlia": [19, "Hortolândia"], "Marcela": [17, "Itapira"], "Manu": [20, "Campinas"]}
print(dicionario)

# Exercício 01
dados = [
    {"Doença": "Gripe", "Sintomas": ["Tosse", "Febre", "Dor de garganta"]},
    {"Doença": "Malária", "Sintomas": ["Febre", "Suor", "Dor no corpo"]},
    {"Doença": "Covid", "Sintomas": ["Febre", "Tosse", "Dor no peito"]},
    {"Doença": "Dengue", "Sintomas": ["Febre", "Dor muscular"]}
]
# Imprimir linhas do vetor
print("Linhas do Vetor: ")
for  i in dados:
    print(i)

# Imprimir conteúdo da chave "Doença"
print("Doenças: ")
for i in dados:
    print(i["Doença"])

# Verificar se a doença pesquisada está cadastrada
doenca = str(input("Digite uma doença: "))
flag = False
for i in dados:
    if doenca == i["Doença"]:
        print("Doença cadastrada")
        flag = True

if flag == False:
    print("Doença não cadastrada")

# Listar linhas
print("Listar Linhas")
for i in dados:
    print(i["\n Doença"])
    print(i["Sintomas"])

totalsintomas = []

# Pegar linha por linha do vetor
for lin in dados:
    # Separa os sintomas
    st = sintomas=lin["Sintomas"]
    # Pegar o número dos sintomas
    nuemro_sintoma=len(st)
    totalsintomas.append(nuemro_sintoma)
    print("Total de sintomas por doença: ", totalsintomas)

sintoma1 = input("Digite um sintoma: ")
sintoma2 = input("Digite um sintoma: ")
ocorrencia = []
soma = 0
for i in dados:
    st=lin["Sintomas"]
    for j in st:
        if sintoma1 ==j:
            soma+=1
        if sintoma2 ==j:
            soma+=1
    ocorrencia.append(soma)

cont = 0
for lin in dados:
    doenca=lin["Doença"]
    percentual = ocorrencia[cont]/totalsintomas[cont]
    print(doenca, " Percentual=", percentual)
    cont+=1


# Pesquisar doenças por sintomas
sintoma = str(input("Digite os sintomas: "))
for i in dados:
    '''print(i)'''
    # Separar doenças
    doenca = i["Doença"]
    # Separar sintomas
    sintomas = i["Sintomas"]
    for j in i["Sintomas"]:
        flag = False
        if sintoma == j:
            print(f"O sintoma {sintoma} está relacionado com a doença {doenca}")
            flag = True
if flag == False:
    print("Sintoma não encontrado")