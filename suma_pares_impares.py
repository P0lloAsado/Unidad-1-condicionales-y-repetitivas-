suma_pares=0
suma_impares=0
n = int(input("Ingresa un numero: "))
for i in range (1, n + 1):
    if i % 2 == 0:
        suma_pares = suma_pares + i
    else:
        suma_impares = suma_impares + i
print("el total de los numeros pares es: ", suma_pares)
print("el total de los numeros impares es: ", suma_impares)
