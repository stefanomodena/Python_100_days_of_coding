print("Bem vindo(a) a calculadora de gorjeta")
conta = float(input("Qual foi o total da Conta? R$"))
gorjeta = float(input("Que porcentagem você quer pagar? 10, 12 ou 15? "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))


conta_total = gorjeta / 100 * conta + conta
resultado = round(conta_total / float(pessoas), 2)

print(f"Cada pessoa deve pagar: R${resultado}")
