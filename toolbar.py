from tkinter import Menu

# variable padre = significa la ventana padre a la que esta asociado

def vMantenimiento(padre):
    mantenimiento = Menu(padre)
    insercion = Menu(mantenimiento) # definimos el submenu de insercion
    insercion.add_command(label="Pais")
    insercion.add_command(label="Ciudad")
    insercion.add_command(label="Ciudad")

    consulta = Menu(mantenimiento) # definimos el submenu de consulta
    consulta.add_command(label="Pais")
    consulta.add_command(label="Ciudad")
    consulta.add_command(label="Ciudad")
    
    modificar = Menu(mantenimiento) # definimos el submenu de insercion
    modificar.add_command(label="Pais")
    modificar.add_command(label="Ciudad")
    modificar.add_command(label="Ciudad")

    eliminar = Menu(mantenimiento) # definimos el submenu de consulta
    eliminar.add_command(label="Pais")
    eliminar.add_command(label="Ciudad")
    eliminar.add_command(label="Ciudad")

    mantenimiento.add_cascade(label='Insercion', menu=insercion, underline=0)
    mantenimiento.add_cascade(label='Consulta', menu=consulta, underline=0)
    mantenimiento.add_cascade(label='Modificar', menu=modificar, underline=0)
    mantenimiento.add_cascade(label='Eliminar', menu=eliminar, underline=0)

    return mantenimiento


def vReportes(padre):
    reportes = Menu(padre)
    opcion1 = Menu(reportes) # Definimos opcion 1
    opcion1.add_command(label="Opcion1")
    opcion1.add_command(label="Opcion2")
    opcion1.add_command(label="Opcion3")

    opcion2 = Menu(reportes) # Defininimos opcion 2
    opcion2.add_command(label="Opcion1")
    opcion2.add_command(label="Opcion2")
    opcion2.add_command(label="Opcion3")

    reportes.add_cascade(label="Opcion 1", menu=opcion1, underline=0)
    reportes.add_cascade(label="Opcion 2", menu=opcion2, underline=0)

    return reportes


def vInformacion(padre):
    informacion = Menu(padre)
    