import time

def descargar_archivo(nombre_archivo, callback):
    print(f"Iniciando descarga de {nombre_archivo}...")
    time.sleep(3)  # Simula el tiempo de descarga
    print(f"Descarga de {nombre_archivo} completada.")
    callback(nombre_archivo)

# Callback termina 
def notificar_descarga_completada(nombre_archivo):
    print(f"Notificación: El archivo {nombre_archivo} está listo para usar.")

descargar_archivo("Tesis.pdf", notificar_descarga_completada)