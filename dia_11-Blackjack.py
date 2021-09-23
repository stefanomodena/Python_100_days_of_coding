############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

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
    else:
        global jogo
        jogo = False

while jogo == True:
    print(user_cartas)
    print(pontuacao("user"))
    
    if score_jogador == 21:
        print("blackjack! Você Venceu!")
        continuar_jogo()
    elif pontuacao("computador") == 21:
        print("O computador Venceu com um Blackjack!")
        continuar_jogo()
    elif score_jogador > 21:
        print("Sua pontuação é maior que 21! Você perdeu!")
        continuar_jogo()
    else:
        hit = int(input("Outra carta('1) ou parar?('2') "))
        if hit == 1:
            distribuir_cartas(user_cartas, 1)
        else:
            while pontuacao("computador") < 17:
                distribuir_cartas(computador_cartas, 1)
            score_final_jogador = pontuacao_final(pontuacao("user"))
            print(f"A sua pontuação foi: {score_jogador}, suas cartas: {user_cartas}")
            score_final_computador = pontuacao_final(pontuacao("computador"))
            print(f"A pontuação do computador foi: {score_computador}, suas cartas: {computador_cartas}")
            if score_final_jogador < score_final_computador or pontuacao("computador") > 21:
                print("Você venceu!")
                continuar_jogo()
            elif score_final_jogador == score_final_computador:
                print("Empate!")
                continuar_jogo()
            else:
                print("Você Perdeu!")
                continuar_jogo()
            
                    


