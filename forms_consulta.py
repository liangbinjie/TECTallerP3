from tkinter import *



def formulario_consultapais():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de consulta")
    Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
    idPais = Entry(t)
    idPais.grid(row = 0, column = 1)
    from pais import consultarPais
    Button(t , text="Consultar", command=lambda: consultarPais(idPais.get())).grid(row=1,column=1)

def formulario_consultaCiudad():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de consulta")
    Label(t ,text = "Codigo de Ciudad").grid(row=1,column = 0)
    codCiudad = Entry(t)
    codCiudad.grid(row = 1, column = 1)
    from ciudad import consultarCiudad
    Button(t , text="Consultar", command=lambda: consultarCiudad(codCiudad.get())).grid(row=2,column=1)

def formulario_consultaCliente():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de consulta")
    Label(t ,text = "ID Cliente").grid(row=0,column = 0)

    idCliente = Entry(t)
    idCliente.grid(row = 0, column = 1)
    from cliente import consultarCliente
    Button(t , text="Consultar", command=lambda:consultarCliente(idCliente.get())).grid(row=3,column=1)

def formulario_consultaMascota():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de consulta")
    Label(t ,text = "Codigo de Mascota").grid(row=1,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row = 1, column = 1)
    from mascota import consultarMascota
    Button(t , text="Consultar", command=lambda: consultarMascota(idMascota.get())).grid(row=2,column=1)
