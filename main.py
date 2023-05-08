from tkinter import *
from toolbar import *

# https://zetcode.com/tkinter/menustoolbars/
class App(Frame):
    counter = 0
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


    # ********** SECCION DE LAS DIFERENTES OPCIONES DEL MENU BAR ***************
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
        self.popupPaises.add_command(label="Insercion")
        self.popupPaises.add_command(label="Consultar")
        self.popupPaises.add_command(label="Eliminar")
        self.popupPaises.add_command(label="Modificar")
        self.popup.add_cascade(label="Paises", menu=self.popupPaises)
        self.popupCiudades = Menu(self.popup)
        self.popupCiudades.add_command(label="Insercion")
        self.popupCiudades.add_command(label="Consultar")
        self.popupCiudades.add_command(label="Eliminar")
        self.popupCiudades.add_command(label="Modificar")
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
        self.popupTratamientos.add_command(label="Insercion")
        self.popupTratamientos.add_command(label="Consultar")
        self.popupTratamientos.add_command(label="Eliminar")
        self.popupTratamientos.add_command(label="Modificar")
        self.popup.add_cascade(label="Tratamientos", menu=self.popupTratamientos)
        self.popupMedicamentos = Menu(self.popup)
        self.popupMedicamentos.add_command(label="Insercion")
        self.popupMedicamentos.add_command(label="Consultar")
        self.popupMedicamentos.add_command(label="Eliminar")
        self.popupMedicamentos.add_command(label="Modificar")
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
        self.popupCliente.add_command(label="Insercion")
        self.popupCliente.add_command(label="Consultar")
        self.popupCliente.add_command(label="Eliminar")
        self.popupCliente.add_command(label="Modificar")
        self.popup.add_cascade(label="Clientes", menu=self.popupCliente)

        self.popupMascotas = Menu(self.popup)
        self.popupMascotas.add_command(label="Insercion")
        self.popupMascotas.add_command(label="Consultar")
        self.popupMascotas.add_command(label="Eliminar")
        self.popupMascotas.add_command(label="Modificar")
        self.popup.add_cascade(label="Mascotas", menu=self.popupMascotas)

        self.popupVisitas = Menu(self.popup)
        self.popupVisitas.add_command(label="Insercion")
        self.popupVisitas.add_command(label="Consultar")
        self.popupVisitas.add_command(label="Eliminar")
        self.popupVisitas.add_command(label="Modificar")
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


    def formulario_contacto(self):
        self.counter += 1
        t = Toplevel(self)
        t.geometry("300x150")
        t.title("Formulario de Contacto")
        Label(t ,text = "Nombre").grid(row = 0,column = 0)
        Label(t ,text = "Correo").grid(row = 1,column = 0)
        Label(t ,text = "Telefono").grid(row = 2,column = 0)
        Label(t ,text = "Comentarios", height=2).grid(row = 3,column = 0)
        nombre = Entry(t).grid(row = 0,column = 1)
        correo = Entry(t).grid(row = 1,column = 1)
        telefono = Entry(t).grid(row = 2,column = 1)
        comentarios = Entry(t).grid(row = 3,column = 1)
        Button(t ,text="Guardar").grid(row=4,column=1)

def main():

    root = Tk()
    root.geometry("880x620")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()
