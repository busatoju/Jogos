import forca
import adivinhacao

print("Escolha o seu jogo:")
print("1 - Adivinhcação")
print("2 - Forca")

jogo = int(input("Qual você quer jogar?"))

while(jogo < 1 or jogo > 2):
    print("Escolha o seu jogo:")
    print("1 - Adivinhcação")
    print("2 - Forca")
    jogo = int(input("Qual você quer jogar?"))

if(jogo == 1):
    print("Jogo escolhido: Adivinhação")
    adivinhacao.adivinhacao.jogar()
elif(jogo == 2):
    print("Jogo escolhido: Forca")
    forca.forca.jogar()

else:
    while(jogo < 1 or jogo > 2):
        print("Escolha o seu jogo:")
        print("1 - Adivinhcação")
        print("2 - Forca")
        jogo = int(input("Qual você quer jogar?"))
