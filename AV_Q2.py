# Faça um programa que leia um valor inteiro do teclado (variável “item”) e a seguir implemente 
# a rotina de busca sequencial: do primeiro elemento da Lista até encontrar; ou até o final da 
# Lista e não encontrar. Mostre as posições juntas dos respectivos elementos da Lista “a” e, finalizando, 
# com o resultado da busca: encontrou na posição tal; ou não encontrou “item” na Lista “a”. 
# Observe o resultado final na coluna “Resultados”.

def busca_sequencial(item):
    # Base de dados fornecida pelo exercício estruturada como Dicionário
    a = {0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18}
    
    # Flag/Sinalizador para sabermos se encontramos o item
    posicao_encontrada = -1
    
    # Mostra a estrutura da lista/dicionário conforme o gabarito
    print(f"{{0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18}}\n")
    
    # Rotina de busca: percorre cada chave do dicionário
    for posicao in a:
        if a[posicao] == item:
            posicao_encontrada = posicao
            break # Interrompe a busca assim que encontra o primeiro
            
    # Bloco de decisão para construir a resposta exata da atividade
    if posicao_encontrada != -1:
        print(f"Item: {item}, foi encontrado na posicao {posicao_encontrada}.")
    else:
        print(f"Item: {item}, \"nao\" foi encontrado.")

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    item_procurado = int(input())
    busca_sequencial(item_procurado)