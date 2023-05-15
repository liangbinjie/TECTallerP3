from tkinter import *
from toolbar import *
from forms_consulta import *

class App(Frame):
    def __init__(self):
        super().__init__()

        self.ventanaPrincipal()


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


    # ********** SECCION DE LAS DIFERENTES OPCIONES DEL TOOLBAR ***************
        menubar.add_cascade(label="Mantenimiento", underline=0, menu=mantenimiento)
        menubar.add_cascade(label="Reportes", underline=0, menu=reportes)
        menubar.add_cascade(label="Facturacion", underline=0, menu=facturacion)
        menubar.add_cascade(label="Acerca De", underline=0, menu=informacion)
        menubar.add_cascade(label="Contacto", underline=0, command=self.formulario_contacto)


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


    def popupLugares(self, btn):
        self.popup = Menu(self.master, tearoff=0)
        self.popupPaises = Menu(self.popup)
        self.popupPaises.add_command(label="Insercion",command= formulario_insercionpais)
        self.popupPaises.add_command(label="Consultar",command= formulario_consultapais)
        self.popupPaises.add_command(label="Eliminar",command = self.formulario_eliminacionpais)
        self.popupPaises.add_command(label="Modificar",command = self.formulario_modificacionpais)
        self.popup.add_cascade(label="Paises", menu=self.popupPaises)
        self.popupCiudades = Menu(self.popup)
        self.popupCiudades.add_command(label="Insercion",command = formulario_insercionciudad)
        self.popupCiudades.add_command(label="Consultar",command = formulario_consultaCiudad)
        self.popupCiudades.add_command(label="Eliminar",command = self.formulario_eliminacionciudad)
        self.popupCiudades.add_command(label="Modificar",command = self.formulario_modificacionciudad)
        self.popup.add_cascade(label="Ciudades", menu=self.popupCiudades)

        try:         
            x = btn.winfo_rootx()
            y = btn.winfo_rooty()
            self.popup.tk_popup(x+128, y, 0)
        finally:
            self.popup.grab_release()

    def popupClinica(self, btn):
        self.popup = Menu(self.master, tearoff=0)
        self.popupTratamientos = Menu(self.popup)
        self.popupTratamientos.add_command(label="Insercion",command = self.formulario_inserciontratamiento)
        self.popupTratamientos.add_command(label="Consultar",command = self.formulario_consultaTratamiento)
        self.popupTratamientos.add_command(label="Eliminar",command = self.formulario_eliminacionTratamiento)
        self.popupTratamientos.add_command(label="Modificar",command = self.formulario_modificaciontratamiento)
        self.popup.add_cascade(label="Tratamientos", menu=self.popupTratamientos)
        self.popupMedicamentos = Menu(self.popup)
        self.popupMedicamentos.add_command(label="Insercion",command = self.formulario_insercionmedicacion)
        self.popupMedicamentos.add_command(label="Consultar",command = self.formulario_consultaMedicacion)
        self.popupMedicamentos.add_command(label="Eliminar",command = self.formulario_eliminacionMedicacion)
        self.popupMedicamentos.add_command(label="Modificar", command = self.formulario_modificacionMedicacion)
        self.popup.add_cascade(label="Medicamentos", menu=self.popupMedicamentos)

        try:         
            x = btn.winfo_rootx()
            y = btn.winfo_rooty()
            self.popup.tk_popup(x+128, y, 0)
        finally:
            self.popup.grab_release()

    def popupClientes(self, btn):
        self.popup = Menu(self.master, tearoff=0)
        self.popupCliente = Menu(self.popup)
        self.popupCliente.add_command(label="Insercion",command = formulario_insercioncliente)
        self.popupCliente.add_command(label="Consultar",command = formulario_consultaCliente)
        self.popupCliente.add_command(label="Eliminar",command = self.formulario_eliminacionCliente)
        self.popupCliente.add_command(label="Modificar",command = self.formulario_modificacionCliente)
        self.popup.add_cascade(label="Clientes", menu=self.popupCliente)

        self.popupMascotas = Menu(self.popup)
        self.popupMascotas.add_command(label="Insercion",command = formulario_insercionmascota)
        self.popupMascotas.add_command(label="Consultar",command = formulario_consultaMascota)
        self.popupMascotas.add_command(label="Eliminar",command = self.formulario_eliminacionMascota)
        self.popupMascotas.add_command(label="Modificar",command = self.formulario_modificacionmascota)
        self.popup.add_cascade(label="Mascotas", menu=self.popupMascotas)

        self.popupVisitas = Menu(self.popup)
        self.popupVisitas.add_command(label="Insercion",command = self.formulario_insercionvisita)
        self.popupVisitas.add_command(label="Consultar",command = self.formulario_consultaVisita)
        self.popupVisitas.add_command(label="Eliminar") #No estoy seguro pero no decia que sucedia si se elimina visita en las especificaciones.
        self.popupVisitas.add_command(label="Modificar", command = self.formulario_modificacionvisita)
        self.popup.add_cascade(label="Visitas", menu=self.popupVisitas)

        try:         
            x = btn.winfo_rootx()
            y = btn.winfo_rooty()
            self.popup.tk_popup(x+128, y, 0)
        finally:
            self.popup.grab_release()

    def popupFacturaciones(self, btn):
        self.popup = Menu(self.master, tearoff=0)
        self.popupFacturacion = Menu(self.popup)
        self.popupFacturacion.add_command(label="Insercion")
        self.popupFacturacion.add_command(label="Consultar")
        self.popupFacturacion.add_command(label="Eliminar")
        self.popupFacturacion.add_command(label="Modificar")
        self.popup.add_cascade(label="Facturacion", menu=self.popupFacturacion)

        self.popupDescuento = Menu(self.popup)
        self.popupDescuento.add_command(label="Insercion")
        self.popupDescuento.add_command(label="Consultar")
        self.popupDescuento.add_command(label="Eliminar")
        self.popupDescuento.add_command(label="Modificar")
        self.popup.add_cascade(label="Descuento", menu=self.popupDescuento)

        self.popupSaldo = Menu(self.popup)
        self.popupSaldo.add_command(label="Insercion")
        self.popupSaldo.add_command(label="Consultar")
        self.popupSaldo.add_command(label="Eliminar")
        self.popupSaldo.add_command(label="Modificar")
        self.popup.add_cascade(label="Saldo", menu=self.popupSaldo)

        try:         
            x = btn.winfo_rootx()
            y = btn.winfo_rooty()
            self.popup.tk_popup(x+128, y, 0)
        finally:
            self.popup.grab_release()


