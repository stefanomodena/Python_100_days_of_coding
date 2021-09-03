import random

pedra = "✊"
papel = "✋"
tesoura = "✌️"

opcoes = [pedra, papel, tesoura]

humano = int(input("Qual você vai jogar? 0 para pedra, 1 para papel e 2 para tesoura\n"))

while humano > 2 or humano < 0:
    print("você digitou um número inválido!")
    humano = int(input("Qual você vai jogar? 0 para pedra, 1 para papel e 2 para tesoura\n"))

humano_jogada = opcoes[humano]
computador_jogada = random.choice(opcoes)

print("Você jogou: ")
print(humano_jogada)
print("O computador jogou: ")
print(computador_jogada)

if humano_jogada == computador_jogada:
    print("empate!")
elif humano_jogada == pedra and computador_jogada == papel:
    print("Você perdeu!")
elif humano_jogada == pedra and computador_jogada == tesoura:
    print("Você ganhou!")
elif humano_jogada == papel and computador_jogada == tesoura:
    print("Você perdeu!")
elif humano_jogada == papel and computador_jogada == pedra:
    print("Você ganhou!")
elif humano_jogada == tesoura and computador_jogada == pedra:
    print("Você perdeu!")
elif humano_jogada == tesoura and computador_jogada == papel:
    print("Você ganhou!")
