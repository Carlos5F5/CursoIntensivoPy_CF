libros = ["romance", "fantasy", "horror", "science fiction"]

opcion = 0 
opcion = int(input("Elige una opción: "))
while True:
    print("*******\nSistema de Operaciones CRUD*******")
    print("1. Mostrar todos los libros")
    print("2. Actualizar un libro")
    print("3. Eliminar un libro")
    print("4. Salir")

    if opcion == 1:
        print("Los libros son: ", libros)
    elif opcion == 2:
        act_libro = input("Nuevo libro es: ")
        act_libro = libros.append(act_libro)
        print("Libros actualizados son: ", libros)
    elif opcion == 3:
        opcion = int(input("Elige una opción: "))

        act_libro = input("Escribe el libro a eliminar: ")
        print("libros",libros)
        if act_libro in libros: 
            libros.remove(act_libro)
            print("Libro eliminado: ", act_libro)
            print("Libros actualizados son: ", libros)
        else: 
            print("Gracias")

    break

