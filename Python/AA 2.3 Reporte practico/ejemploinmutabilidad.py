#Ejemplo 1 inmutabilidad , funcion pura y sn efectos secundarios

varible_global = 10 #variable global

def aumentar_varible_():
    return varible_global + 1 #no se mdifica la variable global, se retorna un nuevo valor

print(aumentar_varible_())

#Ejemplo 2 inmutabilidad , funcion pura y sn efectos secundarios
def contar_palabras(texto):
    return len(texto.split())# Sepra el texto en palabras y cuenta la cantidad    

oracion = "El tema de hoy es la inmutabilidad en Python"
print(contar_palabras(oracion))

#Ejemplo 3 Uso incorrecto de la inmutabildad
contador_global = 0 #variable global

def contar_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())#se reasigna la variable global     


#Uso
texto_ejemplo = "Este es un ejemplo semcillo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

#Mutable
contar_palabras_no_funcional("Otro texto de ejemplo")
print(contador_global)