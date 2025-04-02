from functools import reduce

venta = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

promedio = reduce(lambda x, y: x + y, venta)/ len (venta)
print (f"Promedio de ventas: {promedio:.2f}")

convertir = list(map(lambda x: round(x/20.45), venta))
print (f"Ventas en dolares: {convertir}")

mayora150 = list(filter(lambda x: x > 150, convertir))
print (f"Ventas en dolares mayores a 150: {mayora150}")

sumaventa = reduce(lambda x, y: x + y, mayora150)
print (f"Suma de ventas mayores a 150: {sumaventa:.2f}")