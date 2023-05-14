from tkinter import *

def formulario_insercionpais(self):
    t = Toplevel(self)
    t.geometry("300x150")
    t.title("Formulario de insercion")
    Label(t ,text = "Codigo de pais").grid(row=0,column = 0)
    Label(t ,text = "Nombre").grid(row=1,column = 0)
    Codigo_de_pais = Entry(t).grid(row = 0, column = 1)
    nombre = Entry(t).grid(row = 1,column = 1)
    Button(t , text="Guardar").grid(row=2,column=1)

def formulario_contacto(self):
    """
    Popup para el formulario de contacto
    Tiene los Entries de nombre, correo, telefono y comentarios
    """
    t = Toplevel(self)
    t.geometry("300x150")
    t.title("Formulario de Contacto")
    Label(t ,text = "Nombre").grid(row = 0,column = 0)
    Label(t ,text = "Correo").grid(row = 1,column = 0)
    Label(t ,text = "Telefono").grid(row = 2,column = 0)
    Label(t ,text = "Comentarios", height=2).grid(row = 3,column = 0)
    nombre = Entry(t)
    nombre.grid(row = 0,column = 1)
    correo = Entry(t)
    correo.grid(row = 1,column = 1)
    telefono = Entry(t)
    telefono.grid(row = 2,column = 1)
    comentarios = Entry(t)
    comentarios.grid(row = 3,column = 1)
    Button(t ,text="Guardar").grid(row=4,column=1)