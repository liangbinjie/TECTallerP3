from variables import LISTA_CONTACTO
from tkinter import messagebox

def guardarContacto(nombre, correo, telefono, comentarios):
    LISTA_CONTACTO.append([nombre, correo, telefono, comentarios])
    messagebox.showinfo("Message", "Contacto guardado, ya puede cerrar el formulario")
    print(LISTA_CONTACTO)