def calcular_desconto_condicional(valor_produt):
    # 1. Estrutura de Decisão (Regra de Negócio)
    if valor_produt < 5000.00:
        porcentagem = 10
        desconto = valor_produt * 0.10
    else:
        porcentagem = 15
        desconto = valor_produt * 0.15
        
    valor_final = valor_produt - desconto
    
# 2. Construção do Relatório Formatado (Ajustado para o validador)
    result = f"Valor do Produto        = R$ {valor_produt:.2f}\n" + \
             f"Valor do Desconto ({porcentagem}%) = R$ {desconto:.2f}\n" + \
             f"Valor Final             = R$ {valor_final:.2f}"
             
    return (result)

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    valor = float(input())
    print(calcular_desconto_condicional(valor))