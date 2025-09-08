l1 = int(input("Ingresa la 1era longitud: "))
l2 = int(input("Ingresa la 2da longitud: "))
l3 = int(input("Ingresa la 3era longitud: "))
if l1 ==l2 and l1== l3:
    print("Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Isosceles")
else:
    print("Escaleno")
 