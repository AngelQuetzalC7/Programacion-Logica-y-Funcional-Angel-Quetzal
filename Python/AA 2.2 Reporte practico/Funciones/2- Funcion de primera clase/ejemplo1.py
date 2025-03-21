def filtrar_materias_aprobadas(materias, funcion_filtro):
    return list(filter(funcion_filtro, materias))


def es_aprobada(materia):
    return materia["calificacion"] >= 70

materias = [
    {"nombre": "Redes", "calificacion": 85},
    {"nombre": "Bases de Datos", "calificacion": 65},
    {"nombre": "Inteligencia Artificial", "calificacion": 90},
    {"nombre": "Programación Avanzada", "calificacion": 60},
]

materias_aprobadas = filtrar_materias_aprobadas(materias, es_aprobada)
print("Materias aprobadas:", materias_aprobadas)