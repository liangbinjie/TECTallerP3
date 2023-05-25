from tkinter import Menu
from forms_consulta import *
from forms_insercion import *
from forms_eliminar import *
from forms_modificar import *
from reportes import *

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
    modificar.add_command(label="Visitas", command = form_modificarVisita)
    modificar.add_command(label="Tratamientos", command = form_modificartratamiento)
    modificar.add_command(label="Medicacion", command = form_modificarmedicacion)

    eliminar = Menu(mantenimiento) # definimos el submenu de consulta
    eliminar.add_command(label="Pais", command=form_eliminarPais)
    eliminar.add_command(label="Ciudad", command=form_eliminarCiudad)
    eliminar.add_command(label="Clientes", command=form_eliminarCliente)
    eliminar.add_command(label="Mascotas", command=form_eliminarMascota)
    eliminar.add_command(label="Visitas", command=form_eliminarvisita)
    eliminar.add_command(label="Tratamientos", command = form_eliminartratamiento)
    eliminar.add_command(label="Medicacion", command = form_eliminarmedicamento)

    mantenimiento.add_cascade(label='Insercion', menu=insercion, underline=0)
    mantenimiento.add_cascade(label='Consulta', menu=consulta, underline=0)
    mantenimiento.add_cascade(label='Modificar', menu=modificar, underline=0)
    mantenimiento.add_cascade(label='Eliminar', menu=eliminar, underline=0)

    return mantenimiento


def vReportes(padre):

    reportes = Menu(padre)
    reportes.add_command(label="Lista de paises", underline=0, command=getListaPaises)
    reportes.add_command(label="Ciudades de un pais", underline=0, command=formCiudadesPais)
    reportes.add_command(label="Lista de clientes", underline=0, command=getListaClientes)
    reportes.add_command(label="Lista de mascotas de cliente", underline=0, command=formMascotasCliente)
    reportes.add_command(label="Cliente con mas saldo", underline=0, command=clienteMasSaldo)
    reportes.add_command(label="Clientes con mas descuento", underline=0, command=clientesMasDescuento)
    reportes.add_command(label="Clientes de credito", underline=0, command=clientesCredito)
    reportes.add_command(label="Visitas de una mascota", underline=0, command = form_reportevisitas)
    reportes.add_command(label="Todos los tratamientos",underline=0, command = reportetratamientos)
    reportes.add_command(label="Ultimo tratamiento de una mascota", underline = 0, command = form_ulttratmascota)
    reportes.add_command(label="tratamientos de una mascota", underline = 0, command = form_tratmascota)
    reportes.add_command(label="tratamiento mas utilizado", underline = 0, command = tratamientoMasUtilizado)
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