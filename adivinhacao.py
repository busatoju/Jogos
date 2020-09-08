print('Bem vindo ao jogo de Advinhação!')

numero_secreto = 42

chute_str = input("Digite seu numero: ")
#O python lê o valor como string, sendo necessário converter para inteiro, caso contrário a verificação abaixo
#sempre será falsa

print("Você digitou ", chute_str)
chute= int(chute_str)

if(numero_secreto == chute) :
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de jogo!")
