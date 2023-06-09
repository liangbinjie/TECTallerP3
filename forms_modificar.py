from tkinter import *


def form_modificarPais():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
    idPais = Entry(t)
    idPais.grid(row = 0, column = 1)
    Label(t, text="Nuevo nombre de pais").grid(row=1, column=0)
    nombre = Entry(t)
    nombre.grid(row = 1, column = 1)
    from pais import modificarPais
    Button(t , text="Modificar", command=lambda: modificarPais(idPais.get(), nombre.get(), t)).grid(row=2,column=1)


def form_modificarCiudad():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Ciudad").grid(row=0,column = 0)
    idCiudad = Entry(t)
    idCiudad.grid(row = 0, column = 1)
    nombre = Entry(t)
    Label(t, text="Nombre nuevo").grid(row=1, column=0)
    nombre.grid(row = 1, column = 1)
    from ciudad import modificarCiudad
    Button(t , text="Modificar", command=lambda: modificarCiudad(idCiudad.get(), nombre.get(), t)).grid(row=2,column=1)

def form_modificarCliente():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Cliente").grid(row=0,column = 0)
    idCliente = Entry(t)
    idCliente.grid(row = 0, column = 1)
    Label(t, text="Nombre nuevo (si aplica)").grid(row=1, column=0)
    nombre = Entry(t)
    nombre.grid(row = 1, column = 1)
    Label(t, text="Direccion nueva (si aplica)").grid(row=2, column=0)
    direccion = Entry(t)
    direccion.grid(row=2, column=1)
    Label(t, text="Codigo de Pais (si aplica)").grid(row=3, column=0)
    codPais = Entry(t)
    codPais.grid(row=3, column = 1)
    Label(t, text="Codigo de ciudad (si aplica)").grid(row=4, column=0)
    codCiudad = Entry(t)
    codCiudad.grid(row=4, column=1)
    Label(t, text="Telefono (si aplica)").grid(row=5, column=0)
    telefono = Entry(t)
    telefono.grid(row=5, column=1)
    from cliente import modificarCliente
    Button(t , text="Modificar", command=lambda: modificarCliente(idCliente.get(), nombre.get(), direccion.get(), codPais.get(), codCiudad.get(), telefono.get(), t)).grid(row=6,column=1)


def form_modificarMascota():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row = 0, column = 1)
    Label(t, text="Nombre nuevo").grid(row=1, column=0)
    nombre = Entry(t)
    nombre.grid(row = 1, column = 1)
    Label(t, text="Castrado (si/no)").grid(row=2, column=0)
    castrado = Entry(t)
    castrado.grid(row=2, column=1)
    from mascota import modificarMascota
    Button(t , text="Consultar", command=lambda: modificarMascota(idMascota.get(), nombre.get(), castrado.get(), t)).grid(row=3,column=1)


def form_modificarVisita():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row = 0, column = 1)
    Label(t, text="Codigo de visita").grid(row=1, column=0)
    codvisita = Entry(t)
    codvisita.grid(row = 1, column = 1)
    Label(t, text="Forma de Pago (01/02)").grid(row=2, column=0)
    formadepago = Entry(t)
    formadepago.grid(row=2, column=1)
    from visitas import ModificarVisita
    Button(t , text="Modificar", command=lambda: ModificarVisita(idMascota.get(), codvisita.get(), formadepago.get())).grid(row=3,column=1)

def form_modificartratamiento():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t,text = "Codigo de tratamiento a modificar:").grid(row=0,column=0)
    Label(t,text = "Precio nuevo del tratamiento:").grid(row=1,column=0)
    Codigotrat = Entry(t)
    Codigotrat.grid(row = 0,column = 1)
    Precio = Entry(t)
    Precio.grid(row = 1,column = 1)
    from tratamiento import modificartrat
    Button(t,text="Modificar", command = lambda: modificartrat(Codigotrat.get(),Precio.get())).grid(row=2,column=1)

def form_modificarmedicacion():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de modificar")
    Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row = 0, column = 1)
    Label(t, text="Codigo de medicacion").grid(row=1, column=0)
    codmed = Entry(t)
    codmed.grid(row = 1, column = 1)
    Label(t, text="Cantidad").grid(row=2, column=0)
    cantidad = Entry(t)
    cantidad.grid(row=2, column=1)
    Label(t, text="Precio").grid(row=3,column=0)
    Precio = Entry(t)
    Precio.grid(row=3,column=1)
    from medicacion import modificarmed
    Button(t , text="Modificar", command=lambda: modificarmed(idMascota.get(), codmed.get(), cantidad.get(),Precio.get())).grid(row=4,column=1)