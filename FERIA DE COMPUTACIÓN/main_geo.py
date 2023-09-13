import random
from tkinter import *
from tkinter import PhotoImage


preguntas_geografia = [
    {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "paris"},
    {"pregunta": "¿En qué continente se encuentra Brasil?", "respuesta": "sudamerica"},
    {"pregunta": "¿Cuál es el país más grande del mundo?", "respuesta": "rusia"},
    {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "rio nilo"},
]

def obtener_pregunta_al_azar(preguntas):
    return random.choice(preguntas)

def verificar_respuesta():
    global puntaje, intentos, pregunta_actual
    
    respuesta = entrada_respuesta.get().strip().lower()
    
    if respuesta == pregunta_actual["respuesta"]:
        resultado_label.config(text="¡Correcto! ¡Has respondido correctamente!", fg="green")
        puntaje += 1
    else:
        resultado_label.config(text=f"Incorrecto. La respuesta correcta es: {pregunta_actual['respuesta']}", fg="red")
        intentos -= 1
    
    puntaje_label.config(text=f"Puntaje: {puntaje}/{len(preguntas_geografia)}")
    intentos_label.config(text=f"Intentos restantes: {intentos}")
    
    if intentos == 0:
        finalizar_juego()
    
    pregunta_actual = obtener_pregunta_al_azar(preguntas_geografia)
    pregunta_label.config(text=pregunta_actual["pregunta"])
def finalizar_juego():
    entrada_respuesta.config(state=DISABLED)
    verificar_respuesta_button.config(state=DISABLED)
    resultado_label.config(text=f"Juego terminado. Tu puntaje final es: {puntaje}/{len(preguntas_geografia)}")


ventana = Tk()
ventana.title("Juego de Geografía")
ventana.geometry("600x430")
ventana.resizable(0,0)
imagen_fondo = PhotoImage(file="Fondo-2.png")
fondo_label = Label(ventana, image=imagen_fondo)
fondo_label.place (x=0, y=0, relwidth=1,relheight=1)
etiqueta = Label(ventana)
etiqueta.pack(pady=100)



puntaje = 0
intentos = 3



pregunta_label = Label(ventana, text="", font=("Arial", 14))
entrada_respuesta = Entry(ventana, font=("Arial", 12))
verificar_respuesta_button = Button(ventana, text="Verificar respuesta", command=verificar_respuesta)
resultado_label = Label(ventana, text="", font=("Arial", 12))
puntaje_label =Label(ventana, text=f"Puntaje: {puntaje}/{len(preguntas_geografia)}", font=("Arial", 12))
intentos_label =Label(ventana, text=f"Intentos restantes: {intentos}", font=("Arial", 12))


#### aqui esta la pregunta primera
pregunta_actual = obtener_pregunta_al_azar(preguntas_geografia)
pregunta_label.config(text=pregunta_actual["pregunta"])


pregunta_label.pack(pady=10)
entrada_respuesta.pack()
verificar_respuesta_button.pack(pady=10)
resultado_label.pack()
puntaje_label.pack()
intentos_label.pack()


# verificar_respuesta_button.invoke()


ventana.mainloop()