import random

def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")

    palavras = []
    arquivo = open("frutas.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()

    letras_secretas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_secretas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if (chute == letra) :
                    letras_secretas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_secretas
        print(letras_secretas)

    if (acertou):
        print("Voce ganhou")
    else:
        print("voce perdeu")
    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()