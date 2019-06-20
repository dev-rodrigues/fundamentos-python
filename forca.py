import random

def jogar():
    enforcou = False
    acertou = False
    erros = 0

    impreme_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_secretas = inicializa_letras_acertadas(palavra_secreta)

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

def impreme_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")

def carrega_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__ == "__main__"):
    jogar()