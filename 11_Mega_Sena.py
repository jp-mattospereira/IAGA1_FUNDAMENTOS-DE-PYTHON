# 11_Mega_Sena.py: sorteia aleatoriamente números para uma aposta da mega-sena

from random import randint # Importa a função randint do módulo random para gerar números aleatórios
from Vetor import saida # Importa a função saida do módulo Vetor para exibir os números sorteados

while (True): # Loop infinito para permitir múltiplos sorteios
    n = int(input("Digite a quantidade de números a serem sorteados (no máximo 10 ou -1 para sair): ")) # Solicita ao usuário a quantidade de números a serem sorteados
    if n == -1: # Verifica se o usuário deseja sair do programa
        break
    if ((n <1) or (n > 10)):
        print("Quantidade inválida. Digite um número entre 1 e 10.")
        print() # Imprime uma linha em branco para separar os blocos de código
        continue # Reinicia o loop para solicitar novamente a quantidade de números
    print ()

    no_Jogo = [] # Inicializa uma lista vazia para armazenar os números sorteados
    for i in range(n): # Loop para sortear n números
        jogo = []
        j = 1
        while j <= 6: # Loop para sortear 6 números únicos
            nmro = randint(1, 60) # Gera um número aleatório entre 1 e 60
            if nmro not in no_Jogo: # Verifica se o número já foi sorteado
                jogo.append(nmro) # Adiciona o número à lista de números sorteados
                no_Jogo.append(nmro) # Adiciona o número à lista de números sorteados global
                j += 1 # Incrementa o contador de números sorteados
        print(saida(f"{i+1}o. Jogo", sorted(jogo))) # Exibe os números sorteados para o jogo atual
