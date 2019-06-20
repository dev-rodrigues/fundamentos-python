import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 100

    print("Qual é o nivel de dificuldade")
    print("(1) facil, (2) medio, (3) dificil")

    nivel = int(input("Digite o nível"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))

        chuve_str = input("Digete um numero: ")
        print("Você digitou ", chuve_str)
        chute = int(chuve_str)

        if (chute < 1):
            print("Digite um numero entre 1 e 100")
            continue
        elif (chute >= 100):
            print("Digite um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Você acertou")
            break
        else:
            if (chute_maior):
                print("você errou, o seu valor foi maior do que o numero secreto.")
            if (chute_menor):
                print("você errou, o seu valor foi menor do que o numero secreto.")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
