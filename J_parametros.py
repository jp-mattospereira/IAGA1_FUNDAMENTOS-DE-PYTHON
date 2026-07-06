# parametros.py: demonstra a finalidade dos parâmetros nos módulos. 
# Este exercício foi desenhado para te mostrar como as funções evoluem à medida que passamos 
# informações para dentro delas através dos parâmetros (as variáveis que ficam dentro dos parênteses).

def digaOla():
    print("Olá!") # Esta função não recebe nenhum parâmetro e apenas imprime uma mensagem de saudação.

def digaOlaPara(nome):
    print(f"Olá sr(a), {nome}!") # Esta função recebe um parâmetro chamado 'nome' e imprime uma saudação personalizada.

def boasVindas(nome, sexo):
    if (sexo == 'm') or (sexo == 'M') :
        print(f"Bem-vindo, sr. {nome}!") # Se o sexo for masculino, imprime uma mensagem de boas-vindas para um homem.
    else:
        print(f"Bem-vinda, sra. {nome}!") # Se o sexo for feminino, imprime uma mensagem de boas-vindas para uma mulher.        

# Módulo Principal
digaOla() # Chama a função digaOla, que não recebe parâmetros.
print() # Imprime uma linha em branco para separar os blocos de código.
digaOlaPara("João") # Chama a função digaOlaPara com o parâmetro "João".
print() # Imprime uma linha em branco para separar os blocos de código.
boasVindas("Maria", "f") # Chama a função boasVindas com os parâmetros "Maria" e "f" (feminino).
print() # Imprime uma linha em branco para separar os blocos de código.
boasVindas("Carlos", "m") # Chama a função boasVindas com os parâmetros "Carlos" e "m" (masculino).

