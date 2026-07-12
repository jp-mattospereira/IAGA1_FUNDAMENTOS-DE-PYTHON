# 8_Faz_Linhas.py: fala sobre parâmetro padrão

def linha (tipo="*", tam=10): # Recebe um tipo de caractere e um tamanho, com valores padrão
    result = "" # Inicializa a variável result como uma string vazia
    for i in range(tam): # Loop de 0 a tam-1
        result += tipo # Adiciona o caractere do tipo especificado à variável result

    return (result) # Retorna a linha formada pelo caractere especificado repetido tam

# Módulo Principal (main)
print(linha()) # Chama a função linha com os valores padrão e imprime o resultado

print(linha("+")) # Chama a função linha com o caractere "+" e imprime o resultado
print(linha("-", 20)) # Chama a função linha com o caractere "-" e tamanho 20, e imprime o resultado
print(linha("<ABC>")) # Chama a função linha com o caractere "<ABC>" e imprime o resultado
print(linha("<ABC>", 20)) # Chama a função linha com o caractere "<ABC>" e tamanho 20, e imprime o resultado
