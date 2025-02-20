# Treinos aula 04 - Verificar se o número digitado é par ou impar, finalizar o programa com o 0
X = 1
while X != 0:
    X = int(input("Insira um número inteiro, ou insira 0 para finalizar o programa: "))
    if X % 2 == 0:
        print(X, "é par")
    else:
        print(X, "é impar")
print("Fim do programa")

# Treinos aula 04 - Imprimir os N primeiros números naturais (1 a 10)
X = 0
while X<10:
    X = X+1
    print("X = ", X)

# Treinos aula 04 - Imprimir os N primeiros números naturais
N = int(input("Digite um número: "))
K = 0   
while K < N:
    K = K+1
    print(K, end = " ")    

# Treinos aula 04 - Fazer a leitura de N números e classificá-los em par ou impar, + ou - e múltiplo de 5
while True:
    X = int(input("Digite um número: "))
    if X%2==0:
        print(X,"é par")
    else:
        print(X, "é impar")
    if X > 0:
        print(X, "é positivo")
    else:
        print(X, "é negativo")
    if X%5==0:
        print(X, "é múltiplo de 5")
    else:
        print(X, "Não é multiplo de 5")