import tkinter as tk

class ManteniemientoEmpleado(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(borderwidth=2, relief="groove")
        
        tk.Label(self, text="Formulario de Mantenimiento de Empleado").pack(pady=10)



        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        tk.Label(self, text="Cargo").pack()
        self.cargo_entry = tk.Entry(self)
        self.cargo_entry.pack()
        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)

    def guardar(self):
        nombre = self.nombre_entry.get()
        cargo = self.cargo_entry.get()
        print(f"Nombre: {nombre}, Cargo: {cargo}")
            
class ManteniemientoEmpleado(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(borderwidth=2, relief="groove")
        
        tk.Label(self, text="Formulario de Mantenimiento de Empleado").pack(pady=10)



        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        tk.Label(self, text="Cargo").pack()
        self.cargo_entry = tk.Entry(self)
        self.cargo_entry.pack()
        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)

    def guardar(self):
        nombre = self.nombre_entry.get()
        cargo = self.cargo_entry.get()
        print(f"Nombre: {nombre}, Cargo: {cargo}")

class ManteniemientoEmpleado(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(borderwidth=2, relief="groove")
        
        tk.Label(self, text="Formulario de Mantenimiento de Empleado").pack(pady=10)



        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        tk.Label(self, text="Cargo").pack()
        self.cargo_entry = tk.Entry(self)
        self.cargo_entry.pack()
        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)

    def guardar(self):
        nombre = self.nombre_entry.get()
        cargo = self.cargo_entry.get()
        print(f"Nombre: {nombre}, Cargo: {cargo}")
            