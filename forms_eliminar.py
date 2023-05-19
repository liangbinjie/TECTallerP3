from tkinter import *
from pais import eliminarPais

def form_eliminarPais():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
    idPais = Entry(t)
    idPais.grid(row = 0, column = 1)
    from pais import eliminarPais
    Button(t , text="Consultar", command=lambda: eliminarPais(idPais.get(), t)).grid(row=1,column=1)



def form_eliminarCiudad():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t ,text = "Codigo de ciudad").grid(row=0,column = 0)
    idCiudad = Entry(t)
    idCiudad.grid(row = 0, column = 1)
    from ciudad import eliminarCiudad
    Button(t , text="Consultar", command=lambda: eliminarCiudad(idCiudad.get(), t)).grid(row=1,column=1)


def form_eliminarCliente():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t ,text = "Codigo de cliente").grid(row=0,column = 0)
    idCliente = Entry(t)
    idCliente.grid(row = 0, column = 1)
    from cliente import eliminarCliente
    Button(t , text="Consultar", command=lambda: eliminarCliente(idCliente.get(), t)).grid(row=1,column=1)


def form_eliminarMascota():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t ,text = "Codigo de mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row = 0, column = 1)
    from mascota import eliminarMascotas
    Button(t , text="Consultar", command=lambda: eliminarMascotas(idMascota.get(), t)).grid(row=1,column=1)