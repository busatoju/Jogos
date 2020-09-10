import random


def jogar():

    print('Bem vindo ao jogo da Forca!')

    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual a letra?")
        # Retira os espaços da string
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo!")


if(__name__ == "__main__"):
    jogar()
