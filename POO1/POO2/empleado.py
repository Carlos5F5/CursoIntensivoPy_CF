from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, trabajo en {self.cargo}.")





