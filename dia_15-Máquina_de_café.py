


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cofre = 0.00


resource_check = True


def coffee_make(receita):
    resources['water'] -= MENU[receita]['ingredients']['water']
    resources['coffee'] -= MENU[receita]['ingredients']['coffee']
    resources['milk'] -= MENU[receita]['ingredients']['milk']


def refill_machine():
    resources['water'] += 300
    resources['milk'] += 200
    resources['coffee'] += 100
     

senha = 123456

maquina_ON = True
while maquina_ON:
    pagamento_check = False
    user = input("Escolha o seu café: Espresso/Latte/Cappucino: ").lower()

    if user == "report":
        print(
            f"recursos:\nÁgua: {resources['water']}ml\nLeite: {resources['milk']}ml\nCafé: {resources['coffee']}g\ndinheiro: R${cofre}")
    elif user == "desligar":
        maquina_ON = False
    elif user == "refill":
        refill_machine()
        resource_check = True
    elif user == "saque":
        user_senha = int(input("Informe a senha de administrador: "))
        if user_senha == senha:
            print(f"Foi sacado o valor de: R${cofre}")
            cofre = 0.00
        else:
            print("Senha incorreta!")
    elif user == "espresso" or user == "latte" or user == "cappuccino":
        if resources['water'] < MENU[user]['ingredients']['water'] or resources['coffee'] < MENU[user]['ingredients']['coffee'] or resources['milk'] < MENU[user]['ingredients']['milk']:
            resource_check = False
        
        if resource_check == False:
            print("Recursos insuficientes, contactar o administrador!")

        if resource_check == True:
            while pagamento_check == False:
                print("Informe o pagamento(em moedas): ")
                pennies = float(input("moedas de R$0.01"))
                nickles = float(input("moedas de R$0.05"))
                dimes = float(input("moedas de R$0.10"))
                quarters = float(input("moedas de R$0.25"))
                pagamento = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)
                if pagamento == MENU[user]['cost']:
                    pagamento_check = True
                    cofre += pagamento
                elif pagamento > MENU[user]['cost']:
                    troco = pagamento - MENU[user]['cost']
                    print(f"O seu troco é: R${troco}")
                    cofre += pagamento - troco
                    pagamento_check = True
                else:
                    print("pagamento insuficiente!")
                    pagamento_check = False


        if resource_check == True:
            coffee_make(user)
            print("Aproveite o seu café! Volte sempre!")