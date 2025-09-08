n = input("Ingresa un número: ")

invertido = ""
for i in range(len(n)-1, -1, -1):
    invertido += n[i]

print("Número invertido:", invertido)
