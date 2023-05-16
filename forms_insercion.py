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

def formulario_insercionciudad():
    t = Toplevel()
    t.geometry("300x250")
    t.title("Formulario de insercion")
    Label(t ,text = "Codigo de pais").grid(row=0,column = 0)
    Label(t ,text = "Codigo de ciudad").grid(row=1,column =0)
    Label(t ,text = "Nombre").grid(row=2,column = 0)
    codPais = Entry(t)
    codPais.grid(row = 0, column = 1)
    codCiudad = Entry(t)
    codCiudad.grid(row = 1,column = 1)
    nombre = Entry(t)
    nombre.grid(row = 2,column = 1)
    from ciudad import addCiudad
    Button(t , text="Guardar", command=lambda: addCiudad(codPais.get(), codCiudad.get(), nombre.get())).grid(row=3,column=1)

def formulario_insercioncliente():
    t = Toplevel()
    t.geometry("300x300")
    t.title("Formulario de insercion")
    Label(t ,text = "ID").grid(row=0,column = 0)
    Label(t, text= "Nombre").grid(row=1, column=0) 
    Label(t, text= "Direccion").grid(row=2, column=0) 
    Label(t, text= "ID Pais").grid(row=3, column=0) 
    Label(t, text= "ID Ciudad").grid(row=4, column=0)
    Label(t, text= "Telefono").grid(row=5, column=0)
    Label(t, text= "Fecha (DD-MM-YY)").grid(row=6, column=0)
    Label(t, text= "Descuento").grid(row=7, column=0)
    Label(t, text= "Saldo").grid(row=8, column=0)
    idCliente = Entry(t)
    idCliente.grid(row=0, column=1)
    nombre = Entry(t)
    nombre.grid(row=1, column=1)
    direccion = Entry(t)
    direccion.grid(row=2, column=1)
    pais = Entry(t)
    pais.grid(row=3, column=1)
    ciudad = Entry(t)
    ciudad.grid(row=4, column=1)
    telefono = Entry(t)
    telefono.grid(row=5, column=1)
    fecha = Entry(t)
    fecha.grid(row=6, column=1)
    descuento = Entry(t)
    descuento.grid(row=7, column=1)
    saldo = Entry(t)
    saldo.grid(row=8, column=1)

    from cliente import addCliente
    Button(t , text="Guardar", command=lambda: addCliente(idCliente.get(), nombre.get(), direccion.get(), pais.get(), ciudad.get(), telefono.get(), fecha.get(), descuento.get(), saldo.get())).grid(row=9,column=1)

def formulario_insercionmascota():
    t = Toplevel()
    t.geometry("350x300")
    t.title("Formulario de insercion")
    Label(t ,text = "ID Cliente").grid(row=0,column = 0)
    Label(t ,text = "ID mascota").grid(row=1,column = 0)
    
    Label(t ,text = "Nombre").grid(row=2,column = 0)
    Label(t ,text = "Tipo de mascota").grid(row=3,column = 0)
    Label(t ,text = "Raza").grid(row=4,column = 0)
    Label(t ,text = "Fecha de Nacimiento (DD-MM-YY)").grid(row=5,column = 0)
    Label(t ,text = "Sexo").grid(row=6,column = 0)
    Label(t ,text = "Color").grid(row=7,column = 0)
    Label(t ,text = "Castrado").grid(row=8,column = 0)
    Label(t ,text = "Fecha Ultima visita (DD-MM-YY)").grid(row=9,column = 0)
    idCliente = Entry(t)
    idCliente.grid(row = 0, column = 1)
    idMascota = Entry(t)
    idMascota.grid(row = 1,column = 1)
    nombre = Entry(t)
    nombre.grid(row = 2,column = 1)
    tipoMascota = Entry(t)
    tipoMascota.grid(row = 3,column = 1)
    raza = Entry(t)
    raza.grid(row = 4,column = 1)
    fechaN = Entry(t)
    fechaN.grid(row = 5,column = 1)
    sexo = Entry(t)
    sexo.grid(row = 6,column = 1)
    color = Entry(t)
    color.grid(row = 7,column = 1)
    castrado = Entry(t)
    castrado.grid(row = 8,column = 1)
    fechaUltima = Entry(t)
    fechaUltima.grid(row = 9,column = 1)
    from mascota import addMascota
    Button(t , text="Guardar", command=lambda: addMascota(idCliente.get(), idMascota.get(), nombre.get(), tipoMascota.get(), raza.get(),fechaN.get(), sexo.get(), color.get(),castrado.get(), fechaUltima.get())).grid(row=10,column=1)


