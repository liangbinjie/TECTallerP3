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


def form_eliminarmedicamento():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t,text = "Codigo de medicamento a eliminar:").grid(row=0,column=0)
    CodigoMed = Entry(t)
    CodigoMed.grid(row = 0,column = 1)
    from medicacion import eliminarmed
    Button(t,text="Eliminar", command = lambda: eliminarmed(CodigoMed.get())).grid(row=1,column=1)


def form_eliminarvisita():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t,text = "Codigo de visita a eliminar:").grid(row=0,column=0)
    Codigovisita = Entry(t)
    Codigovisita.grid(row = 0,column = 1)
    from visitas import eliminarvisita
    Button(t,text="Eliminar", command = lambda: eliminarvisita(Codigovisita.get())).grid(row=1,column=1)

def form_eliminartratamiento():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de eliminar")
    Label(t,text = "Codigo de tratamiento a eliminar:").grid(row=0,column=0)
    Codigotrat = Entry(t)
    Codigotrat.grid(row = 0,column = 1)
    from tratamiento import eliminartrat
    Button(t,text="Eliminar", command = lambda: eliminartrat(Codigotrat.get())).grid(row=1,column=1)
