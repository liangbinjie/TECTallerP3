from tkinter import Menu

# variable padre = significa la ventana padre a la que esta asociado

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

    facturacion.add_cascade(label="Saldos", menu=opcion1, underline=0)
    facturacion.add_cascade(label="Descuentos", menu=opcion2, underline=0)
    facturacion.add_cascade(label="Facturacion", menu=opcion2, underline=0)

    return facturacion