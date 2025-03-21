def generar_reporte(datos, formato):
    return [formato(dato) for dato in datos]

# Función
def formato_resultado_examen(resultado):
    return f"Materia: {resultado['materia']}, Calificación: {resultado['calificacion']}, Estado: {'Aprobado' if resultado['calificacion'] >= 70 else 'Reprobado'}"

resultados = [
    {"materia": "Redes", "calificacion": 85},
    {"materia": "Bases de Datos", "calificacion": 65},
    {"materia": "Inteligencia Artificial", "calificacion": 90},
]

reporte = generar_reporte(resultados, formato_resultado_examen)
for linea in reporte:
    print(linea)