jugadores = [
    {"nombre":"Brandon", "Edad": 22},
    {"nombre":"Luis", "Edad": 23},
    {"nombre":"Alana", "Edad": 24}, 
]

nombre_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombre_jugadores)