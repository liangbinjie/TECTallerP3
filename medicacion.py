from variables import TABLA_MEDICACION,LISTA_MEDICACION
from tkinter import messagebox

def cargarMed():
    archivo = open(TABLA_MEDICACION)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    for medicamento in salida:
        if medicamento not in LISTA_MEDICACION:
            LISTA_MEDICACION.append(medicamento)



def codmedexist(codmed):
    for medicacion in LISTA_MEDICACION:
        if medicacion[1] == codmed:
            return True
    return False
        
def codmedic(codmed):
    for medicacion in LISTA_MEDICACION:
        if medicacion[1] == codmed:
            return medicacion
    return False

def animexist(codanim):
    for medicacion in LISTA_MEDICACION:
        if medicacion[0] == codanim:
            return True
    return False

def consultarmedicacion(codanim,codmed):
    if animexist(codanim)==True:
        if codmedexist(codmed)==True:
            medicacion=codmedic(codmed)
            messagebox.showinfo("Consulta de medicacion", f"ID de animal: {medicacion[0]}\n"+
                            f"ID de medicacion: {medicacion[1]}\n"+
                            f"fecha ultima visita: {medicacion[2]}-{medicacion[3]}-{medicacion[4]}\n"+
                            f"lista de medicamentos: {medicacion[5]}\n"+
                            f"costo unitario: {medicacion[6]}\n"+
                            f"cantidad: {medicacion[7]}\n"+
                            f"costo total: {medicacion[8]}\n"+
                            f"cantidad recetada: {medicacion[9]}\n")
        else:
            messagebox.showerror("Error", "No se encontro el codigo de medicacion")

    else:
        messagebox.showerror("Error", "No se encontro el codigo de animal")

def insercionmedicacion(codanim,codmed,ultvisita,medicamentos,costounitario,cantidad,costototal):
    if animexist(codanim) == True:
        if codmedic(codmed) == False:
            nuevo = [codanim, codmed, ultvisita, medicamentos,costounitario,cantidad,costototal]
            LISTA_MEDICACION.append(nuevo)
            print(LISTA_MEDICACION)
        else:
            messagebox.showerror("Error", "El codigo de medicacion es repetido")
    else:
        messagebox.showerror("Error", "No se encontro el codigo animal")
            
