from tkinter import *

def formulario_insercionpais():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de insercion")
    Label(t ,text = "Codigo de pais").grid(row=0,column = 0)
    Label(t ,text = "Nombre").grid(row=1,column = 0)
    idPais = Entry(t)
    idPais.grid(row = 0, column = 1)
    nombre = Entry(t)
    nombre.grid(row = 1,column = 1)
    from pais import addPais
    Button(t , text="Guardar", command=lambda: addPais(idPais.get(), nombre.get()) ).grid(row=2,column=1)