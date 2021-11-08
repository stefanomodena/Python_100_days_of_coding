import random
import os


def clearConsole():
  command = "clear"
  if os.name in ('nt', 'dos'):
    command = "cls"
  os.system(command)

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cartas = []
computador_cartas = []

cartas_distribuidas = []

global aposta
aposta = 0
dinheiro = 1000

def aposta_func():
    global aposta
    global dinheiro
    aposta += int(input("Quanto você deseja apostar? "))
    while aposta > dinheiro:
        aposta += int(input(f"Insira um  valor válido menor ou igual a: ${dinheiro}"))

    dinheiro -= aposta

def distribuir_cartas(list, vezes):
    """Adiciona uma quantidade de cartas, determinado por vezes, no deck determinado por LIST"""
    for i in range(vezes):
        list.append(random.choice(cartas))

def pontuacao(player):
    """Calcula a pontuacao da pessoa determinada por PLAYER. O 11 é trataco como ÁS, então é calculado como 11 ou 1"""
    if player == "user":
        global score_jogador
        score_jogador = sum(user_cartas)
        if 11 in user_cartas and score_jogador > 21:
            user_cartas.remove(11)
            user_cartas.append(1)
            score_jogador = sum(user_cartas)
            return score_jogador
        else:
            return score_jogador
    if player == "computador":
        global score_computador
        score_computador = sum(computador_cartas)
        if 11 in computador_cartas and score_computador > 21:
            computador_cartas.remove(11)
            computador_cartas.append(1)
            score_computador = sum(computador_cartas)
            return score_computador
        else:
            return score_computador

distribuir_cartas(user_cartas, 2)
distribuir_cartas(computador_cartas, 2)

def pontuacao_final(player):
    score_final = 21 - player
    return score_final

global jogo
jogo = True

def continuar_jogo():
    continuar = input("Deseja jogar novamente? s ou n ")
    if continuar == "s":
        clearConsole()
        user_cartas.clear()
        computador_cartas.clear()
        distribuir_cartas(user_cartas, 2)
        distribuir_cartas(computador_cartas, 2)
        global aposta
        aposta = 0
    else:
        global jogo
        jogo = False

while jogo == True:
    print(user_cartas)
    print(pontuacao("user"))
    print(f"${dinheiro}")
    print(f"Aposta atual: {aposta}")



    if score_jogador == 21:
        print("blackjack! Você Venceu!")
        dinheiro += (aposta * 2)
        print(f"${dinheiro}")
        continuar_jogo()
    elif pontuacao("computador") == 21:
        print("O computador Venceu com um Blackjack!")
        print(f"${dinheiro}")
        continuar_jogo()
    elif score_jogador > 21:
        print("Sua pontuação é maior que 21! Você perdeu!")
        print(f"${dinheiro}")
        continuar_jogo()
    else:
        hit = int(input("Outra carta('1) parar('2') ou apostar('3') "))
        if hit == 1:
            distribuir_cartas(user_cartas, 1)
        elif hit == 3:
            aposta_func()
            while pontuacao("computador") < 17:
                distribuir_cartas(computador_cartas, 1)
            score_final_jogador = pontuacao_final(pontuacao("user"))
            print(
                f"A sua pontuação foi: {score_jogador}, suas cartas: {user_cartas}")
            score_final_computador = pontuacao_final(pontuacao("computador"))
            print(
                f"A pontuação do computador foi: {score_computador}, suas cartas: {computador_cartas}")
            if score_final_jogador < score_final_computador or pontuacao("computador") > 21:
                print("Você venceu!")
                dinheiro += (aposta * 2)
                print(f"${dinheiro}")
                continuar_jogo()
            elif score_final_jogador == score_final_computador:
                print("Empate!")
                dinheiro += aposta
                continuar_jogo()
            else:
                print("Você Perdeu!")
                print(f"${dinheiro}")
                continuar_jogo()
        else:
            while pontuacao("computador") < 17:
                distribuir_cartas(computador_cartas, 1)
            score_final_jogador = pontuacao_final(pontuacao("user"))
            print(f"A sua pontuação foi: {score_jogador}, suas cartas: {user_cartas}")
            score_final_computador = pontuacao_final(pontuacao("computador"))
            print(f"A pontuação do computador foi: {score_computador}, suas cartas: {computador_cartas}")
            if score_final_jogador < score_final_computador or pontuacao("computador") > 21:
                print("Você venceu!")
                dinheiro += (aposta * 2)
                print(f"${dinheiro}")
                continuar_jogo()
            elif score_final_jogador == score_final_computador:
                print("Empate!")
                dinheiro += aposta
                continuar_jogo()
            else:
                print("Você Perdeu!")
                print(f"${dinheiro}")
                continuar_jogo()