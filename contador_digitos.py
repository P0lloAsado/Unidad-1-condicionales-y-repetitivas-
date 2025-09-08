n = int(input("Ingresa un número: "))
n = abs(n)  
contador = 0

if n == 0:
    contador = 1
else:
    while n > 0:
        n //= 10     
        contador += 1

print("El número tiene", contador, "dígitos.")
