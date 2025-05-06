frase = "La mejor contraseña es 12345678"
print("La frase es: ", frase)
print(len(frase)) # longitud de la frase

 
slicing = frase[0:5] # slicing de la frase
print("El slicing es: ", slicing) # slicing de la frase

champaa = input("Escribe la clave: ") # clave de la frase  
if champaa in frase: 
    print("la palabra", champaa,"está en la frase", "y la frase completa es:", frase)
else:
    print("la palabra ", champaa," no está en la frase")
