import random
from data import *
import os


def clearConsole():
  command = "clear"
  if os.name in ('nt', 'dos'):
    command = "cls"
  os.system(command)

def aleatorio():
    numero = random.randint(0, 49)
    return numero


print("Quem possui mais seguidores?")

pessoa1 = aleatorio()
print("Primeiro: ")
print(f"Seu nome é: {data[pessoa1]['name']} essa pessoa é {data[pessoa1]['description']} e mora em: {data[pessoa1]['country']}")

pessoa2 = aleatorio()
while pessoa2 == pessoa1:
    pessoa2 = aleatorio()
print("Segundo: ")
print(f"Seu nome é: {data[pessoa2]['name']} essa pessoa é {data[pessoa2]['description']} e mora em: {data[pessoa2]['country']}")

vencedor = 0
score = 0
game = True

if data[pessoa1]['follower_count'] > data[pessoa2]['follower_count']:
    # print(f"{data[pessoa1]['name']} possui mais seguidores")
    vencedor = 1
    vencedor_nome = data[pessoa1]['name']
    vencedor_seguidores = data[pessoa1]['follower_count']
    perdedor_nome = data[pessoa2]['name']
    perdedor_seguidores = data[pessoa2]['follower_count']
else:
    # print(f"{data[pessoa2]['name']} possui mais seguidores")
    vencedor = 2
    vencedor_nome = data[pessoa2]['name']
    vencedor_seguidores = data[pessoa2]['follower_count']
    perdedor_nome = data[pessoa1]['name']
    perdedor_seguidores = data[pessoa1]['follower_count']

resposta = int(input("Digite 1 para a primeira pessoa e 2 para a segunda: "))
while resposta != 1 and resposta != 2:
    print("Digite 1 ou 2!")
    resposta = int(input("Digite 1 para a primeira pessoa e 2 para a segunda: "))

if vencedor == resposta:
    print(
        f"Você acertou! {vencedor_nome} possui {vencedor_seguidores} milhões de seguidores enquanto {perdedor_nome} possui {perdedor_seguidores} milhões de seguidores")
    score += 1
    print(f"Você tem {score} pontos")
else:
    print(f"Você errou! {vencedor_nome} possui {vencedor_seguidores} milhões de seguidores enquanto {perdedor_nome} possui {perdedor_seguidores} milhões de seguidores")
    game = False


while game == True:
    print("Quem possui mais seguidores?")

    print("Primeiro: ")
    print(f"Seu nome é: {vencedor_nome} essa pessoa possui {vencedor_seguidores} milhões de seguidores")

    pessoa2 = aleatorio()
    while data[pessoa2]['name'] == vencedor_nome:
        pessoa2 = aleatorio()
    print("Segundo: ")
    print(f"Seu nome é: {data[pessoa2]['name']} essa pessoa é {data[pessoa2]['description']} e mora em: {data[pessoa2]['country']}")

    if vencedor_seguidores > data[pessoa2]['follower_count']:
        # print(f"{data[pessoa1]['name']} possui mais seguidores")
        vencedor = 1
        perdedor_nome = data[pessoa2]['name']
        perdedor_seguidores = data[pessoa2]['follower_count']
    else:
        # print(f"{data[pessoa2]['name']} possui mais seguidores")
        vencedor = 2
        perdedor_nome = vencedor_nome
        perdedor_seguidores = vencedor_seguidores
        vencedor_nome = data[pessoa2]['name']
        vencedor_seguidores = data[pessoa2]['follower_count']

    resposta = int(input("Digite 1 para a primeira pessoa e 2 para a segunda: "))
    while resposta != 1 and resposta != 2:
        print("Digite 1 ou 2!")
        resposta = int(input("Digite 1 para a primeira pessoa e 2 para a segunda: "))

    if vencedor == resposta:
        print(f"Você acertou! {vencedor_nome} possui {vencedor_seguidores} milhões de seguidores enquanto {perdedor_nome} possui {perdedor_seguidores} milhões de seguidores")
        score += 1
        print(f"Você tem {score} pontos")
    else:
        print(f"Você errou! {vencedor_nome} possui {vencedor_seguidores} milhões de seguidores enquanto {perdedor_nome} possui {perdedor_seguidores} milhões de seguidores")
        print(f"Sua pontuação final foi de: {score} pontos")
        game = False

    if game == False:
        break
    continuar = int(input("Deseja continuar jogando? (1) sim e (2) não: "))
    if continuar == 1:
        clearConsole()
        game = True
    else:
        print(f"Sua pontuação final foi de: {score} pontos")
        game = False
