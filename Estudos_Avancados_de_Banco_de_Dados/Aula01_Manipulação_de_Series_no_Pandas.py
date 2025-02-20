import pandas as pd
import numpy as np

#1) Criando e Acessando Elementos
numeros = [12, 45, 78, 34, 89, 22]
s = pd.Series(numeros)
s[2]

s.size

s.iloc[-1] = 99
s

"""# 2) Rótulos"""

dic_cidades = {"Campinas": 1139047 , "Itapira": 70000 , "São Paula": 750000000000 , "Valinhas": 57000000 , "Paulinha": 20000}
serie_cidades = pd.Series(dic_cidades)
serie_cidades

serie_cidades["Mariquita"] = 1966
serie_cidades

"""# 3) Operações"""

dic_produtos = {"Sabonete": 3.75 , "Shampoo": 23.5 , "Condicionador": 30.00 , "Café": 500.5 , "Suco": 15. }
serie_produtos = pd.Series(dic_produtos)
serie_produtos

copia_produtos = serie_produtos.copy()
copia_produtos

copia_produtos = copia_produtos.mul(0.9)
copia_produtos

prod_mais_20 = copia_produtos[copia_produtos > 20]
prod_mais_20

"""# 4) Verificando e Modificando Dados"""

dic_estados = {"SP": "São Paulo" , "RJ": "Rio de Janeiro" , "ES": "Espírito Anto" , "MG": "Minas Gerais" , "BA": "Bahia"}
serie_estados = pd.Series(dic_estados)
serie_estados

serie_estados["ES"] = "Espírito Santo"
serie_estados

"""ex 4 c"""

serie_estados["SP"]

serie_estados.get("SP") is not None

existe_sp = "SP" in serie_estados.keys()
existe_sp

"""# 5) Filtragem"""

numeros_aleatorios = pd.Series(np.random.randint(1,101, size=10))
numeros_aleatorios

numeros_aleatorios.max()

numeros_aleatorios.min()

numeros_aleatorios[numeros_aleatorios > 50]