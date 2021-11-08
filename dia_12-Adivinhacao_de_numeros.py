################### Adivinhe o número ####################
import random

game = True


numero = random.randrange(0, 100)

print('Bem Vindo(a) ao jogo de adivinhação!')
print('Estou pensando em um número de 1 a 100...')
dificuldade = input('Escolha a dificuldade: Digite 1 para "Fácil" ou  2 "Díficil"')

tentativas = 0

if dificuldade == '1':
    tentativas = 10
else:
    tentativas = 5

while game == True:
    print(f"Você tem {tentativas} tentativas")
    chute = int(input("Tente adivinhar: "))

    if tentativas == 0:
        print(f"Você perdeu! O número era: {numero}")
        game = False
    elif chute == numero:
        print("Parabéns! Você acertou!")
        game = False
    elif chute > 100 or chute < 0:
        print("Digite um valor entre 1 e 100")
    elif chute > numero:
        print("Tente um número menor!")
        tentativas -= 1
    elif chute < numero:
        print("Tente um número maior!")
        tentativas -= 1
    
