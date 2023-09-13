import random
import tkinter as tk

diccionario = {
    "gato": "cat",
    "perro": "dog",
    "casa": "house",
    "libro": "book",
    "sol": "sun",
}

def obtener_palabra_al_azar(diccionario):
    palabra = random.choice(list(diccionario.keys()))
    return palabra, diccionario[palabra]

def verificar_respuesta():
    global puntaje, intentos, palabra_español,palabra_ingles

    
    respuesta = entrada_respuesta.get().strip().lower()
    if respuesta == palabra_ingles:
        resultado_label.config(text="¡Correcto! ¡Has adivinado la palabra correctamente!", fg="green")
        puntaje += 1
    else:
        resultado_label.config(text=f"Incorrecto. La respuesta correcta es: {palabra_ingles}", fg="red")
        intentos -= 1
    puntaje_label.config(text=f"Puntaje: {puntaje}/{len(diccionario)}")
    intentos_label.config(text=f"Intentos restantes: {intentos}")
    
    if intentos == 0:
        finalizar_juego()
        palabra_español, palabra_ingles = obtener_palabra_al_azar(diccionario)
        palabra_label.config(text=f"Traduce la palabra: {palabra_español}")

def finalizar_juego():
    entrada_respuesta.config(state=tk.DISABLED)
    verificar_respuesta_button.config(state=tk.DISABLED)
    resultado_label.config(text=f"Juego terminado. Tu puntaje final es: {puntaje}/{len(diccionario)}")


ventana = tk.Tk()
ventana.resizable(0,0)
ventana.title("Juego de Inglés Básico")


puntaje = 0
intentos = 3


palabra_label = tk.Label(ventana, text="", font=("Arial", 14))
entrada_respuesta = tk.Entry(ventana, font=("Arial", 12))
verificar_respuesta_button = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta)
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
puntaje_label = tk.Label(ventana, text=f"Puntaje: {puntaje}/{len(diccionario)}", font=("Arial", 12))
intentos_label = tk.Label(ventana, text=f"Intentos restantes: {intentos}", font=("Arial", 12))


####  primera pregunta
palabra_español, palabra_ingles = obtener_palabra_al_azar(diccionario)
palabra_label.config(text=f"Traduce la palabra: {palabra_español}")

palabra_label.pack(pady=10)
entrada_respuesta.pack()
verificar_respuesta_button.pack(pady=10)
resultado_label.pack()
puntaje_label.pack()
intentos_label.pack()


# verificar_respuesta_button.invoke()

ventana.mainloop()