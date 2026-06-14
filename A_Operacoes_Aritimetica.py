a = int(input("a:"))
b = int(input("b:"))

soma = a + b
sub = a - b
mult = a * b
divInt = a // b
resto = a % b
divReal = a / b

print()
print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {sub}")
print(f"{a} * {b} = {mult}")
print(f"{a} // {b} = {divInt} divisão inteira")
print(f"{a} % {b} = {resto} resto da divisão inteira")
print(f"{a} / {b} = {divReal} divisão real")