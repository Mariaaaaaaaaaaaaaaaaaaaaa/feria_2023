import tkinter as tk
import random
from tkinter import PhotoImage

oraciones = [
    "El gato ____ en el tejado.",
    "Ella ____ libros todos los días.",
    "Los estudiantes ____ en el aula.",
    "Mi amigo y yo ____ al parque ayer.",
    "Ella ____ música clásica en la radio.",
    "Mi abuela ______ fideos con estofado."
]

respuestas = [
    "esta",
    "lee",
    "estudian",
    "fuimos",
    "escucha",
    "cocino"
]


def verificar_respuesta():
    respuesta_usuario = entrada_respuesta.get()
    respuesta_correcta = respuestas[indice_oracion]
    
    if respuesta_usuario.lower() == respuesta_correcta:
        resultado_label.config(text="¡Correcto! Ganaste 1 punto.", fg="green")
        aumentar_puntuacion()
    else:
        resultado_label.config(text=f"Incorrecto. La respuesta correcta era: {respuesta_correcta}", fg="red")
    
    siguiente_oracion()


def siguiente_oracion():
    global indice_oracion
    if len(oraciones_restantes) > 0:
        indice_oracion = random.randint(0, len(oraciones_restantes) - 1)
        oracion_actual.set(oraciones_restantes[indice_oracion])
        entrada_respuesta.delete(0, tk.END)
        resultado_label.config(text="")
    else:
        finalizar_juego()


def aumentar_puntuacion():
    puntuacion_actual = puntuacion.get()
    puntuacion.set(puntuacion_actual + 1)


def finalizar_juego():
    entrada_respuesta.config(state=tk.DISABLED)
    verificar_respuesta_button.config(state=tk.DISABLED)
    resultado_label.config(text=f"Puntuación final: {puntuacion.get()}/5")


ventana = tk.Tk()
ventana.title("Juego de Gramática")
ventana.geometry("500x500")
ventana.resizable(0,0)
imagen_fondo = PhotoImage(file="fondo-3.png")
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place (x=0, y=0, relwidth=1,relheight=1)
etiqueta = tk.Label(ventana)
etiqueta.pack(pady=100)

oraciones_restantes = oraciones.copy()
indice_oracion = 0
oracion_actual = tk.StringVar()
oracion_actual.set(oraciones[indice_oracion])
puntuacion = tk.IntVar()


oracion_label = tk.Label(ventana, textvariable=oracion_actual, font=("Arial", 14))
entrada_respuesta = tk.Entry(ventana, font=("Arial", 12))
verificar_respuesta_button = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta)
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
puntuacion_label = tk.Label(ventana, textvariable=puntuacion, font=("Arial", 16))


oracion_label.pack(pady=10)
entrada_respuesta.pack()
verificar_respuesta_button.pack(pady=10)
resultado_label.pack()
puntuacion_label.pack(pady=10)


siguiente_oracion()


ventana.mainloop()