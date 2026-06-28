paciente = input("Nome do Paciente.....: ")
pc = float(input("Peso Corporal (kg)...: "))
alt = float(input("Altura (m)..........: "))

vlr_IMC = pc / (alt ** 2)

if (vlr_IMC < 18.5):
    interpretacao = "Abaixo do peso ideal"

if (vlr_IMC >= 18.5) and (vlr_IMC < 25):
    interpretacao = "Peso ideal"

if (vlr_IMC >= 25) and (vlr_IMC < 30):
    interpretacao = "Sobrepeso" 

if (vlr_IMC >= 30) and (vlr_IMC < 35):
    interpretacao = "Obesidade grau I"

if (vlr_IMC >= 35) and (vlr_IMC < 40):
    interpretacao = "Obesidade grau II"

print("\n")
print(f"Nome do Paciente.....: {paciente}")
print(f"Peso Corporal........: {pc:.3f} kg")
print(f"Altura...............: {alt:.2f} m")
print(f"IMC..................: {vlr_IMC:.2f} - {interpretacao}")