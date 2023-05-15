from variables import TABLA_VISITAS,LISTA_VISITAS

def cargarVisitas():
    archivo = open(TABLA_VISITAS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    # for para verificar que no haya elementos repetidos
    for elemento in salida:
        if elemento not in LISTA_VISITAS:
            LISTA_VISITAS.append(elemento)
