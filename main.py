from tkinter import *
from toolbar import *


master = Tk()
master.geometry("880x620")
master.title("TecnoPETS - Tu Veterinaria de confianza")


# ******** TOOLBAR ********
toolbar = Menu(master)
master.config(menu=toolbar)


# definimos la opcion de mantenimiento
mantenimiento = vMantenimiento(toolbar) # la llamamos de la funcion de mantenimiento

# Definimos la opcion de reportes
reportes = vReportes(toolbar)

facturacion = vFacturacion(toolbar)

informacion = Menu(toolbar)
informacion.add_cascade(label="TecnoPets, 2023, Cartago Calle IC1803")
informacion.add_separator()
informacion.add_cascade(label="Desarrollado por:")
informacion.add_cascade(label="- Binjie Liang")
informacion.add_cascade(label="- Aaron Moncada")



toolbar.add_cascade(label="Mantenimiento", underline=0, menu=mantenimiento)
toolbar.add_cascade(label="Reportes", underline=0, menu=reportes)
toolbar.add_cascade(label="Facturacion", underline=0, menu=facturacion)
toolbar.add_cascade(label="Acerca De", underline=0, menu=informacion)
toolbar.add_cascade(label="Contacto", underline=0)


# ********** SECCION DE REDES SOCIALES Y LOGO ****************
LOGO_FB = PhotoImage(file='resources/facebook.png')
LOGO_INS = PhotoImage(file='resources/instagram.png')
LOGO_TWT = PhotoImage(file="resources/twitter.png")
LOGO = PhotoImage(file='resources/LOGO.png')

Label(master, image=LOGO_FB).place(x=30, y=550)
Label(master, image=LOGO_INS).place(x=90, y=550)
Label(master, image=LOGO_TWT).place(x=150, y=550)
Label(master, image=LOGO).place(x=560, y=550)

# ********* POPUPS ***********
popup = Menu(master, tearoff=0)
popupPaises = Menu(popup)

popupPaises.add_command(label="Insercion")
popupPaises.add_command(label="Consultar")
popupPaises.add_command(label="Eliminar")
popupPaises.add_command(label="Modificar")
popup.add_cascade(label="Paises", menu=popupPaises)

# ** FUNCION DE POPUP **
def popupm(button, modulo):
   print(modulo)
   try:         
      x = button.winfo_rootx()
      y = button.winfo_rooty()
      popup.tk_popup(x+128, y, 0)
   finally:
      popup.grab_release()

# *********** SECCION DE BOTONES DE LOS DIFERENTES MODULOS ************

lugares = PhotoImage(file="resources/lugares.png")
btnLugares = Button(master, image=lugares, command=popupm)
btnLugares.configure(command= lambda: popupm(btnLugares, "paises"))
btnLugares.place(x=250,y=30)
Label(text="Lugares", font=("Arial", 20)).place(x=265, y=168)


clientes = PhotoImage(file="resources/cliente.png")
btnClientes = Button(master, image=clientes)
btnClientes.configure(command= lambda: popupm(btnClientes, "clientes"))
btnClientes.place(x=450,y=30)


clinica = PhotoImage(file="resources/clinica.png")
btnClinica = Button(master, image=clinica)
btnClinica.configure(command= lambda: popupm(btnClinica, "clientes"))
btnClinica.place(x=250,y=300)

facturacion = PhotoImage(file="resources/facturacion.png")
btnFacturacion = Button(master, image=facturacion)
btnFacturacion.configure(command= lambda: popupm(btnFacturacion, "clientes"))
btnFacturacion.place(x=450,y=300)




master.mainloop()