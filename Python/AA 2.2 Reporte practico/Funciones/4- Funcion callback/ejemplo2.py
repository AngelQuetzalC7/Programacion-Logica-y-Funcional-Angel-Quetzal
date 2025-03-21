def validar_formulario(dato, callback):
    if not dato:
        callback("Error: El campo no puede estar vacío.")
    elif len(dato) < 5:
        callback("Error: El campo debe tener al menos 5 caracteres.")
    else:
        callback("Éxito: El dato es válido.")

# Callback para mostrar mensajes de retroalimentación
def mostrar_mensaje(mensaje):
    print(mensaje)

# Ejemplo de uso:
validar_formulario("", mostrar_mensaje)  # Campo vacío
validar_formulario("abc", mostrar_mensaje)  # Menos de 5 caracteres
validar_formulario("usuario123", mostrar_mensaje)  # Válido