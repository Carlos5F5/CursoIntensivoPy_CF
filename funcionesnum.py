""" n1 = int(input("Escribe un número: "))
n2 = int(input("Escribe otro número: "))
n3 = int(input("Escribe otro número: "))


def suma(c1, c2, a3):
    print("La suma es: ", c1 + c2 + a3)

suma(n1, n2, n3)
 """

def suma(valor1, valor2, valor3):

    r = valor1 + valor2 + valor3
    p = r / 3 
    return r

try:
    n1 = int(input("Escribe el número 1: "))
    n2 = int(input("Escribe el número 2: "))
    n3 = int(input("Escribe el número 3: "))

    r = suma(n1, n2, n3)

except ValueError:
    print("Error: Debes ingresar un número entero.")

print ("La suma es: ", r)
print ("El promedio es: ", r/3)