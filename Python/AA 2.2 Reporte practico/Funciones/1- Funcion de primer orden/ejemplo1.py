def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

calificaciones = [85, 90, 78, 92, 88]
promedio = calcular_promedio(calificaciones)
print(f"El promedio de calificaciones es: {promedio}")