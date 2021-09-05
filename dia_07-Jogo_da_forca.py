from palavras import words_list
from artes import logo, stages
import random

palavra = random.choice(words_list)

display = []
tamanho = len(palavra)
endgame = False

for char in palavra:
   display.append("_")


# print(f"debug - a palavra é: {palavra}")

print(logo)
print(display)

vidas = 6

while not endgame:
   tentativa = input("digite uma letra: ").lower()
   for posicao in range(tamanho):
      letra = palavra[posicao]
      if letra == tentativa:
         display[posicao] = letra


   print(stages[vidas])
   if tentativa not in palavra:
      vidas -= 1

  

   print(display)
   if "_" not in display:
      endgame = True
      print("Você venceu!")
   elif vidas < 0:
      endgame = True
      print("Você perdeu!")


