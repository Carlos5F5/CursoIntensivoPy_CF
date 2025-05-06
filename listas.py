persona = ["Antes de la crisis", "Juan", 30, 1.60]

print("El nombre es ", persona)

persona.remove("Antes de la crisis")
persona.append("Es novio de Andrea")
persona.insert(2, "No le cocina")

print("Despues de la crisis", persona)

andrea = input("Escribe caracteristicas de Andrea: ")

persona.append(andrea)
print("Caracteristicas de Adrea",persona)
