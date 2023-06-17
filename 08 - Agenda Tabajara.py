# Nicole Silvestrini Garrio - 23009486
menu = -1
agenda= {}

while menu != 0 and menu != 1 and menu != 2 and menu != 3:
    print("Menu:\n 1 - Cadastrar\n 2 - Listar\n 3 - Consultar\n 0 - Sair\n")
    menu = int(input("Digite sua opção: "))
    if menu == 1:
            print("\nTela de Cadastro")
            continua = "s"
            while continua == "s":
                    nome = str(input("Nome: "))
                    celular = int(input("Celular: "))
                    telefone = int(input("Telefone fixo: "))
                    cadastro = {nome:[celular, telefone]}
                    agenda.update(cadastro)
                    print("Cadastrado com sucesso!")
                    continua = str(input("\nAdicionar pessoa? s/n\n"))
                    while continua != "s" and continua != "n":
                         continua = str(input("\nAdicionar pessoa? s/n\n"))
                    if continua == "n":
                        print("Fim do cadastro!\n")
                        menu = -1                      

    if menu ==2:
        print("\nAgenda: ")
        for i in agenda:
             print(i, " ", agenda[i], "\n")
        menu = -1

    if menu == 3:
        print("\nTela de Consulta")
        nome = str(input("Digite o nome que deseja encontrar: "))
        for i in agenda:
             if i == nome:
                  print(i, " ", agenda[i])
        menu = -1

    if menu == 0:
        print("Fim do programa!")
        break