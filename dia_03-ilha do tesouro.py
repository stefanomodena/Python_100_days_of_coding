print("Bem vindo(a) a ilha do tesouro! Sua missão é encontrar o báu de tesouro.")
encruzilhada = input("Você está em uma encruzilhada, esquerda ou direita? ")

if encruzilhada == "direita":
    print("Você se perdeu! Game over")
elif encruzilhada == "esquerda":
    print("Você chegou em um lago!")
    lago = input("Tem uma ilha no meio do lago, você deseja nadar até ela ou esperar o barco? ")
    if lago == "nadar":
        print("Você se afogou! Game over")
    elif lago == "esperar":
        print("Você chegou na ilha!")
        porta = input("Na ilha há uma casa com 3 portas, amarela, vermelha e azul, qual você escolhe? ")
        if porta == "vermelha": 
            print("Dentro há uma armadilha! Game over")
        elif porta == "azul":
            print("Há um monstro dentro! Game over")
        elif  porta == "amarela":
            print("Parabéns você encontrou o tesouro!")