# Exercício 01 - sistema de login
SENHA = int(input("Insira uma senha de 4 dígitos: "))
LOGIN = int(input("Insira a senha para logar: "))
if LOGIN == SENHA:
    print("Acesso Pertmitido")
else:
    if LOGIN != SENHA:
        print("Acesso Negado")



# Exercício 02 - Inserir números e verificar se os mesmos podem formar um triângulo
print("Olá, esse código tem a função de verificar se os números inseridos por você podem formar um triângulo.Caso seja possível o sistema informa se o triângulo formado é equilátero, isósceles ou escaleno! Vamos iniciar?")
L1 = float(input("Insira a medida do primeiro lado: "))
L2 = float(input("Insira a medida do segundo lado: "))
L3 = float(input("Insira a medida do terceiro lado: "))

SOMA1 = L2+L3
SOMA2 = L1+L2
SOMA3 = L1+L3

if L1 == L2 and L1 == L3:
    print("Essas medidas formam um triângulo equilátero")
elif L1 == L2 or L1 == L3 or L2 == L3:
    if L1 < SOMA1 and L2 < SOMA3 and L3 < SOMA2:
        print("Esse triângulo é isóceles")
    else:
        print("Esses números não podem formar um triângulo")
elif L1 != L2 != L3:
    if L1 < SOMA1 and L2 < SOMA3 and L3 < SOMA2:
        print("Esse triângulo é Escaleno")
    else:
        print("Esses números não podem formar um triângulo")



# Exercício 03 - Verificar se o número inserido é par ou impar
N = float(input("Insira um núemro: "))
if N%2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")



# Exercício 04 - Verificar se X é divisível por Y
X = float(input("Insira o primeiro número: "))
Y = float(input("Insira o segundo número: "))
if X%Y == 0:
    print(X, " é divisível por ", Y)
else:
    print(X, " não é divisível por ", Y)



#Exercício 05 - Calcular média do aluno
print("Boletim do Aluno")
NOTA1 = float(input("Insira a nota da primeira prova: "))
NOTA2 = float(input("Insira a nota da segunda prova: "))
PESO1 = 2
PESO2 = 1

MEDIA = (NOTA1*PESO1+NOTA2*PESO2)/ PESO1+PESO2

print("As notas desse aluno foram ", NOTA1, "e ", NOTA2, " e os respectivos pesos são ", PESO1, "e ", PESO2)
print("A média final desse aluno é", MEDIA)
if MEDIA < 5:
    print("Aluno Reprovado")
if MEDIA >= 5:
    print("Aluno Aprovado")
    if MEDIA >=8 and MEDIA<9:
        print("Parabéns, seu desempenho foi muito bom")
    if MEDIA > 9:
        print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR")



# Exercício 06 e 07 - Conversão para ºC
print("Menu:\n 1 - Fahrenheit\n 2 - Kelvin\n 3 - Rankine\n 4 - Réaumur")
MENU = int(input("Digite o número referente a medida que deseja trabalhar:"))

if MENU == 1:
    F = float(input("Você esolheu a opção Fahrenheit\nIsira o número que deseja converter para Celsius: "))
    C = (5*(F-32))/9
    print("O valor de ", F, "graus Fahrenheit em Celsius é %.2f" %C)
if MENU == 2:
    K = float(input("Você esolheu a opção Kelvin\nIsira o número que deseja converter para Celsius: "))
    C = K - 273.15
    print("O valor de ", K, " graus Kelvins em Celsius é %.2f" %C)
if MENU == 3:
    RK = float(input("Você esolheu a opção Rankine\nIsira o número que deseja converter para Celsius: "))
    C = 5*RK/9-273.13
    print("O valor de ", RK, "graus Rankine em Celsius é %.2f" %C)
if MENU == 4:
    R = float(input("Você esolheu a opção Réaumur\nIsira o número que deseja converter para Celsius: "))
    C = 5*R/4
    print("O valor de ", R, "graus Réaumur em Celsius é %.2f" %C)



# Exercício 08 - Calcular desconto
print("Para calcular seu desconto é necessário algumas informações")
CONSTRUCAO = float(input("Insira o ano de construção do imóvel: "))
ANO = float(input("Insira o ano atual: "))

IDADE = ANO - CONSTRUCAO
if IDADE < 5:
    print("Você não possue direito ao desconto, pois a idade do imóvel é inferior a 5 anos!")
if IDADE >=5 and IDADE < 20:
    print("Seu percentual de desconto é equivalente a 15%")
if IDADE >= 20 and IDADE < 40:
    print("Seu percentual de desconto é equivalente a 25%")
if IDADE >= 40:
    print("Seu percentual de desconto é equivalente a 30%")



# Exercício 09 - Cálcular IMC e informar classificação
print("Olá, esse app tem a função de calcular seu índice de massa corporal (IMC) e informar qual sua classificação:\n Menor que 18,5 - baixo do peso\n De 18,5 a 24,99 - normal\n De 25 a 29,99 - Sobrepeso\n Maior que 30 - Obesidade\n vamos começar?")
PESO = float(input("Digite seu peso em KG: "))
ALTURA = float(input("Digite sua altura em metros: "))

IMC = PESO / ALTURA**2

print(f"Seu IMC foi: {IMC:6.2f}")

if IMC < 18.5:
    print("Você está classificado como [abaixo do peso]")
if IMC > 18.5 and IMC < 24.9:
   print("Você está classificado como [normal]")
if IMC > 25 and IMC < 29.99:
  print("Você está classificado como [sobrepeso]")
if IMC > 30:
  print("Você está classificado como [Obeso]")



# Exercício 10 - Informar ordem dos números inseridos pelo usuário
N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
N3= float(input("Digite o terceiro número: "))

if N1 < N2 < N3:
    print("Os números estão em ordem crescente!")
if N3 < N2 < N1:
    print("Os números estão em ordem decrescente")
else:
    print("Esses números não estão seguindo uma ordem")



# Exercício 11 - Cálcular média e frequência do aluno
print("Cálculo do Boletim do Aluno")
NOTA1 = float(input("Digite a nota da avaliação 1: "))
NOTA2 = float(input("Digite a nota da avaliação 2: "))
AULAS = int(input("Insira a quantidade de aulas do semestre: "))
PRESENCA = int(input("Insira o número de presença: "))

MEDIA = NOTA1+NOTA2/2
FREQUENCIA = PRESENCA*100/AULAS

print("Boletim do Aluno:\n Média: ", MEDIA, " Frequência: %.2f" %FREQUENCIA)
if FREQUENCIA < 75:
    print("Reprovado")
if FREQUENCIA >= 75 and MEDIA < 4:
    print("Reprovado")
if FREQUENCIA >= 75 and MEDIA > 4 and MEDIA < 6:
    print("Exame")
if FREQUENCIA >= 75 and MEDIA > 6:
    print("Aprovado")


# Exercício 12 - Resolver a equação
x = int(input("Digite o valor de x que seja diferente de zero: "))
f = 0
if x != 0:
    f = ((4*x^2)-(3*x)+9)/x 
    print("f(x) = ", f)
else: 
    print("Digite um valor diferente de zero!")