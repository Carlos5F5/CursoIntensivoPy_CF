def suma (n1,n2):
    r = n1 + n2
    return r

def resta (n1,n2):
    r = n1 - n2
    return r

def multiplicacion (n1,n2):
    r = n1 * n2
    return r

def division (n1,n2):
    r = n1 / n2
    return r 

while True:
    try:
        num1 = int(input("Escribe el número 1: "))
        num2 = int(input("Escribe el número 2: "))

        rSuma = suma(num1, num2)
        print("La suma es: ", rSuma)


        rResta = resta(num1, num2)
        print("La resta es: ", rResta)

        rMultiplicacion = multiplicacion(num1, num2)
        print("La multiplicación es: ", rMultiplicacion)

        rDivision = division(num1, num2)
        print("La división es: ", rDivision)
        break
    
    except ValueError:
        print("Error: Debes ingresar un número entero.")