# 7_Partes_Do_Nome.py: define as partes de um nome: primeiros nomes e sobrenome

def primeiros_nomes (nome): # Recebe um nome completo e retorna os primeiros nomes
    partes = nome.split(" ") # Divide o nome em partes usando espaço como delimitador
    n = len(partes) # Calcula o número de partes do nome
    result = ""
    for i in range(n - 1): # Loop de 0 a n-2
        result += partes[i] + " " # Adiciona cada parte do nome, exceto o último, ao resultado
    return (result) # Retorna os primeiros nomes concatenados com espaço


def sobrenome (nome): # Recebe um nome completo e retorna o sobrenome
    partes = nome.split(" ") # Divide o nome em partes usando espaço como delimitador
    n = len(partes) # Calcula o número de partes do nome
    return (partes[n - 1]) # Retorna a última parte do nome, que é o sobrenome


# Módulo Principal (main)
while (True):
    nome = input("Informe um nome completo ou FIM para encerrar: ") # Solicita ao usuário que insira um
    if (nome.upper() == "FIM"):
        break

    print() # Imprime uma linha em branco para separar os blocos de código

    print(f"Primeiros nomes: {primeiros_nomes(nome)}")
    print(f"Sobrenome: {sobrenome(nome)}")
    
