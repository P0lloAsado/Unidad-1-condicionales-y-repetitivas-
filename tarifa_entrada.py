edad= int(input("ingresa tu edad: "))
if edad <= 12:
    print("Pagas $50")
elif edad > 12 and edad <= 17:
    print("Pagas $80")
else:
    print("Pagas $120")