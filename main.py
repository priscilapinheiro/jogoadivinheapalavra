#Jogo adivinhe a palavra

import random

lines = open("palavras.txt").readlines()
line = lines[0]

palavras = line.split()


#Introdução

print("")
print("Jogo: Adivinhe a palavra")
print("*"*50)
print("Você recebera dicas e terá 3 chances para acertar a palavra.")
print("")
print("Vamos começar")
print("")

#Dicas

def dica1(palavra):
    if palavra == "gato":
        print("Dica 1:é um animal")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "água":
        print("Dica 1: seu nome tem 4 letras.")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "tulipa":
        print("Dica 1: é uma espécie de planta")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "pudim":
        print("Dica 1: pode ser doce ou salgado.")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "chocolate":
        print("Dica 1: é um alimento comum e popular no mundo todo.")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "pernambuco":
        print("Dica 1:  é uma das 27 unidades federativas do Brasil.")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "rocky":
        print("Dica 1:  ganhou o Oscar de melhor filme em 1977.")
        palpite1 = input("Qual é a palavra? ")
    elif palavra == "atary":
        print("Dica 1:  e uma das principais responsáveis pela popularização dos vídeo games.")
        palpite1 = input("Qual é a palavra? ")
    return palpite1
print("")
def dica2(palavra):
    if palavra == "gato":
        print("Dica 2:seu nome tem 4 letras.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "água":
        print("Dica 2: dia 22 de março é um dia dedicado a ela.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "tulipa":
        print("Dica 2: foi responsável por uma das primeiras bolhas financeiras do mundo.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "pudim":
        print("Dica 2: no Brasil, é mais comum como uma sobremesa.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "chocolate":
        print("Dica 2: atualmente os maiores produtores estão na áfrica.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "pernambuco":
        print("Dica 2: foi o primeiro núcleo econômico do Brasil.")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "rocky":
        print("Dica 2:  O filme gerou 8 sequências, sendo sua última lançada em 2018")
        palpite2 = input("Qual é a palavra? ")
    elif palavra == "atary":
        print("Dica 2: seu primeiro jogo foi o arcade Pong.")
        palpite2 = input("Qual é a palavra? ")
    return palpite2
print("")
def dica3(palavra):
    if palavra == "gato":
        print("Dica 3:tem hábitos noturnos. ")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "água":
        print("Dica 3: em seu estado líquido, é transparente.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "tulipa":
        print("Dica 3:  tem 6 letras.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "pudim":
        print("Dica 3:era uma refeição comum dos navios da marinha real britânica nos séculos 18 e 19.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "chocolate":
        print("Dica 3: tem 9 letras.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "pernambuco":
        print("Dica 3: estado onde nasceu o escritor Nelson Rodrigues.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "rocky":
        print("Dica 3:  foi escrito e estrelado por Sylvester Stallone.")
        palpite3 = input("Qual é a palavra? ")
    elif palavra == "atary":
        print("Dica 3: Em 1976, a empresa foi adquirida pela Warner Communications.")
        palpite3 = input("Qual é a palavra? ")
    return palpite3
print("")
#Jogo

def game():
    tentativas = 0
    limite_tentativas = 3
    palpite = []
    palavra = random.choice(palavras)
    while tentativas < limite_tentativas:
        if palpite != palavra and tentativas < 1:
            palpite = dica1(palavra)
            tentativas += 1
        elif palpite != palavra and tentativas < 2:
            print("Você errou!")
            palpite = dica2(palavra)
            tentativas += 1
        elif palpite != palavra and tentativas < 3:
            print("Você errou, essa é sua última tentativa.")
            palpite = dica3(palavra)
            tentativas += 1
        else:
            print("Você acertou")
            break
    else:
        print("Você perdeu")


game()

resposta = input("Você gostaria de jogar novamente? sim ou não? ")

while resposta == "sim":
    game()
    resposta = input("Você gostaria de jogar novamente? sim ou não? ")
else:
    print("Até logo!")

