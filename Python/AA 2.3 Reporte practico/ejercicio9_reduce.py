from functools import reduce

jugadores = [
    {"nombre":"Brandon", "Edad": 22},
    {"nombre":"Luis", "Edad": 23},
    {"nombre":"Alana", "Edad": 24},
    {"nombre":"Pedro", "Edad": 25}, 
]

suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador["Edad"], jugadores,0)
print(suma_edades)