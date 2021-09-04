import random

letras = ['a', 'b',	'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
          'm', 'n',	'o', 'p', 'q', 'r',	's', 't', 'u', 'v',	'w', 'x', 
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F,', 'G', 'H', 'I', 
          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
          'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '+', '*']

print("Bem vindo(a) ao gerador de senhas!")
nr_letras = int(input("Quantas letras você quer na sua senha?\n"))
nr_simbolos = int(input("Quantos simbolos você quer na sua senha?\n"))
nr_numeros = int(input("Quantos numeros você quer na sua senha?\n"))

senha = []

while nr_letras > 0:
   senha += [random.choice(letras)]
   nr_letras -= 1


while nr_simbolos > 0:
   senha += [random.choice(simbolos)]
   nr_simbolos -= 1


while nr_numeros > 0:
   senha += [random.choice(numeros)]
   nr_numeros -= 1


random.shuffle(senha)

senha_final = ""

for caracteres in (senha):
    senha_final += str(caracteres)


print(senha_final)
