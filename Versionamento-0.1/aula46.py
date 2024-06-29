"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 

palavra_secreta = 'Perfume'
acertos = ''
NumTentativas = 0

while True:
    Letra_digitada = input('Digite uma letra:')
    NumTentativas += 1

    if len(Letra_digitada) > 1:
        print ('Digite apenas uma letra.')
        continue

    if Letra_digitada in palavra_secreta:
        acertos += Letra_digitada

    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertos:
            palavra_formada +=letra_secreta
        else:
            palavra_formada += '*'  
    print('palavra formada:', palavra_formada )              
    if palavra_formada == palavra_secreta: 
         os.system('cls')
         print('Você ganhou!!!')
         print('Palavra secreta era: ', palavra_secreta)
         print('Quantidade de tentativas = ', NumTentativas)  
         acertos = ''
         NumTentativas = 0
 







''''''
import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "openai"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("*", end=" ")
    print()

def jogo():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    tentativas = 0
    max_tentativas = 7

    print("Bem-vindo ao jogo da palavra secreta!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while tentativas < max_tentativas:
        exibir_palavra(palavra_secreta, letras_corretas)
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_corretas:
            print("Você já tentou essa letra!")
        elif tentativa in palavra_secreta:
            letras_corretas.add(tentativa)
            if len(letras_corretas) == len(set(palavra_secreta)):
                print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
                break
        else:
            print("Essa letra não está na palavra secreta.")
            tentativas += 1

    if tentativas == max_tentativas:
        print("Você excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)

jogo()
''''''