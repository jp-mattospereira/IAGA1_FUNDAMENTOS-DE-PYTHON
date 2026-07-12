def desenhar_matriz_moldura(n):
    # Percorre cada linha da matriz
    for i in range(n):
        linha_atual = []
        
        # Percorre cada coluna da linha atual
        for j in range(n):
            # Validação de fronteira: se for uma das bordas externas, coloca '*'
            if (i == 0) or (i == n - 1) or (j == 0) or (j == n - 1):
                linha_atual.append("*")
            else:
                linha_atual.append("@")
                
        # Junta os elementos da linha usando um espaço em branco como separador
        print(" ".join(linha_atual))

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    tamanho = int(input())
    desenhar_matriz_moldura(tamanho)