from tkinter import *

def ventanaPrincipal(self):
    self.master.title("TecnoPETS - Tu Veterinaria de confianza")

    menubar = Menu(self.master)
    self.master.config(menu=menubar)

    # definimos la opcion de mantenimiento
    mantenimiento = vMantenimiento(menubar) # la llamamos de la funcion de mantenimiento

    # Definimos la opcion de reportes
    reportes = vReportes(menubar)

    # definimos la opcion de facturacion
    facturacion = vFacturacion(menubar)
    
# *********** SECCION DE ACERCA DE LA EMPRESA ******************
    informacion = Menu(menubar)
    informacion.add_cascade(label="TecnoPets, 2023, Cartago Calle IC1803")
    informacion.add_separator()
    informacion.add_cascade(label="Desarrollado por:")
    informacion.add_cascade(label="- Binjie Liang")
    informacion.add_cascade(label="- Aaron Moncada")


# ********** SECCION DE LAS DIFERENTES OPCIONES DEL MENU BAR ***************
    menubar.add_cascade(label="Mantenimiento", underline=0, menu=mantenimiento)
    menubar.add_cascade(label="Reportes", underline=0, menu=reportes)
    menubar.add_cascade(label="Facturacion", underline=0, menu=facturacion)
    menubar.add_cascade(label="Acerca De", underline=0, menu=informacion)
    menubar.add_cascade(label="Contacto", underline=0)


# ********** SECCION DE REDES SOCIALES Y LOGO ****************
    self.logo_fb = PhotoImage(file='resources/facebook.png')
    self.logo_ins = PhotoImage(file='resources/instagram.png')
    self.logo_twt = PhotoImage(file="resources/twitter.png")
    self.logo = PhotoImage(file='resources/LOGO.png')

    Label(self.master, image=self.logo_fb).place(x=30, y=550)
    Label(self.master, image=self.logo_ins).place(x=90, y=550)
    Label(self.master, image=self.logo_twt).place(x=150, y=550)
    Label(self.master, image=self.logo).place(x=560, y=550)

# *********** SECCION DE BOTONES DE LOS DIFERENTES MODULOS ************
    self.lugares = PhotoImage(file="resources/lugares.png")
    self.btnLugares = Button(self.master, image=self.lugares)
    self.btnLugares.configure(command= lambda: self.popupLugares(self.btnLugares))
    self.btnLugares.place(x=250,y=30)
    Label(text="Lugares", font=("Arial", 20)).place(x=265, y=168)


    self.clientes = PhotoImage(file="resources/cliente.png")
    self.btnClientes = Button(self.master, image=self.clientes)
    self.btnClientes.configure(command=lambda: self.popupClientes(self.btnClientes))
    self.btnClientes.place(x=450,y=30)
    Label(text="Clientes", font=("Arial", 20)).place(x=465, y=168)

    self.clinica = PhotoImage(file="resources/clinica.png")
    self.btnClinica = Button(self.master, image=self.clinica)
    self.btnClinica.configure(command=lambda: self.popupClinica(self.btnClinica))
    self.btnClinica.place(x=250,y=300)
    Label(text="Clinica", font=("Arial", 20)).place(x=270, y=440)

    self.facturacion = PhotoImage(file="resources/facturacion.png")
    self.btnFacturacion = Button(self.master, image=self.facturacion)
    self.btnFacturacion.configure(command=lambda: self.popupFacturaciones(self.btnFacturacion))
    self.btnFacturacion.place(x=450,y=300)
    Label(text="Facturacion", font=("Arial", 20)).place(x=440, y=440)

def vMantenimiento(padre):
    mantenimiento = Menu(padre)
    insercion = Menu(mantenimiento) # definimos el submenu de insercion
    insercion.add_command(label="Pais")
    insercion.add_command(label="Ciudad")
    insercion.add_command(label="Clientes")
    insercion.add_command(label="Mascotas")
    insercion.add_command(label="Visitas")
    insercion.add_command(label="Tratamientos")
    insercion.add_command(label="Medicacion")

    consulta = Menu(mantenimiento) # definimos el submenu de consulta
    consulta.add_command(label="Pais")
    consulta.add_command(label="Ciudad")
    consulta.add_command(label="Clientes")
    consulta.add_command(label="Mascotas")
    consulta.add_command(label="Visitas")
    consulta.add_command(label="Tratamientos")
    consulta.add_command(label="Medicacion")
    
    modificar = Menu(mantenimiento) # definimos el submenu de insercion
    modificar.add_command(label="Pais")
    modificar.add_command(label="Ciudad")
    modificar.add_command(label="Clientes")
    modificar.add_command(label="Mascotas")
    modificar.add_command(label="Visitas")
    modificar.add_command(label="Tratamientos")
    modificar.add_command(label="Medicacion")

    eliminar = Menu(mantenimiento) # definimos el submenu de consulta
    eliminar.add_command(label="Pais")
    eliminar.add_command(label="Ciudad")
    eliminar.add_command(label="Clientes")
    eliminar.add_command(label="Mascotas")
    eliminar.add_command(label="Visitas")
    eliminar.add_command(label="Tratamientos")
    eliminar.add_command(label="Medicacion")

    mantenimiento.add_cascade(label='Insercion', menu=insercion, underline=0)
    mantenimiento.add_cascade(label='Consulta', menu=consulta, underline=0)
    mantenimiento.add_cascade(label='Modificar', menu=modificar, underline=0)
    mantenimiento.add_cascade(label='Eliminar', menu=eliminar, underline=0)

    return mantenimiento

def vReportes(padre):
    reportes = Menu(padre)
    # opcion1 = Menu(reportes) # Definimos opcion 1
    # opcion1.add_command(label="Reportes")
    # opcion1.add_command(label="Opcion2")
    # opcion1.add_command(label="Opcion3")

    # opcion2 = Menu(reportes) # Defininimos opcion 2
    # opcion2.add_command(label="Opcion1")
    # opcion2.add_command(label="Opcion2")
    # opcion2.add_command(label="Opcion3")

    reportes.add_command(label="Reportes Solicitados", underline=0)
    # reportes.add_cascade(label="Opcion 2", menu=opcion2, underline=0)

    return reportes

def vFacturacion(padre):
    facturacion = Menu(padre)
    opcion1 = Menu(facturacion) # Definimos opcion 1
    opcion1.add_command(label="Saldos")
    opcion1.add_command(label="Descuentos")
    opcion1.add_command(label="Facturacion")

    opcion2 = Menu(facturacion) # Defininimos opcion 2
    opcion2.add_command(label="Opcion1")
    opcion2.add_command(label="Opcion2")
    opcion2.add_command(label="Opcion3")

    facturacion.add_cascade(label="Saldos", menu=opcion2, underline=0)
    facturacion.add_cascade(label="Descuentos", menu=opcion2, underline=0)
    facturacion.add_cascade(label="Facturacion", menu=opcion2, underline=0)

    return facturacion