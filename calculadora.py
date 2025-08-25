from tkinter import *
import time
import sys
import os

taps = []              
MAX_TAPS = 8           

# --- Funciones ---
def calcular_resultados(bpm):
    negra = 60000 / bpm
    resultados = {
        "1/2": round(negra * 2, 2),
        "1/4": round(negra, 2),
        "1/8": round(negra / 2, 2),
        "1/16": round(negra / 4, 2),
        "1/32": round(negra / 8, 2),
        "1/64": round(negra / 16, 2),
        "1/128": round(negra / 32, 2)
    }

    for widget in frame_resultados.winfo_children():
        widget.destroy()

    Label(frame_resultados, text="Nota").grid(row=0, column=0, padx=5, pady=2)
    Label(frame_resultados, text="Milisegundos (ms)").grid(row=0, column=1, padx=5, pady=2)

    for fila, (nota, valor) in enumerate(resultados.items(), start=1):
        Label(frame_resultados, text=nota).grid(row=fila, column=0, sticky="w")
        Label(frame_resultados, text=valor).grid(row=fila, column=1, sticky="e")

def codigoBoton():
    try:
        bpm = float(entrada_tempo.get())
        if bpm <= 0:
            raise ValueError("El BPM debe ser mayor que 0")
        calcular_resultados(bpm)
    except ValueError:
        for widget in frame_resultados.winfo_children():
            widget.destroy()
        Label(frame_resultados, text="Ingresa un número válido (>0)").grid(row=0, column=0, columnspan=2)

def tap_tempo():
    global taps
    ahora = time.time() * 1000
    taps.append(ahora)

    if len(taps) > MAX_TAPS:
        taps.pop(0)

    if len(taps) >= 2:
        intervalos = [taps[i+1] - taps[i] for i in range(len(taps)-1)]
        intervalo_promedio = sum(intervalos) / len(intervalos)
        bpm = 60000 / intervalo_promedio
        if bpm <= 0:
            return
        entrada_tempo.delete(0, END)
        entrada_tempo.insert(0, str(round(bpm, 2)))
        calcular_resultados(bpm)

def limpiar_tabla(event=None):
    global taps
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    taps = []

# --- Ventana principal
raiz = Tk()
raiz.title("Subdivisiones Tempo")
raiz.geometry("300x350")
raiz.resizable(True, True)
raiz.minsize(300, 350)

# --- Icono 
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

icono_png = os.path.join(base_path, "icono.png")
if os.path.exists(icono_png):
    try:
        ico = PhotoImage(file=icono_png)
        raiz.iconphoto(True, ico)
    except Exception as e:
        print("No se pudo cargar el icono:", e)

# --- Teclas
raiz.bind("<Escape>", limpiar_tabla)
raiz.bind("<Return>", lambda event: codigoBoton())
raiz.bind("<space>", lambda event: tap_tempo())

# --- Formulario BPM 
formulario = Frame(raiz, padx=20, pady=20)
formulario.pack()

formulario.columnconfigure(0, weight=1)
formulario.columnconfigure(1, weight=2)

Label(formulario, text="Ingresa el BPM:").grid(row=0, column=0, sticky="e", pady=5)
entrada_tempo = Entry(formulario)
entrada_tempo.grid(row=0, column=1, pady=5)

botonEnvio = Button(formulario, text="Calcular", command=codigoBoton)
botonEnvio.grid(row=1, column=0, columnspan=2, pady=10)

botonTap = Button(formulario, text="Tap Tempo", command=tap_tempo)
botonTap.grid(row=2, column=0, columnspan=2, pady=5)

# --- Frame para resultados
frame_contenedor = Frame(raiz)
frame_contenedor.pack(expand=True)

frame_resultados = Frame(frame_contenedor, padx=20, pady=10)
frame_resultados.pack(fill="x", expand=False)

raiz.mainloop()
