# Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto fixo de 10%. 
# Calcule também o valor final do produto. Apresente os valores como apresentado na coluna “Resultados”.


def calcular_desconto(valor_produto):
    # Regra de negócio: Desconto fixo de 10%
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    
# Construindo o relatório com f-strings e alinhamento visual
    result = f"Valor do Produto  = R$ {valor_produto:.2f}\n" + \
             f"Valor do Desconto = R$ {desconto:.2f}\n" + \
             f"Valor Final       = R$ {valor_final:.2f}"         
    return (result) # Retorna a string result com o relatório do desconto aplicado

# Módulo principal
if __name__ == "__main__": 

    # Captura o valor monetário digitado (ex: 10000.00 ou 5500.30)
    valor = float(input())
    
    # Exibe o relatório gerado pela nossa função
    print(calcular_desconto(valor))