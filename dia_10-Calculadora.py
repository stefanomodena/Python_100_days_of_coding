# somar
def somar(n1, n2):
    return n1 + n2

# Subtrair
def subtrair(n1, n2):
    return n1 - n2

# Multiplicar
def multiplicar(n1, n2):
    return n1 * n2

# Dividir
def dividir(n1, n2):
    return n1 / n2

operacoes = {
    "+": somar, 
    "-": subtrair, 
    "*": multiplicar, 
    "/": dividir, 
    }



continuar = True

while continuar == True:

    num1 = int(input("Qual é o primeiro número?"))

    for operator in operacoes:
        print(operator)

    operacao = input("Escolha uma operação entre as acima: ")

    num2 = int(input("Qual é o segundo número?"))

    operacao_funcao = operacoes[operacao]
    resposta1 = operacao_funcao(num1, num2)

    print(f"{num1} {operacao} {num2} = {resposta1}")

    continuar_input = input("Deseja continuar este cálculo? 's' ou 'n' ")
    if continuar_input == "n":
        continuar = False
        break

    operacao = input("Escolha outra operação: ")
    num3 = int(input("Qual é o próximo número?"))
    operacao_funcao = operacoes[operacao]
    resposta2 = operacao_funcao(resposta1, num3)

    print(f"{resposta1} {operacao} {num3} = {resposta2}")

    continuar_input = input("Deseja realizar outro cálculo? 's' ou 'n' ")
    if continuar_input == "n":
        continuar = False
