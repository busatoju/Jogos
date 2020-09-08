import forca
import adivinhacao


def menu_jogos():
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
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogo escolhido: Forca")
        forca.jogar()

    else:
        while(jogo < 1 or jogo > 2):
            print("Escolha o seu jogo:")
            print("1 - Adivinhcação")
            print("2 - Forca")
            jogo = int(input("Qual você quer jogar?"))


menu_jogos()
