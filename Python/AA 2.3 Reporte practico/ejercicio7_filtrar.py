jugadores = [
    {"nombre":"Brandon", "Edad": 22},
    {"nombre":"Luis", "Edad": 23},
    {"nombre":"Alana", "Edad": 24},
    {"nombre":"Pedro", "Edad": 25}, 
]

#suar filter para obtener jugadores mayores de 23
jugadores_mayores = list(filter(lambda jugador: jugador["Edad"] > 23, jugadores))
print(jugadores_mayores)
