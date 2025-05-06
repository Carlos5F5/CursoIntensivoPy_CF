from persona import Persona
from cuenta_bancaria import CuentaBancaria
from empleado import Empleado
from animal import Perro, Gato 

#Persona
p = Persona("Andrea", 20)
p.saludar()

#CuentaBancaria
cuenta = CuentaBancaria("Andrea", 1000)
cuenta.depositar(500)
cuenta.mostrar_saldo()

#Empleado
e = Empleado("Carlos", 32, "Conserje")
e.presentarse()


#Animal

animales = [Perro(), Gato()]
for animal in animales:
    animal.hablar()

