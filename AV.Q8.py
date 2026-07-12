def processar_e_ordenar_lista():
    valores = []
    
    # 1. Loop para ler os 7 valores inteiros do teclado
    for _ in range(7):
        numero = int(input())
        valores.append(numero)
        
    # 2. Ordenação da lista em ordem ascendente (crescente)
    valores.sort()
    
    # 3. Exibição da lista ordenada elemento por elemento
    for i in range(7):
        print(f"x[{i}] = {valores[i]}")
        
    print() # Pula uma linha em branco conforme o layout do gabarito
    
    # 4. Exibição do menor e maior elemento (já ordenados)
    print(f"Menor elemento, x[0] = {valores[0]}")
    print(f"Maior elemento, x[6] = {valores[6]}")

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    processar_e_ordenar_lista()