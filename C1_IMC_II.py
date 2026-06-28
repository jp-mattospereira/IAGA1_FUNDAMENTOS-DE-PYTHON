# Calcula e interpreta o Índice de Massa Corporal (IMC)
# Utilizando If na sua forma composta: If e Else

Paciente = input("Nome do Paciente.....: ")
pc = float(input("Peso Corporal (kg)...: "))
alt = float(input("Altura (m)..........: "))

vlr_IMC = pc / (alt ** 2)

if (vlr_IMC < 18.5):
    interpretacao = "Abaixo do peso ideal"
else:
    if (vlr_IMC < 25):
        interpretacao = "Peso ideal"
    else:
        if (vlr_IMC < 30):
            interpretacao = "Sobrepeso"
        else:
            if (vlr_IMC < 35):
                interpretacao = "Obesidade grau I"
            else:
                if (vlr_IMC < 40):
                    interpretacao = "Obesidade grau II"
                else:
                    interpretacao = "Obesidade grau III"

print("\n")
print(f"Nome do Paciente.....: {Paciente}")
print(f"Índice de Massa Corporal (IMC): {vlr_IMC:.2f}")
print(f"Interpretação: {interpretacao}")    