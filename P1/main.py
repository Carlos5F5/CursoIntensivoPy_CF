import tkinter as tk
from tkinter import Menu
from mantenimiento_empleado import ManteniemientoEmpleado


class MainaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Principal")
        self.geometry("600x400")

        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        self.desktop_frame = tk.Frame(self)
        self.desktop_frame.pack(expand=True, fill="both")

        empleados_menu = Menu(self.menu_bar, tearoff=0)
        empleados_menu.add_command(label="Abrir Formulario", command=self.abrir_empleados)
        self.menu_bar.add_cascade(label="Empleados", menu=empleados_menu)

    def abrir_empleados(self):
        for widget in self.desktop_frame.winfo_children():
            widget.destroy()

        ventana = ManteniemientoEmpleado(self.desktop_frame)
        ventana.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainaApp()
    app.mainloop()

