productos = ["Frijoles Refritos", "Coca Cola", "Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]

ordenado = sorted(productos)

cadena = ", ".join(ordenado)
print("Cadena de nombres en orden alfabético:", cadena)

slugs = list(map(lambda nombre: nombre.lower().replace(" ", "-"), ordenado))

print("Lista de slugs:", slugs)
