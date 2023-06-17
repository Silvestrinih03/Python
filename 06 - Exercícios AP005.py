# Exercício 01 - Inserir dois valores e mostrar todos os valores que estão entre os valores escolhidos
v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))

for i in range (v1,v2+1):
    print(i)

# Exercício 02 e 03 - Cálcular média e exibir a maior e menor nota inserida
n = int(input("Digite a quantidade de notas que será inserido: "))
nota = float(input('Nota: '))
menor = maior = nota
soma = nota
for i in range (n):
    nota = float(input('Nota: '))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
soma+=nota
media = soma/n
print("Média = ", media)
print("Menor = ", menor)
print("Maior = ", maior)

# Exercício 04 - Mostrar o fatorial de um número
n = int(input("Digite um número: "))
fatorial = 1*n
for i in range(1,n):
    fatorial *= (n-i)
    print(fatorial)

# Exercício 05 - Tábuada
n = int(input("Digite um número: "))
resultado = 0
for i in range(11):
    resultado = n*i
    print(f"{n} x {i} = {resultado}")

# Exercício 06 - Resolver equação para os 30 dias do mês e exibir os resultados e o dia do menor resultado 
menor = 0
for d in range(31):
    temp = 0.011*d**3 - 0.3*d**2 + 0.04*d
    print(f"A temperatura no dia {d} foi de {temp:.2f}")

    if menor > temp:
        menor = temp
print(f"A menor temperatura foi de {menor}")

# Exercício 07, 08, 09 e 10 - Computador sorteia um número e usuário tem que descobrir qual é o número sorteado
import random
computador = random.randint(0,5)
jogador = int(input("Qual sua tentativa? "))
cont = 0
while True:
    while jogador != -1:
        if computador > jogador:
            print("Seu número é MENOR que o do computador")
            jogador = int(input("Próxima tentativa ou -1 para desistir: "))
            cont+=1
        if computador < jogador:
            print("Seu número é MAIOR que o da máquina")
            jogador = int(input("Próxima tentativa ou -1 para desistir: "))
            cont+=1
        if computador == jogador:
            cont+=1
            print(f"Parabéns, você acertou o número com {cont} tentativas!")
    continuar = input("Você desistiu! \n Quer recomeçar a partida? (s/n) ")
    if continuar == "n":
        print("Ok, até mais!")
        break

# Exercício 11 e 12 - Solicitar um intervalo e verificar quais números do intervalo são divisíveis por n
vinicial = int(input("Digite o valor incial: "))
vfinal =  int(input("Digite o valor final: "))
n = int(input("Insira o número que deseja dividir: "))
print(f"Os números no intervalo de {vinicial} e {vfinal} que são divisíveis por {n} são: ")
for i in range(vinicial, vfinal+1):
    if i % n == 0:
        print(f"{i}")

# Exercício 13 - Printar itens da lista
lista=["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO","SANTOS", "FERROVIÁRIA", "JUVENTUS", "GOIÁS","ÍBIS", "SINOP"]
for i in range(len(lista)):
    print(f"{i} - {lista[i]}")

# Exercício 14, 15 e 16 - Jogar pedra, papel, tesoura com a máquina
import random
computador = int(random.randint(0,301)/100)
jogador = computador
while computador == jogador:
    jogador = int(input(" 0 - Pedra\n 1 - Papel\n 2 - Tesoura\nEscolha sua opção: "))
    while jogador < 0 or jogador > 2:
        jogador = int(input(" 0 - Pedra\n 1 - Papel\n 2 - Tesoura\nEscolha sua opção: "))
    if computador == 0 and jogador == 2:
        print("A máquina venceu!")
    elif computador == 1 and jogador == 0:
        print("A máquina venceu!")
    elif computador == 2 and jogador == 1:
        print("A máquina venceu!")
    else:
        print("Você venceu!")