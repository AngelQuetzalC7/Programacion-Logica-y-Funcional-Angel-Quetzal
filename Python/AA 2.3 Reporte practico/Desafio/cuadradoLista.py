'''
A partir del código base modifica la función cuadradosLista utilizando cualquier 
combinación de map(), filter(), o reduce().
La función debería devolver un nuevo arreglo que contenga los cuadrados únicamente de 
los enteros positivos (los números decimales no son enteros) cuando se le pase un 
arreglo de números reales.
Un ejemplo de un arreglo de números reales es [-3, 4.8, 5, 3, -3.2].

Nota: La función no debe usar ningún tipo de bucles for o while ni la función forEach().
'''

def cuadradosLista(arreglo):

    #Escribir codigo aquí
    enteropositivo = filter(lambda num: isinstance(num, int ) and num > 0, arreglo)

    alcuadrado = list(map(lambda num: num ** 2,enteropositivo))

    return list(alcuadrado) # Devolver una lista con los cuadrados de los enteros positivos

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 9, 4.8, 5, 3, -3.2, 4, 5.1, 6, 7.3])
print(cuadrados_enteros)
