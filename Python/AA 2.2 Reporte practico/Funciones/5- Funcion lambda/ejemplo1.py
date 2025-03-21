# Lista
materias = [
    {"nombre": "Redes", "calificacion": 85},
    {"nombre": "Bases de Datos", "calificacion": 65},
    {"nombre": "Inteligencia Artificial", "calificacion": 90},
    {"nombre": "Programación Avanzada", "calificacion": 78},
]

materias_ordenadas = sorted(materias, key=lambda x: x["calificacion"], reverse=True)

# Imprimir
for materia in materias_ordenadas:
    print(f"{materia['nombre']}: {materia['calificacion']}")