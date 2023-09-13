import random
import tkinter as tk
from tkinter import PhotoImage

def generar_pregunta():
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores)
    numero1 = random.randint(1, 100)
    numero2 = random.randint(1, 100)
    
    if operador == '+':
        respuesta = numero1 + numero2
    elif operador == '-':
        respuesta = numero1 - numero2
    elif operador == '*':
        respuesta = numero1 * numero2
    else:
        numero1 = numero2 * random.randint(1, 10)
        respuesta = numero1 / numero2
    
    return f'¿Cuánto es {numero1} {operador} {numero2}?', respuesta

def verificar_respuesta():
    respuesta_usuario = entrada_respuesta.get()
    if respuesta_usuario == str(respuesta_correcta):
        resultado.config(text='¡Correcto!', fg='green')
        actualizar_puntuacion(1)
    else:
        resultado.config(text=f'Incorrecto. La respuesta correcta era {respuesta_correcta}', fg='red')
    
    nueva_pregunta()

def actualizar_puntuacion(puntos):
    global puntuacion
    puntuacion += puntos
    etiqueta_puntuacion.config(text=f'Puntos: {puntuacion}')

def nueva_pregunta():
    global respuesta_correcta
    pregunta, respuesta_correcta = generar_pregunta()
    etiqueta_pregunta.config(text=pregunta)
    resultado.config(text='')
    entrada_respuesta.delete(0, tk.END)

def salir_del_juego():
    ventana.destroy()

# Ventana principal
ventana = tk.Tk()
ventana.resizable(0,0)
ventana.title('Juego Matemático')

imagen_fondo = PhotoImage(file="Fondo.png")
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place (x=0, y=0, relwidth=1,relheight=1)
etiqueta = tk.Label(ventana)
etiqueta.pack(pady=100)


puntuacion = 0
etiqueta_puntuacion = tk.Label(ventana, text=f'Puntos: {puntuacion}')
etiqueta_puntuacion.pack()

etiqueta_pregunta = tk.Label(ventana, text='', font=('Helvetica', 24))
etiqueta_pregunta.pack()

entrada_respuesta = tk.Entry(ventana, font=('Helvetica', 24))
entrada_respuesta.pack()

boton_verificar = tk.Button(ventana, text='Verificar', command=verificar_respuesta)
boton_verificar.pack()

resultado = tk.Label(ventana, text='', font=('Helvetica', 18))
resultado.pack()

boton_nueva_pregunta = tk.Button(ventana, text='Nueva Pregunta', command=nueva_pregunta)
boton_nueva_pregunta.pack()

boton_salir = tk.Button(ventana, text='Salir', command=salir_del_juego)
boton_salir.pack()

# Iniciar el juego
nueva_pregunta()

ventana.mainloop()
    


#juego geo

