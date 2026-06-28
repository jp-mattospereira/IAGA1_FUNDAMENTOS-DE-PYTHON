# Operações_com_Lista.py: realizar operações sobre uma Lista
# O objetivo dele é gerar uma aposta da Mega-Sena com 6 números aleatórios entre 1 e n.

# from random import randint: O Python, por padrão, não sabe gerar # números aleatórios sozinho. 
# Por isso, importamos uma "ferramenta" de fora chamada randint (que significa random integer, ou 
# inteiro aleatório). # Ela serve para sortear números.

from random import randint

jogo = [] #cria uma lista vazia chamada jogo

i = 1
while (i <= 6): #enquanto i for menor ou igual a 6, faça:
    nmro = randint(1, 60) #gera um número aleatório entre 1 e 60
    if (nmro not in jogo): #se o número sorteado não estiver na lista
        jogo.append(nmro) #adiciona o número sorteado à lista
        i = i + 1 #incrementa i em 1

print("\nAposta da Mega-Sena...............:", jogo) #imprime a lista com os números sorteados
jogo.sort() #ordena a lista em ordem crescente
print("Aposta da Mega-Sena (ordenada)....:", jogo) #imprime a lista com os números sorteados em ordem crescente
