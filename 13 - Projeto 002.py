# Dataset - Lista de dicionarios com doces e suas respectivas características e pesos
dados=[{"SOBREMESA":"PUDIM","CARACTERISTICA":{"CREMOSO":10, "CHOCOLATE":3, "LEITE CONDENSADO":7}},
         {"SOBREMESA":"SORVETE","CARACTERISTICA":{"MORANGO":4,"CHOCOLATE":9, "BAUNILIA":4}},
         {"SOBREMESA":"CROASSANT","CARACTERISTICA":{"CROCANTE":8,"CHOCOLATE":5, "MACIO":2}},
         {"SOBREMESA":"TIRAMISU","CARACTERISTICA":{"CREMOSO":5, "CAFE":6, "BISCOITOS":1}},
         {"SOBREMESA":"BOLO DE CANECA","CARACTERISTICA":{"MACIO":7, "BAUNILHA":10, "MORANGO":4}},
         {"SOBREMESA":"GELEIA DE MORANGO","CARACTERISTICA":{"CREMOSO":10, "AZEDO":4, "MORANGO":10}},
         {"SOBREMESA":"CANJICA","CARACTERISTICA":{"LEITE CONDENSADO":5, "MILHO":7, "PACOCA":3}},
         {"SOBREMESA":"PAMONHA","CARACTERISTICA":{"MILHO":10, "MACIO":8, "QUEIJO":5}},
         {"SOBREMESA":"CHURROS","CARACTERISTICA":{"CROCANTE":10, "DOCE DE LEITE":4, "CANELA":2}},
         {"SOBREMESA":"BOLINHO DE CHUVA","CARACTERISTICA":{"ACUCAR":2, "CANELA":2, "LEITE":7}}]

# Desing da tabela OK ----> TESTES CONCLUIDOS
def tracinho():
    print("-"*20)

# Função para separar sobremesas OK ----> TESTES CONCLUIDOS
def separar_sobremesas(ds:dict):
    sobremesa = []
    for i in ds:
        s = i["SOBREMESA"]
        sobremesa.append(s)
    return sobremesa

# Lista de sobremesas disponíveis OK ----> TESTES CONCLUIDOS
tracinho()
print(">>>  SOBREMESAS  <<<")
tracinho()
for lin in dados:
    # Separar sobremesa e suas caracteristicas OK ----> TESTES CONCLUIDOS
    sobremesa = lin["SOBREMESA"]
    print(sobremesa)
tracinho()

# Escolher três causas pra consulta OK -----> TESTES CONCLUIDOS
# Armazenar seus respectivos pesos na lista "valores" OK -----> TESTES CONCLUIDOS
valores = []
for i in range(11):
    valores.append(0)

cont=3
while cont>0:
    cont-=1
    flag=False
    caracteristicaProcurado=input("\n> DIGITE A CARACTERISTICA: ").upper()
    for pos,i in enumerate(dados):
        if caracteristicaProcurado in i["CARACTERISTICA"]:
            valores[pos]=valores[pos]+i["CARACTERISTICA"][caracteristicaProcurado]
            flag=True
    if flag==False:
        tracinho()
        print("CARACTERISTICA NÃO ENCONTRADA")
        cont+=1

# Somar pesos total para as respectivas sobremesas OK ------> TESTES CONCLUÍDOS
somapesos = []
for lin in dados:
    st = lin["CARACTERISTICA"]
    somapesos_total = 0
    for i in st:
        somapesos_total += st[i]
    somapesos.append(somapesos_total)

# Calculo da probabilidade feito através da junção das 
# listas anteriores (valores e somapesos) OK ------> TESTES CONCLUÍDOS
resultadinho = []
for a, b in zip(valores, somapesos):
    resultadinho.append((a/b)*100)

# Apresentação dos respectivos resultados da conta anterior de probabilidade em 
# ordem decrescente OK ------> TESTES CONCLUÍDOS
print('\n')
tracinho()
print('>>> PERCENTUAL DAS\n   CARACTERISTICAS \n      NOS DOCES\n   CADASTRADOS <<<')
tracinho()
sobremesa = separar_sobremesas(dados)
cont=0
lista = []
for i in resultadinho:
    if i>0:
        teste = sobremesa[cont],i
        lista.append(teste)
        cont+=1
lista.sort(key=lambda x:x[1], reverse=True)
print('\n')
for i in lista:
    doce = i[0]
    porc = i[1]
    print(f"{doce} {porc:.2f}%")

print('\n')
tracinho()
print("** FIM DO PROGRAMA **")
print("  JÚLIA DIAS \n       E\nNICOLE SILVESTRINI")