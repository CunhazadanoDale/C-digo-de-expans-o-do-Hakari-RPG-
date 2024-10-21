from random import randint
from time import sleep

def Cores():
    cor_hab = randint(1, 3)
    if cor_hab == 1:
        print("A cor é verde!")
        print("Probabilidade de 20%")
        return 1
    elif cor_hab == 2:
        print("A cor é vermelha!")
        print("Probabilidade de 40%")
        return 2
    else:
        print("A cor é dourada!")
        print("Probabilidade de 70%")
        return 3

def Eventos():
    eventos_hab = randint(1, 4)
    if eventos_hab == 1:
        print("O evento escolhido foi Cartão de Transporte!")
        return 1
    elif eventos_hab == 2:
        print("O evento escolhido foi Competição do Assento de Passageiro!")
        return 2
    elif eventos_hab == 3:
        print("O evento escolhido foi Aguentar o Aperto para o Banheiro no Trem Expresso!") 
        return 3
    else:
        print("O evento escolhido foi Último Trem de Sexta à Noite!")
        return 4

def Roletando(cor, evento):
    roleta_hab = 0
    cartas_reservadas = []  # Lista para armazenar as cartas tiradas
    resultado = randint(1, 239)
    bonus_resultado = randint(1, 239)
    bonus_do_bonus = randint(1, 239)

    if evento == 1:
        print("\nO número retirado foi {}!".format(resultado))
        if cor == 1 and resultado <= 47:
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 1")
        elif cor == 2 and resultado <= 95:
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            cartas_reservadas.append("Carta 2")
        elif cor == 3 and resultado <= 167:
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 3")
        else:
            print("Que azar! Faltou pouco...")

    elif evento == 2 or evento == 3:
        print("\nOs números retirados foram {} e {}".format(resultado, bonus_resultado))
        if cor == 1 and (resultado <= 47 or bonus_resultado <= 47):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 1")
        elif cor == 2 and (resultado <= 95 or bonus_resultado <= 95):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 2")
        elif cor == 3 and (resultado <= 167 or bonus_resultado <= 167):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 3")
        else:
            print("Que azar! Faltou pouco...")

    elif evento == 4:
        print("\nOs números retirados foram {}, {} e {}".format(resultado, bonus_resultado, bonus_do_bonus))
        if cor == 1 and (resultado <= 47 or bonus_resultado <= 47 or bonus_do_bonus <= 47):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 1")
        elif cor == 2 and (resultado <= 95 or bonus_resultado <= 95 or bonus_do_bonus <= 95):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 2")
        elif cor == 3 and (resultado <= 167 or bonus_resultado <= 167 or bonus_do_bonus <= 167):
            print("--"*20)
            print("Uma carta adicionada!")
            print("--"*20)
            sleep (2)
            cartas_reservadas.append("Carta 3")
        else:
            print("Que azar! Faltou pouco...")
    #verificando o total de cartas
    roleta_hab = len(cartas_reservadas)

    return roleta_hab  


    