# agregar insercion visita, tratamiento, medicamento

def formulario_insercionvisita():
        t = Toplevel()
        t.geometry("300x150")
        t.title("Formulario de insercion")
        Label(t ,text = "Codigo de visita").grid(row=0,column = 0)
        
        Label(t ,text = "Codigo de Animal").grid(row=1,column = 0)
        Label(t ,text = "Fecha de ultima visita").grid(row=2,column = 0)
        Label(t ,text = "Total Factura").grid(row=3,column = 0)
        Label(t ,text = "Forma de Pago").grid(row=4,column = 0)

        CodigoDeVisita = Entry(t)
        CodigoDeVisita.grid(row = 0, column = 1)
        CodigoDeAnimal = Entry(t)
        CodigoDeAnimal.grid(row = 1,column = 1)

        FechaUltimaVisita = Entry(t)
        FechaUltimaVisita.grid(row = 2,column = 1)
        TotalFactura = Entry(t)
        TotalFactura.grid(row = 3,column = 1)
        FormaDePago = Entry(t)
        FormaDePago.grid(row = 4,column = 1)

        from visitas import insercionvisita

        Button(t , text="Guardar", command = lambda: insercionvisita(CodigoDeVisita.get(), CodigoDeAnimal.get(), FechaUltimaVisita.get(), TotalFactura.get(), FormaDePago.get()) ).grid(row=5,column=1)

def formulario_inserciontratamiento():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Formulario de insercion")
    Label(t ,text = "Codigo de Tratamiento").grid(row=0,column = 0)
    Label(t ,text = "Nombre").grid(row=1,column = 0)
    Label(t ,text = "Precio Unitario").grid(row=2,column = 0)
    Label(t ,text = "Cantidad").grid(row=3,column = 0)
    CodigoDeTratamiento = Entry(t)
    CodigoDeTratamiento.grid(row = 0, column = 1)
    nombre = Entry(t)
    nombre.grid(row = 1,column = 1)
    PrecioUnitario = Entry(t)
    PrecioUnitario.grid(row = 2,column = 1)
    Cantidad = Entry(t)
    Cantidad.grid(row = 3,column = 1)

    from tratamiento import inserciontratamiento

    Button(t , text="Guardar", command = lambda: inserciontratamiento(CodigoDeTratamiento.get(),nombre.get(),PrecioUnitario.get(),Cantidad.get())).grid(row=4,column=1)

def formulario_insercionMedicacion():
    t = Toplevel()
    t.geometry("300x200")
    t.title("Formulario de insercion")
    Label(t ,text = "Codigo del Animal").grid(row=0,column = 0)
    Label(t ,text = "Codigo de Medicacion").grid(row=1,column = 0)
    Label(t ,text = "Fecha de Ultima Visita").grid(row=2, column = 0)
    Label(t ,text = "Lista de Medicamentos").grid(row=3, column = 0)
    Label(t ,text = "Costo unitario").grid(row=4, column = 0)
    Label(t ,text = "Cantidad").grid(row=5, column = 0)
    Label(t ,text = "Costo total").grid(row=6, column = 0)

    Codigo_de_Animal = Entry(t)
    Codigo_de_Animal.grid(row = 0, column = 1)
    codigoDeMedicacion = Entry(t)
    codigoDeMedicacion.grid(row = 1,column = 1)
    FechaDeUltimaVisita = Entry(t)
    FechaDeUltimaVisita.grid(row = 2,column = 1)
    ListaDeMedicamentos = Entry(t)
    ListaDeMedicamentos.grid(row = 3,column = 1)
    CostoUnitario = Entry(t)
    CostoUnitario.grid(row = 4,column = 1)
    Cantidad = Entry(t)
    Cantidad.grid(row = 5,column = 1)
    CostoTotal = Entry(t)
    CostoTotal.grid(row = 6,column = 1)

    from medicacion import insercionmedicacion

    Button(t , text="Guardar", command = lambda: insercionmedicacion(Codigo_de_Animal.get(),codigoDeMedicacion.get(),FechaDeUltimaVisita.get(),ListaDeMedicamentos.get(),CostoUnitario.get(),Cantidad.get(),CostoTotal.get())).grid(row=7,column=1)