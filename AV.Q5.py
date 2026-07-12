def formatar_e_repetir_string(texto):
    # 1. Transforma a string em uma lista de caracteres
    caracteres = list(texto)
    
    # 2. Junta os caracteres colocando um espaço em branco entre eles
    linha_formatada = " ".join(caracteres)

    #o método .join() é a forma mais performática de colar elementos de uma lista. 
    # Usando " " (um espaço entre aspas) antes dele, nós ordenamos: "Pegue cada letra
    #  da lista e junte-as colocando um espaço em branco no meio".
    
    # 3. Imprime a linha formatada 3 vezes usando um loop simples
    for _ in range(3): 
        print(linha_formatada)
        # Dica de Mentor: Reparou que usei um caractere de underline (_) no lugar do 
        # nome da variável do for? Na convenção do Python, quando criamos um loop apenas 
        # para repetir uma ação e não vamos usar o número do índice (0, 1, 2) para nada 
        # dentro dele, usamos o _. Isso avisa a outros desenvolvedores que aquela variável 
        # é descartável, deixando o código super profissional.
    

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    # Como a entrada é um texto puro (String), usamos apenas o input()
    entrada = input()
    formatar_e_repetir_string(entrada)