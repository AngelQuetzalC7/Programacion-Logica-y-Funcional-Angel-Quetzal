def aplicar_descuento(productos, funcion_descuento):
    return [funcion_descuento(producto) for producto in productos]

def descuento_20(producto):
    producto["precio"] *= 0.80
    return producto

productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Mouse", "precio": 300},
    {"nombre": "Teclado", "precio": 500},
]

productos_con_descuento = aplicar_descuento(productos, descuento_20)
print("Productos con descuento:", productos_con_descuento)