from tkinter import Menu
from forms_consulta import *
from forms_insercion import *
from forms_eliminar import *
from forms_modificar import *
# variable padre = significa la ventana padre a la que esta asociado

def vMantenimiento(padre):
    mantenimiento = Menu(padre)
    insercion = Menu(mantenimiento) # definimos el submenu de insercion
    insercion.add_command(label="Pais", command=formulario_insercionpais)
    insercion.add_command(label="Ciudad", command=formulario_insercionciudad)
    insercion.add_command(label="Clientes", command=formulario_insercioncliente)
    insercion.add_command(label="Mascotas", command=formulario_insercionmascota)
    insercion.add_command(label="Visitas", command=formulario_insercionvisita)
    insercion.add_command(label="Tratamientos", command=formulario_inserciontratamiento)
    insercion.add_command(label="Medicacion", command=formulario_insercionMedicacion)

    consulta = Menu(mantenimiento) # definimos el submenu de consulta
    consulta.add_command(label="Pais", command=formulario_consultapais)
    consulta.add_command(label="Ciudad", command=formulario_consultaCiudad)
    consulta.add_command(label="Clientes", command=formulario_consultaCliente)
    consulta.add_command(label="Mascotas", command=formulario_consultaMascota)
    consulta.add_command(label="Visitas", command=formulario_consultaVisita)
    consulta.add_command(label="Tratamientos", command=formulario_consultatratamiento)
    consulta.add_command(label="Medicacion", command=formulario_consultaMedicacion)
    
    modificar = Menu(mantenimiento) # definimos el submenu de insercion
    modificar.add_command(label="Pais", command=form_modificarPais)
    modificar.add_command(label="Ciudad", command=form_modificarCiudad)
    modificar.add_command(label="Clientes", command=form_modificarCliente)
    modificar.add_command(label="Mascotas", command=form_modificarMascota)
    modificar.add_command(label="Visitas")
    modificar.add_command(label="Tratamientos")
    modificar.add_command(label="Medicacion")

    eliminar = Menu(mantenimiento) # definimos el submenu de consulta
    eliminar.add_command(label="Pais", command=form_eliminarPais)
    eliminar.add_command(label="Ciudad", command=form_eliminarCiudad)
    eliminar.add_command(label="Clientes", command=form_eliminarCliente)
    eliminar.add_command(label="Mascotas", command=form_eliminarMascota)
    eliminar.add_command(label="Visitas")
    eliminar.add_command(label="Tratamientos")
    eliminar.add_command(label="Medicacion", command=form_eliminarPais)

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