import os

def clearConsole():
  command = "clear"
  if os.name in ('nt', 'dos'):
    command = "cls"
  os.system(command)

lances = {}

leilao = True

def encontrar_vencedor(lances_armazenados):
  lance_mais_alto = 0
  vencedor = ""
  for comprador in lances_armazenados:
    total_lance = lances_armazenados[comprador]
    if total_lance > lance_mais_alto:
      lance_mais_alto = total_lance
      vencedor = comprador
  print(f"O(A) vencedor é {vencedor} com um lance de ${lance_mais_alto}")



while leilao == True:
  name = input("Qual o seu nome? ")
  preco = int(input("Qual o seu lance? $"))
  lances[name] = preco

  continuar = input("Há outros competidores? 'sim' ou 'nao'")
  clearConsole()
  if continuar == "nao":
    leilao = False
    encontrar_vencedor(lances)


