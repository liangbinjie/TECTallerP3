from variables import LISTA_TRATAMIENTOS,TABLA_TRATAMIENTOS


def cargarTratamientos():
    archivo = open(TABLA_TRATAMIENTOS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for elemento in salida:
        if elemento not in LISTA_TRATAMIENTOS:
            LISTA_TRATAMIENTOS.append(elemento)


        
    
