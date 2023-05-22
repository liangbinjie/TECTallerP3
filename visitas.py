from email import message
from variables import TABLA_VISITAS,LISTA_VISITAS
from tkinter import messagebox


def cargarVisitas():
    archivo = open(TABLA_VISITAS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    # for para verificar que no haya elementos repetidos
    for elemento in salida:
        if elemento not in LISTA_VISITAS:
            LISTA_VISITAS.append(elemento)


def animalexist(idanim):
    for animal in LISTA_VISITAS:
        if animal[1] == idanim:
            return True
    return False

def visitaexist(idvisita):
    for visita in LISTA_VISITAS:
        if visita[0] == idvisita:
            return True
    return False

def visitanum(idvisita):
    i=len(LISTA_VISITAS)-1
    while i>=0:
        if LISTA_VISITAS[i][0] == idvisita:
            return i
        i=i-1

def visitaind(codvisita):
    for visita in LISTA_VISITAS:
        if visita[0] == codvisita:
            return visita


def consultarvisitas(idanim,idvisita):
    if animalexist(idanim) == True:
        if visitaexist(idvisita) == True:
            numero=visitanum(idvisita)
            messagebox.showinfo("Consulta de visita", f"iD visita: {idvisita}\n"+
                               f"ID mascota: {idanim}\n"+
                               f"fecha de ultima visita: {LISTA_VISITAS[numero][2]}-{LISTA_VISITAS[numero][3]}-{LISTA_VISITAS[numero][4]}\n"+
                               f"Total factura: {LISTA_VISITAS[numero][5]}\n"+
                               f"forma de pago: {LISTA_VISITAS[numero][6]}\n")
        else:
            messagebox.showerror("Error", "No se encontro el codigo de visita")
            
    else:
        messagebox.showerror("Error", "No se encontro el codigo animal")



def insercionvisita(idvisita, codanim, fecha, factura, formadepago):
    if visitaexist(idvisita)==True:
        messagebox.showerror("Error", "El codigo visita es repetido")
        return "Codigo repetido"
    else:
        if animalexist == False:
            messagebox.showerror("Error", "No se encontro el codigo animal")
            return "Codigo no encontrado"
        else:
            nuevo = [idvisita,codanim,fecha,factura,formadepago]
            LISTA_VISITAS.append(nuevo)
            messagebox.showinfo("Agregado", "Nueva visita agregada")
            print(LISTA_VISITAS)

def eliminarvisita(codvisita):
    if visitaexist(codvisita)==True:
        visita = visitaind(codvisita)
        print(visita)
        LISTA_VISITAS.remove(visita)
        print(LISTA_VISITAS)
        messagebox.showinfo("Eliminado","Visita eliminada")
    else:
        messagebox.showerror("Error","No se encontro el codigo de visita")

def ModificarVisita(codanim,codvisita,pago):
    if animalexist(codanim)==True:
        if visitaexist(codvisita)==True:
            num=visitanum(codvisita)
            LISTA_VISITAS[num][6]=pago
            print(LISTA_VISITAS)
            messagebox.showinfo("Modificado","Forma de pago modificada")
        else:
            messagebox.showerror("Error","No se encontro el codigo de visita")
    else:
        messagebox.showerror("Error", "No se encontro el codigo animal")




    

    


