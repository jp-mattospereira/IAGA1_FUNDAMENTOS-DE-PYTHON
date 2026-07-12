def gerar_lista_binaria(tamanho):
    lista_resultado = []
    
    # 1. Loop para construir a estrutura baseado no tamanho informado
    for i in range(tamanho):
        # Se o índice atual dividido por 2 tiver resto 0, ele é par
        if i % 2 == 0:
            lista_resultado.append("0")
        else:
            lista_resultado.append("1")
            
    # 2. Formatação estética exigida pelo gabarito da UTFPR
    # Junta os números com ", " e envelopa com chaves de strings
    conteudo_formatado = ", ".join(lista_resultado)
    resultado_final = f"{{{conteudo_formatado}}}"
    
    print(resultado_final)

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    tamanho_desejado = int(input())
    gerar_lista_binaria(tamanho_desejado)