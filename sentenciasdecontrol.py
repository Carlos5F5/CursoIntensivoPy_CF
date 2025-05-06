cantidad1 = int(input("Ingrese la cantidad de productos1: "))
cantidad2 = int(input("Ingrese la cantidad de productos2: "))

cantidad_total = cantidad1 + cantidad2
resta = cantidad_total -5

if cantidad_total > 25:
    print("Cantidad total es: ", cantidad_total)
    print("Cantidad total menos 5 es: ", resta)

elif resta < 10:
    print("La cantidad total es de menos 10 " )