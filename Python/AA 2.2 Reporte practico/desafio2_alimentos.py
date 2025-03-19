def prep_pizza():
    return "🍕"

def prep_hamburguesa():
    return "🍔"

def prep_hotdog():
    return "🌭"

def ordenar_alimento(funcion , porciones):
    preparar_alimento = [funcion() for _ in range(porciones)]
    bonus = contar_bonus(porciones)
    return preparar_alimento,bonus

def contar_bonus(porciones):
    if porciones > 2:
        return "COCA GRATIS"
    else:
        return "NO HAY COCA"


porcione_pizza = ordenar_alimento(prep_pizza, 3)
porciones_hamburguesa = ordenar_alimento(prep_hamburguesa, 1)
porciones_hotdog = ordenar_alimento(prep_hotdog, 4)

print(porcione_pizza)
print(porciones_hamburguesa)
print(porciones_hotdog) 