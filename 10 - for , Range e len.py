# Funcionamento - range 01
N=3
print(range(1,N+1))

# Funcionamento - for e range
n = 5
fatorial = 1
for i in range (1, n+1):
    fatorial = fatorial*i
    print(i, " ", fatorial)
print(n, "! = ", fatorial)

# Funcionamento - for e range 02
menor = 1000
for d in range (30+1):
    temp = 0.011*d**3-0.3*d**2+0.04*d
    if temp < menor:
        menor = temp
        print("Dia", d, "Temperatura = ", temp)
print("A menor temperatura é ", menor, "C")