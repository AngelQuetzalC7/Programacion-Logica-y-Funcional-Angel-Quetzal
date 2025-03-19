def preparar_cafe_a():
    return "cafe americano"

def preparar_cafe_b():
    return "cafe_olla"

def ordenar_cafe(funcion , numero_tazas):
    tazas_cafe = [funcion() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_a, 5)
cafe_grupo_b = ordenar_cafe(preparar_cafe_b, 5)

print(cafe_grupo_a,'\n',cafe_grupo_b)