def preparar_hotcake():
    return "🥞"

def pedido(numero_piezas):
    piezas_hotcake = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcake

mi_familia = pedido (int(input("Ingrese la cantidad de hotcakes que desea: ")))

print(mi_familia)
#print(preparar_hotcake())

