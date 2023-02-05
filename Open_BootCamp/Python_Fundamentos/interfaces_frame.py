import tkinter
from tkinter import ttk
import sys

# Creamos una ventana
window = tkinter.Tk()

# Creamos una rejilla para utilizar con grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Los "frame" son como contenedores o marcos, y dentro se colocan los elementos
# frame se utiliza para agrupar elementos
# Creamos un frame
frame = ttk.Frame(window, width=800, height=600, relief="sunken")

# Creamos una etiqueta para colocar dentro del frame
label = ttk.Label(frame, text="frame_label")

# Colocamos label segun la geometria grid
label.grid(column=0, row=0, sticky=tkinter.SE, padx=50, pady=50)

# Mostramos el frame segun geometria grid
frame.grid(column=0, row=0, sticky=tkinter.SE, padx=30, pady=30)

window.mainloop()
sys.exit(0)     # finalizamos el programa, está es la última línea que se ejecuta 