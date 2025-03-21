def procesar_notas(notas, operacion):
    return [operacion(nota) for nota in notas]

# 1 funcion
def ajustar_notas(nota):
    return nota + 5

# 2 funcion
def convertir_a_porcentaje(nota):
    return (nota / 20) * 100

# Uso
notas = [12, 15, 18, 10]

notas_ajustadas = procesar_notas(notas, ajustar_notas)
print("Notas ajustadas:", notas_ajustadas)

notas_porcentaje = procesar_notas(notas, convertir_a_porcentaje)
print("Notas en porcentaje:", notas_porcentaje)