#asignatura_VII = ["Programacion BackEnd"]

def agregar_asignatura(lista):
    asig_nueva = input("Ingrese la nueva asignatura: ")
    if asig_nueva =="exit":
        return lista
    return agregar_asignatura(lista + [asig_nueva])#recursividads

asignatura_VII = ["Programacion BackEnd"]

nueva_lista = agregar_asignatura(asignatura_VII)
print(nueva_lista)