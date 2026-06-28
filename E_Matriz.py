# c_Matriz.py: monta um matriz destacando os elementos da diagonal principal, da diagonal secundária e o ponto central
# Utilizando while true, while, if em sua forma composta e for

while True:
    n=0
#Este é um loop de validação.
#Enquanto o número digitado for par (n % 2 == 0) OU for menor/igual a zero (n <= 0), insista. 
#Mas só faça isso se o usuário NÃO tiver digitado -1 (n != -1)".
#Isso garante que o programa só vai avançar se o usuário digitar um número ímpar positivo (como 3, 5, 7...) ou o comando de saída -1.  
    while (((n % 2) == 0) or (n <= 0)) and (n != -1): 
        n = int(input("Digite um número ímpar e positivo para a ordem da matriz (ou -1 para sair): "))

    if (n == -1):
        print("Programa encerrado.")
        break # O 'break' quebra o 'while True' e sai do loop

# O operador // faz uma divisão inteira (descarta o que vem depois da vírgula). 
# Se você digitar n = 5, a divisão normal seria 2.5. A divisão inteira 5 // 2 resulta em 2. 
# Como os índices em Python começam em 0 (0, 1, 2, 3, 4), o índice 2 é exatamente a posição do meio!
    meio = n // 2 
    print(f"\nMatriz de ordem {n}x{n} (meio = {meio}):\n")
    print()
    


# A Regra do Centro: 
#  Se a linha atual (i) for igual ao meio E a coluna atual (j) também for igual ao meio, 
#  significa que estamos exatamente no centro do desenho. Então, ele imprime " X ".

    for i in range(n):
        for j in range(n):
            if (i == meio and j == meio):
                print(" X ", end=" ") #end="" serve p/ q o Python ñ pule p/ a próxima linha depois de imprimir, mantendo os números lado a lado na mesma linha.
          
            elif (i == j): # A Regra da Diagonal Principal: Se a linha atual (i) for igual à coluna atual (j), significa que estamos na diagonal principal. Então, ele imprime " 1 ".
                print(" 1 ", end=" ")
        
            elif (i + j == n - 1): # A Regra da Diagonal Secundária: Se a soma da linha atual (i) e da coluna atual (j) for igual a n - 1, significa que estamos na diagonal secundária. Então, ele imprime " 2 ".
                print(" 2 ", end=" ")
            else: # Se nenhuma das condições acima for verdadeira, significa que estamos em um espaço vazio. Então, ele imprime " * ".
                print(" * ", end=" ")    
        print()
    print() # Apenas para adicionar uma linha em branco entre as matrizes, tornando a saída mais legível.
    




