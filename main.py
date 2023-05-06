from tkinter import *
from toolbar import *


master = Tk()
master.geometry("880x620")
master.title("TecnoPETS - Tu Veterinaria de confianza")

menubar = Menu(master)
master.config(menu=menubar)


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
facebook = PhotoImage(file='resources/facebook.png')
instagram = PhotoImage(file='resources/instagram.png')
twitter = PhotoImage(file="resources/twitter.png")
logo = PhotoImage(file='resources/LOGO.png')

Label(master, image=facebook).place(x=30, y=550)
Label(master, image=instagram).place(x=90, y=550)
Label(master, image=twitter).place(x=150, y=550)
Label(master, image=logo).place(x=560, y=550)

# ********* POPUPS ***********
popup = Menu(master, tearoff=0)
popup.add_command(label="Insertar")
popup.add_command(label="Consultar")
popup.add_command(label="Modificar")
popup.add_command(label="Eliminar")

def popupm(button, modulo):
   print(modulo)
   try:         
      x = button.winfo_rootx()
      y = button.winfo_rooty()
      popup.tk_popup(x, y, 0)
   finally:
      popup.grab_release()

# *********** SECCION DE BOTONES DE LOS DIFERENTES MODULOS ************
paises = PhotoImage(file="resources/paises.png")
ciudades = PhotoImage(file="resources/ciudades.png")
clientes = PhotoImage(file="resources/cliente.png")

btnPaises = Button(master, image=paises, command=popupm)
btnPaises.configure(command= lambda: popupm(btnPaises, "paises"))
btnPaises.place(x=30,y=100)

btnCiudades = Button(master, image=ciudades)
btnCiudades.configure(command= lambda: popupm(btnCiudades, "ciudades"))
btnCiudades.place(x=188,y=100)

btnClientes = Button(master, image=clientes)
btnClientes.configure(command= lambda: popupm(btnClientes, "clientes"))
btnClientes.place(x=346,y=100)





master.mainloop()