# ********** SECCION FORMULARIOS ***************

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
        from datos import guardarContacto
        Button(t ,text="Guardar", command= lambda: guardarContacto(nombre.get(), correo.get(), telefono.get(), comentarios.get())).grid(row=4,column=1)

    def formulario_insercionvisita(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de insercion")
        Label(t ,text = "Codigo de visita").grid(row=0,column = 0)
        
        Label(t ,text = "Codigo de Animal").grid(row=1,column = 0)
        Label(t ,text = "Fecha de ultima visita").grid(row=2,column = 0)
        Label(t ,text = "Total Factura").grid(row=3,column = 0)
        Label(t ,text = "Forma de Pago").grid(row=4,column = 0)

        CodigoDeVisita = Entry(t).grid(row = 0, column = 1)
        CodigoDeAnimal = Entry(t).grid(row = 1,column = 1)

        FechaUltimaVisita = Entry(t).grid(row = 2,column = 1)
        TotalFactura = Entry(t).grid(row = 3,column = 1)
        FormaDePago = Entry(t).grid(row = 4,column = 1)


        Button(t , text="Guardar").grid(row=5,column=1)

    def formulario_inserciontratamiento(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de insercion")
        Label(t ,text = "Codigo de Tratamiento").grid(row=0,column = 0)
        Label(t ,text = "Nombre").grid(row=1,column = 0)
        Label(t ,text = "Precio Unitario").grid(row=2,column = 0)
        Label(t ,text = "Cantidad").grid(row=3,column = 0)
        CodigoDeTratamiento = Entry(t).grid(row = 0, column = 1)
        nombre = Entry(t).grid(row = 1,column = 1)
        PrecioUnitario = Entry(t).grid(row = 2,column = 1)
        Cantidad = Entry(t).grid(row = 3,column = 1)




        Button(t , text="Guardar").grid(row=4,column=1)



    def formulario_insercionmedicacion(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de insercion")
        Label(t ,text = "Codigo del Animal").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Medicacion").grid(row=1,column = 0)
        Label(t ,text = "Fecha de Ultima Visita").grid(row=2, column = 0)
        Label(t ,text = "Lista de Medicamentos").grid(row=3, column = 0)
        Label(t ,text = "Costo unitario").grid(row=4, column = 0)
        Label(t ,text = "Cantidad").grid(row=5, column = 0)
        Label(t ,text = "Costo total").grid(row=6, column = 0)

        Codigo_de_Animal = Entry(t).grid(row = 0, column = 1)
        codigoDeMedicacion = Entry(t).grid(row = 1,column = 1)
        FechaDeUltimaVisita = Entry(t).grid(row = 2,column = 1)
        ListaDeMedicamentos = Entry(t).grid(row = 3,column = 1)
        CostoUnitario = Entry(t).grid(row = 4,column = 1)
        Cantidad = Entry(t).grid(row = 5,column = 1)
        CostoTotal = Entry(t).grid(row = 6,column = 1)


        Button(t , text="Guardar").grid(row=7,column=1)


# ************* SECCION FORMULARIOS DE CONSULTA ***************

    def formulario_consultapais(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
        idPais = Entry(t)
        idPais.grid(row = 0, column = 1)
        from pais import consultarPais
        Button(t , text="Consultar", command=lambda: consultarPais(idPais.get())).grid(row=1,column=1)

    def formulario_consultaCiudad(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Ciudad").grid(row=1,column = 0)
        codCiudad = Entry(t)
        codCiudad.grid(row = 1, column = 1)
        from ciudad import consultarCiudad
        Button(t , text="Consultar", command=lambda: consultarCiudad(codCiudad.get())).grid(row=2,column=1)

    def formulario_consultaCliente(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "ID Cliente").grid(row=0,column = 0)

        idCliente = Entry(t)
        idCliente.grid(row = 0, column = 1)
        from cliente import consultarCliente
        Button(t , text="Consultar", command=lambda:consultarCliente(idCliente.get())).grid(row=3,column=1)

    def formulario_consultaMascota(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Mascota").grid(row=1,column = 0)
        idMascota = Entry(t)
        idMascota.grid(row = 1, column = 1)
        from mascota import consultarMascota
        Button(t , text="Consultar", command=lambda: consultarMascota(idMascota.get())).grid(row=2,column=1)

    def formulario_consultaVisita(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Visita").grid(row=1,column = 0)
        Codigo_de_Mascota = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Visita = Entry(t).grid(row = 1, column = 1)
        Button(t , text="Consultar").grid(row=2,column=1)

    def formulario_consultaTratamiento(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Tratamiento").grid(row=0,column = 0)
        Codigo_de_tratamiento = Entry(t).grid(row = 0, column = 1)
        Button(t , text="Consultar").grid(row=2,column=1)

    def formulario_consultaMedicacion(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de consulta")
        Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Medicacion").grid(row = 1,column = 0)
        Codigo_de_Mascota = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Medicacion = Entry(t).grid(row = 1, column = 1)
        Button(t , text="Consultar").grid(row=2,column=1)


    def formulario_eliminacionpais(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        
        Button(t , text="Eliminar").grid(row=1,column=1)

    def formulario_eliminacionciudad(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Ciudad a eliminar").grid(row=1,column = 0)
        Label(t ,text = "Codigo de Pais nuevo").grid(row=2,column = 0)
        Label(t ,text = "Codigo de Ciudad nuevo").grid(row=3,column = 0)
        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Ciudadeliminar = Entry(t).grid(row = 1, column = 1)
        Codigo_de_Paisnuevo = Entry(t).grid(row = 2, column = 1)
        Codigo_de_Ciudadnuevo = Entry(t).grid(row = 3, column = 1)
        
        Button(t , text="Eliminar").grid(row=4,column=1)
    
    def formulario_eliminacionCliente(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Cliente").grid(row=0,column = 0)
        Codigo_de_Cliente = Entry(t).grid(row = 0, column = 1)
        
        Button(t , text="Eliminar").grid(row=1,column=1)    


    def formulario_eliminacionMascota(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Mascota").grid(row=0,column = 0)
        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        
        Button(t , text="Eliminar").grid(row=1,column=1)

    def formulario_eliminacionTratamiento(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Tratamiento").grid(row=0,column = 0)
        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        
        Button(t , text="Eliminar").grid(row=1,column=1)

    def formulario_eliminacionMedicacion(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de eliminacion")
        Label(t ,text = "Codigo de Medicacion").grid(row=0,column = 0)
        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        
        Button(t , text="Eliminar").grid(row=1,column=1)

    def formulario_modificacionpais(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
        Label(t ,text = "Nombre nuevo").grid(row=1,column = 0)

        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        NombreNuevo = Entry(t).grid(row = 1, column = 1)
        
        Button(t , text="Modificar").grid(row=1,column=1)

    def formulario_modificacionciudad(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Ciudad").grid(row=1,column = 0)
        Label(t ,text = "Nombre nuevo").grid(row=2,column = 0)

        Codigo_de_Pais = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Ciudad = Entry(t).grid(row = 1, column = 1)
        NombreNuevo = Entry(t).grid(row = 2, column = 1)
        
        Button(t , text="Modificar").grid(row=3,column=1)

    def formulario_modificacionCliente(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Cliente").grid(row=0,column = 0)
        Label(t ,text = "Nombre nuevo").grid(row=1,column = 0)
        Label(t ,text = "Direccion nueva").grid(row=2,column = 0)
        Label(t ,text = "Codigo de pais nuevo").grid(row=3,column = 0)
        Label(t ,text = "Codigo de ciudad nueva").grid(row=4,column = 0)
        Label(t ,text = "Telefono nuevo").grid(row=5,column = 0)

        Codigo_de_Cliente = Entry(t).grid(row = 0, column = 1)
        NombreNuevo = Entry(t).grid(row = 1, column = 1)
        Direccion_nueva = Entry(t).grid(row = 2, column = 1)
        Codigo_de_Pais = Entry(t).grid(row = 3, column = 1)
        Codigo_de_Ciudad = Entry(t).grid(row = 4, column = 1)
        TelefonoNuevo = Entry(t).grid(row = 5, column = 1)
        
        
        Button(t , text="Modificar").grid(row=6,column=1)

    def formulario_modificacionmascota(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Cliente").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Mascota").grid(row=1,column = 0)
        Label(t ,text = "Nombre nuevo de Mascota").grid(row=2,column = 0)
        Label(t ,text = "Castrado").grid(row=3,column = 0)

        Codigo_de_Cliente = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Ciudad = Entry(t).grid(row = 1, column = 1)
        NombreNuevo = Entry(t).grid(row = 2, column = 1)
        Castrado = Entry(t).grid(row = 3, column = 1)
        
        Button(t , text="Modificar").grid(row=4,column=1)


    def formulario_modificacionvisita(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Visita").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Mascota").grid(row=1,column = 0)
        Label(t ,text = "Forma de Pago nueva").grid(row=2,column = 0)
     

        Codigo_de_Visita = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Mascota = Entry(t).grid(row = 1, column = 1)
        Forma_de_Pago = Entry(t).grid(row = 2, column = 1)
        
        Button(t , text="Modificar").grid(row=3,column=1)
    

    def formulario_modificacionvisita(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Visita").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Mascota").grid(row=1,column = 0)
        Label(t ,text = "Forma de Pago nueva").grid(row=2,column = 0)
     

        Codigo_de_Visita = Entry(t).grid(row = 0, column = 1)
        Codigo_de_Mascota = Entry(t).grid(row = 1, column = 1)
        Forma_de_Pago = Entry(t).grid(row = 2, column = 1)
        
        Button(t , text="Modificar").grid(row=3,column=1)

    def formulario_modificaciontratamiento(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de tratamiento").grid(row=0,column = 0)
        Label(t ,text = "Precio unitario nuevo").grid(row=1,column = 0)

     

        Codigo_de_Visita = Entry(t).grid(row = 0, column = 1)
        PrecioUnitario = Entry(t).grid(row = 1, column = 1)
        
        
        Button(t , text="Modificar").grid(row=2,column=1)

    def formulario_modificacionMedicacion(self):
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de modificacion")
        Label(t ,text = "Codigo de Medicacion").grid(row=0,column = 0)
        Label(t ,text = "Codigo de Animal").grid(row=1,column = 0)
        Label(t ,text = "Cantidad nueva de medicamento").grid(row=2,column = 0)
        Label(t ,text = "Precio nuevo de medicamento").grid(row=3,column = 0)
        Label(t ,text = "Precio total nuevo de medicamento").grid(row=4,column = 0)


     

        Codigo_de_Visita = Entry(t).grid(row = 0, column = 1)
        PrecioUnitario = Entry(t).grid(row = 1, column = 1)
        Cantidad = Entry(t).grid(row = 2, column = 1)
        Precio = Entry(t).grid(row = 3, column = 1)
        PrecioTotal = Entry(t).grid(row = 4, column = 1)
        
        Button(t , text="Modificar").grid(row=5,column=1)



def main():
    from pais import cargarPaises
    cargarPaises()
    from ciudad import cargarCiudad
    cargarCiudad()
    from cliente import cargarClientes
    cargarClientes()
    from mascota import cargarMascotas
    cargarMascotas()
    from visitas import cargarVisitas
    cargarVisitas()
    from medicacion import cargarMed
    cargarMed()
    from tratamiento import cargarTratamientos
    cargarTratamientos()
    root = Tk()
    root.resizable(False, False)
    root.geometry("880x620")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()
