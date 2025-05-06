""" persona = {
    "Andrea": "Mujer", 
    "Edad": 20,
    "Estatura": 1.50,
    "Profesion":"Ingeniera"
}
print(persona.items()) # Muestra las claves del diccionario

persona.update({"Esposo": "Juan"}) # Agrega un nuevo elemento al diccionario

print(persona) # Muestra las claves del diccionario

persona ["carro"] = "Tsuru"

persona.pop("Esposo") 


for clave, valor in persona.items():
    print(clave, ":", valor)
 """


calificaciones = (10, 8, 9, 7)
print(type(calificaciones))
print(calificaciones)


listacalificaciones = list(calificaciones) # Convierte la tupla en una lista
print(type(listacalificaciones))


listacalificaciones.insert(5, 10)
print(listacalificaciones)


