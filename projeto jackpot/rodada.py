from realfuncao import Cores, Roletando, Eventos
from time import sleep

sleep (1)
print ("=*"*20)
print ("EXPANSÃO DE DOMÍNIO! \n    APOSTADOR INCANSÁVEL!")
print ("=*"*20)
sleep(3)

print("Você chamou a expansão!")
sleep(2)
print ("Sua primeira ação resultou em...")
sleep(1)

print ("=="*20)
cor = Cores()
print (cor)
print ("=="*20)


resp = str(input("Você deseja prosseguir com essa cor? "))
if resp in "Ss":
    sleep (2)
    print ("=*="*20)
    evento = Eventos()
    print (evento)
    print ("=*="*20)
    sleep(2)
    print ("O evento começou! Isso significa que...")
    sleep (1)
    print ("A roleta...")
    sleep (1)
    print ("DEU-SE INÍCIO!")
    sleep(2)
    print ("=-="*20)
else:
    print("Tudo bem!! Vamos voltar a expandir o domínio!")

cartas_total = 0
tentativas = 0

while cartas_total < 3 and tentativas <= 5:
    tentativas += 1
    print(f"\nTentativa {tentativas} de 5\n")
    cartas_adicionadas = Roletando(cor, evento)
    cartas_total += cartas_adicionadas

    if cartas_total >= 3:
        print(f"Um momento...")
        sleep (2)
        print(f"Você retirou {cartas_total} cartas! ISSO SIGNIFICA...")
        sleep(2)
        print("-=-"*20)
        print (f"JACKPOT BABY! VOCÊ VENCEU! ESTÁ IMORTAL POR 4 MINUTOS E 11 SEGUNDOS!")
        print("-=-"*20)
        sleep(0.5)
        print (f"AHH... A DOCE MÚSICA ESTÁ CHEGANDO!")
        sleep (3)
        break

    if tentativas >= 5:
        sleep (1)
        print("-=-"*20)
        print ("QUE AZAARR BABY!")
        sleep (0.5)
        print ("\nVocê atingiu o limite de 5 tentativas! Não conseguiu tirar 3 cartas?")
        sleep (0.5)
        print("-=-"*20)
        print ("O jogo vai recomeçar!")
        break
    
    continuar = input("\nHouve ação? [S/N]")
    if continuar in "Nn":
        sleep (2)
        print("-=-"*20)
        sleep (0.3)
        print ("O jogo pausou. WON WON! Falha no sistema! Recomece!")
        print("-=-"*20)
        break
        
