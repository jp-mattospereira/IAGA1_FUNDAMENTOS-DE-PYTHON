# Vetor.py: arquivo de módulos com operações sobre vetores

def entrada (id, tam): # Recebe um identificador e um tamanho, e retorna um vetor preenchido com valores do usuário
    x = [] # Inicializa uma lista vazia para armazenar os valores do vetor
    for i in range(tam): # Loop de 0 a tam-1
        x.append(int(input(f"{i + 1}o. valor, {id}[{i}]: "))) # Solicita ao usuário que insira um valor inteiro para cada posição do vetor e adiciona à lista x
    print() # Imprime uma linha em branco para separar os blocos de código
    return (x) # Retorna o vetor preenchido com os valores do usuário


def saida (id, x): # Recebe um identificador e um vetor, e imprime os valores do vetor
    tam = len(x) # Calcula o tamanho do vetor

    result = f"{id} = [" # Inicializa a string result com o identificador e o início do vetor
    for i in range(tam): # Loop de 0 a tam-1
        result += f"{x[i]}" # Adiciona o valor do vetor na posição i à string result
        if (i != (tam - 1)): # Se não for o último elemento, adiciona uma vírgula e um espaço
            result += ", "
    result += "]" # Adiciona o fechamento do vetor à string result
    return (result) # Retorna a string result

def somar (x):
    return sum(x) # Retorna a soma de todos os elementos do vetor x

def media (x):
    return (sum(x) / len(x)) # Retorna a média dos elementos do vetor x   

def toString (id, x):
    result = saida(id, x)    
    f"\n \nSoma dos Valores = {somar(x)}\n"
    f"Média dos Valores = {media(x)}" # Concatena a saída do vetor, a soma e a média em uma única string
    return (result) # Retorna a string result
