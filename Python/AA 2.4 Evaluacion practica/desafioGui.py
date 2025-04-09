import tkinter as tk
from tkinter import messagebox
from functools import reduce

# Lista de aspectos a evaluar
aspectos = ["Actividades", "Herramientas", "Contenido", "Evaluación", "Practicas"]

# Lista de materias a evaluar
materias = ["ConmutacionRedes", "Programación", "Bases de Datos", "Inteligencia Artificial"]

# Diccionario para guardar las valoraciones por materia
valoraciones_por_materia = {materia: [] for materia in materias}

# Crear ventana
ventana = tk.Tk()
ventana.title("Encuesta por Materia")

# Menú desplegable para elegir materia
materia_seleccionada = tk.StringVar(ventana)
materia_seleccionada.set(materias[0])  # Valor por defecto

tk.Label(ventana, text="Selecciona la materia:").grid(row=0, column=0)
tk.OptionMenu(ventana, materia_seleccionada, *materias).grid(row=0, column=1)

# Entradas por aspecto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada3 = tk.Entry(ventana)
entrada4 = tk.Entry(ventana)
entrada5 = tk.Entry(ventana)

# Etiquetas y entradas (sin bucles)
tk.Label(ventana, text=aspectos[0] + " (1-10):").grid(row=1, column=0)
entrada1.grid(row=1, column=1)

tk.Label(ventana, text=aspectos[1] + " (1-10):").grid(row=2, column=0)
entrada2.grid(row=2, column=1)

tk.Label(ventana, text=aspectos[2] + " (1-10):").grid(row=3, column=0)
entrada3.grid(row=3, column=1)

tk.Label(ventana, text=aspectos[3] + " (1-10):").grid(row=4, column=0)
entrada4.grid(row=4, column=1)

tk.Label(ventana, text=aspectos[4] + " (1-10):").grid(row=5, column=0)
entrada5.grid(row=5, column=1)

# Funciones auxiliares
def transponer(matriz):
    if not matriz or not matriz[0]:
        return []
    return [list(map(lambda fila: fila[0], matriz))] + transponer(list(map(lambda fila: fila[1:], matriz)))

def promedio(lista):
    return reduce(lambda a, b: a + b, lista) / len(lista)

def total(lista):
    return reduce(lambda a, b: a + b, lista)

def contar_mayores(lista, umbral):
    if not lista:
        return 0
    return (1 if lista[0] > umbral else 0) + contar_mayores(lista[1:], umbral)

def mostrar_resultados(aspectos, promedios, totales, i=0):
    if i >= len(aspectos):
        return ""
    linea = f"{aspectos[i]} → Promedio: {promedios[i]:.2f}, Total: {totales[i]}\n"
    return linea + mostrar_resultados(aspectos, promedios, totales, i + 1)

# Función para enviar respuestas
def enviar():
    try:
        entradas = list(map(lambda e: int(e.get()), [entrada1, entrada2, entrada3, entrada4, entrada5]))
        if not list(map(lambda x: 1 <= x <= 10, entradas)).count(False) == 0:
            raise ValueError
        materia = materia_seleccionada.get()
        valoraciones_por_materia[materia].append(entradas)
        list(map(lambda e: e.delete(0, tk.END), [entrada1, entrada2, entrada3, entrada4, entrada5]))
        messagebox.showinfo("Guardado", f"Valoraciones guardadas para {materia}.")
    except:
        messagebox.showerror("Error", "Por favor ingresa números válidos entre 1 y 10.")

# Función para procesar resultados de la materia seleccionada
def procesar():
    materia = materia_seleccionada.get()
    datos = valoraciones_por_materia[materia]
    if not datos:
        messagebox.showwarning("Sin datos", f"No hay valoraciones para {materia}.")
        return
    transpuesta = transponer(datos)
    promedios = list(map(promedio, transpuesta))
    totales = list(map(total, transpuesta))
    todas = reduce(lambda a, b: a + b, datos)
    mayores_a_8 = contar_mayores(todas, 8)
    texto = f"📘 Resultados para: {materia}\n\n"
    texto += mostrar_resultados(aspectos, promedios, totales)
    texto += f"\nValoraciones mayores a 8: {mayores_a_8}"
    messagebox.showinfo("Resultados de la encuesta", texto)

# Botones
tk.Button(ventana, text="Enviar", command=enviar).grid(row=6, column=0)
tk.Button(ventana, text="Procesar Resultados", command=procesar).grid(row=6, column=1)

# Ejecutar
ventana.mainloop()
