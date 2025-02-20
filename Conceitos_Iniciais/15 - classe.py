# Orientação a objetos
# Criar objetos - classes
    # Atributos - características
    # Métodos - função

#Objeto
class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        # Atributos
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    # Métodos
    def mudar_de_canal(self, botao):
        if botao == "+":
            print("AVANÇA")
        elif botao == "-":
            print("REGRESSA")
    

# Instansias da classe - Utilizar classes
controle_1 = ControleRemoto("Preto", "10cm", "2cm", "2cm")
print(f"\nControle 1:\nCor = {controle_1.cor}\nAltura = {controle_1.altura}\nProfundidade = {controle_1.profundidade}\nLargura = {controle_1.largura}")
botao_escolhido = input("Escolha + para avançar ou - para regressar: ")
controle_1.mudar_de_canal(botao_escolhido)

controle_2 = ControleRemoto("Cinza", "15cm", "3cm", "2cm")
print(f"\nControle 2:\nCor = {controle_2.cor}\nAltura = {controle_2.altura}\nProfundidade = {controle_2.profundidade}\nLargura = {controle_2.largura}")
botao_escolhido = input("Escolha + para avançar ou - para regressar: ")
controle_2.mudar_de_canal(botao_escolhido)