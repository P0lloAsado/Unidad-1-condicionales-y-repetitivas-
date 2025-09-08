n1= int(input("Ingresa un numero: "))
n2= int(input("Ingresa otro numero: "))
n3= int(input("Ingresa otro numero: "))
if n1 > n2 and n1 > n3:
    print("el numero mayor es: ", n1)
elif n2 > n1 and n2 > n3:
    print("el numero mayor es: ", n2)
else:
    print("el numero mayor es: ", n3)