# Classe para clientes da netflix
class client:
    # Atributo
    def __init__(self, nome, email, plano):
        #Atributos >> Características
        self.nome = nome
        self.email = email
        self.plano = plano
    # Método --> Finalizar
    # def mudar_de_plano(self):
    # def ver_filme(self):

# Cadastro
nome_cliente = input("Nome: ")
email_cliente = input("E-mail: ")
plano_cliente = input(f"Planos:\n 1 - Basic\n 2 - Premium\nPlano escolhido : ").upper()
lista_planos = ["BASIC", "PREMIUM"]
if plano_cliente not in lista_planos:
    raise Exception("Plano inválido")

# Utilizar classes
cliente = client(nome_cliente, email_cliente, plano_cliente)
print(f"\nDados do Cliente: {cliente.nome}\nE-mail: {cliente.email}\nPlano: {cliente.plano}")