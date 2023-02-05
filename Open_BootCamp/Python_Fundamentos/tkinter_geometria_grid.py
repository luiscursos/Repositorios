import tkinter
from tkinter import ttk

# ttk = template toolkit, para que las aplicaciones de tkinter tengan estilo


## GEOMETRIA GRID
# Principalmente usado para formularios/tablas

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)

# THIS EXAMPLE
# (username_label) (username_entry) (2,0)
# (password_label) (username_entry) (2,1)
# (0,2) (1,2) (Button)
# (0,3) (1,3) (2,3)

window=tkinter.Tk()

# Configuramos nuestra matriz indicando un indice y las columnas que va a tener
window.columnconfigure(0, weight=1) # indice 0 longitud (columnas)=1
window.columnconfigure(1, weight=3) # indice 1 longitud (columnas)=3

# Crear etiqueta 'username_label' con ttk 
# Crea la etiqueta con el estilo del sistema operativo mientras que tkinter usa el estilo de TCL

username_label = ttk.Label(window, text="Username:")
# Con el parametro sticky, fijamos nuestra rejilla y padx=establecemos ancho, pady=establecemos alto
# Diferencias entre ipad e pad.
#   -inerpadding = ipad -> Es lo que empuja del texto hacia afuera de la etiqueta
#   -padding     = pad  -> Es el margen
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)    # La Establecemos posicion indicando columna y fila. La W de sticky, indica la posición según la rosa de los vientos (marineros)


### Campo Username
# Entrada de texto, text box, imput box
username_entry=ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)


# Etiqueta password
password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# Campo password
password_entry=ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5,pady=5)

# Crear Boton
login_button=ttk.Button(window, text="login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)


window.mainloop()   