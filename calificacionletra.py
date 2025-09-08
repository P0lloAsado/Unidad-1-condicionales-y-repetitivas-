cal=int(input("Ingresa una calificacion: "))
if cal <= 60:
    print("F")
elif cal > 60 and cal<=69:
    print("D")
elif cal > 70 and cal<=79:
    print("C")
elif cal > 80 and cal<=89:
    print("B")
elif cal > 90 and cal<=100:
    print("A")
else: 
    print("dato incorrecto")