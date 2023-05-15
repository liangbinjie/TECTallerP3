from variables import TABLA_MEDICACION,LISTA_MEDICACION

def cargarMed():
    archivo = open(TABLA_MEDICACION)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    for medicamento in salida:
        if medicamento not in LISTA_MEDICACION:
            LISTA_MEDICACION.append(medicamento)
