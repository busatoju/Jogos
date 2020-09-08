import random


def jogar():
    print("Bem vindo ao Jogo da Adivinhação")
    numero_secreto = random.randrange(1, 101)

    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print(" 1- Fácil 2- Médio 3- Difícil")
    nivel = int(input("Escolha o nível:"))

    while(nivel < 1 or nivel > 3):
        print("Qual o nível de dificuldade?")
        print(" 1- Fácil 2- Médio 3- Difícil")
        nivel = int(input("Escolha o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20

    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")

        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(menor):
                print("Você errou! Chute menor que o número secreto!")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} ".format(
                        numero_secreto, pontos))
            elif(maior):
                print(" Você errou! Chute maior que o número secreto!")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} ".format(
                        numero_secreto, pontos))

        # Pontos perdidos da rodada
        pontos_perdidos = abs(numero_secreto - chute)
        # subtraindo os pontos perdidos da pontuação total
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1


jogar()
