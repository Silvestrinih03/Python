# Exercício 01 - Converter Dolar em Real
# Qual o valor em dolar?
VD = input("Digite o valor em dolar que você deseja converter para real: ")
VD = float(VD) 
# Como converter dolar em real?
VR = VD*5.15
# Qual o resultado da conversão?
print("$",VD," é equivalente a ", VR, "R$");


# Exercício 02 >> Calcular salário bruto, imposto de renda e salário líquido
# Informações sobre salário hora (SH)
print("Para calcular seu salário bruto é necessário as seguintes informações:")
SH = input("Insira o valor do salário hora: ")
SH = float(SH)
# Informações sobre quantidade de horas trabalhadas (HT)
HT = input("Digite a quantidade de horas trabalhadas: ")
HT= float(HT)
# Calcular valor do salário bruto (SB)
SB = SH*HT
# Mostrar valor do salário bruto
print("De acordo com os dados informados, seu salário bruto é de R$", SB);
# Solicitar porcentagem do imposto de renda
PIR = input("Para chegarmos no seu salário líquido, precisamos saber quanto é descontado no seu imposto de renda, para isso insira qual seu percentual fixo de imposto de renda: ")
PIR = float(PIR)
# Calcular IR
IR = SB*(PIR/100)
# Calcular salário líquido
SL = SB - IR
# Motrar valor descontado no imposto de renda e qual o salário líquido
print("O valor descontado no seu imposto de renda é equivalente a ", IR, "% Portanto, seu salário líquido vale R$", SL);


# Exercício 03 - Solicitar dados e calcular o valor do seguro e das parcelas a serem pagas
# Boas Vindas
print("Olá, bem-vindo a seguradora Tabajata!")
print("Esse software tem o objetivo de te ajudar a calcular o valor do seguro e das parcelas a serem pagas de forma fácil e rápida!")
# Início >> Solicitação das informações necessárias
print("\nPara começar é necessário algumas informações: ")
# Solicitação do valor do bem a ser segurado (VBS)
VBS = float(input("Insira o valor do bem a ser segurado: "))
# Solicitação do número de usuários (USER)
USER = float(input("Quantos usuários estarão inclusos no plano? "))
# Solicitação da taxa de seguro (TS)
TS = float(input("Qual o percentual da taxa de seguro? "))
# Solicitação da taxa de desconto (TD)
TD = float(input("Existe alguma taxa de desconto? Insira o percentual: "))
# Solicitação do número de parcelas (NP)
NP = float(input("Qual o número de parcelas a serem pagas? "))
# Cálculos necessários para chegar a informação final
# Valor do Seguro (VSEG)
VSEG = VBS*(TS/100)
# Valor adicional por usuário (VUSER)
VUSER = VSEG*(USER/100)
# Descontos (DESC)
DESC = (VSEG + VUSER) * (TD/100)
# Valor líquido do seguro (SEG)
SEG = VSEG + VUSER - DESC
# Valor das parcelas (VPARCELA)
VPARCELA = SEG / NP
# Resposta Final do sistema
print("\nÓtimo, com as informações que você inseriu consegui calcular que o valor total do seguro é de R$", SEG, ", Portanto o valor das parcelas será de R$", VPARCELA, " por mês.")