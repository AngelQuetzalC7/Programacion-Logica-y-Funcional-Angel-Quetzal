# Lista de calificaciones y sus pesos (créditos)
calificaciones = [85, 90, 78, 92]
pesos = [3, 4, 2, 3]  # Créditos de cada materia

# Calcular el promedio ponderado usando una función lambda
promedio_ponderado = sum(map(lambda c, p: c * p, calificaciones, pesos)) / sum(pesos)

# Mostrar el resultado
print(f"El promedio ponderado es: {promedio_ponderado:.2f}")