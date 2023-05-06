from tkinter import *
from toolbar import vMantenimiento, vReportes

# https://zetcode.com/tkinter/menustoolbars/
class MainFrame(Frame):

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
        
        informacion = Menu(menubar)
        informacion.add_cascade(label="Desarrollado por:")
        informacion.add_cascade(label="- Binjie Liang")
        informacion.add_cascade(label="- Aaron Moncada")



        menubar.add_cascade(label="Mantenimiento", underline=0, menu=mantenimiento)
        menubar.add_cascade(label="Reportes", underline=0, menu=reportes)
        menubar.add_cascade(label="Informacion", underline=0, menu=informacion)
        menubar.add_cascade(label="Contacto", underline=0)


        # ********** SECCION DE REDES SOCIALES Y LOGO ****************
        self.facebook = PhotoImage(file='resources/facebook.png')
        self.instagram = PhotoImage(file='resources/instagram.png')
        self.twitter = PhotoImage(file="resources/twitter.png")
        self.logo = PhotoImage(file='resources/LOGO.png')

        Label(self.master, image=self.facebook).place(x=30, y=550)
        Label(self.master, image=self.instagram).place(x=90, y=550)
        Label(self.master, image=self.twitter).place(x=150, y=550)
        Label(self.master, image=self.logo).place(x=560, y=550)


        # *********** SECCION DE BOTONES DE LOS DIFERENTES MODULOS ************
        self.paises = PhotoImage(file="resources/paises.png")
        self.ciudades = PhotoImage(file="resources/ciudades.png")
        self.clientes = PhotoImage(file="resources/cliente.png")
        Button(self.master, image=self.paises, command=self.printHola).place(x=30,y=100)
        Button(self.master, image=self.ciudades).place(x=188,y=100)
        Button(self.master, image=self.clientes).place(x=346,y=100)

    def printHola(self):
        print("Presionaste el boton de Paises")


def main():

    root = Tk()
    root.geometry("880x620")
    app = MainFrame()
    root.mainloop()


if __name__ == '__main__':
    main()
