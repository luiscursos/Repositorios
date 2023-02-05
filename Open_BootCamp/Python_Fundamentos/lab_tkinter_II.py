import tkinter

# Los widgets, componentes o también llamados controles son los:
#  buttons, text box, radio buttons,...
# Estos widgets se ponen en contenedores, frames o windows

# Dentro de un widget se pueden posicionar objetos, 
# # hay 3 modos de posicionamiento o geometría 
#   1 -> Pack : Agolpa las cosas unas con otras. 
#               Se utiliza cuando coloquemos los objetos de arriba a abajo o cara a cara (izquierda-derecha)
#   2 -> Breed
#   3 -> Place
# Las geometrías se colocan antes del mainloop()

#_______________________________________________________________________________

#***************  GEOMETRIA PACK **************************#

window = tkinter.Tk() # Crear una ventana

# widget label, para crear una etiqueta
# La propiedad bg (background) cambia el fondo y la propiedad fg (foreground) cambia el texto 
label1 = tkinter.Label(window, text="label1", bg="yellow", fg="blue")

# Posicionamos la etiqueta dentro de una ventana con la geometría pack
# Establecemos los parametros ipadx(ancho de etiqueta) ipady(alto de etiqueta)
# La propiedad fill tiene 3 opciones, (x-y-both), rellena segun la opcion que se indique
 
label1.pack(ipadx=45, ipady=15, fill="both")

# Creamos otra etiqueta, establecemos parametros <<text,bg,fg>> y la posicionamos mediante pack()
label2 = tkinter.Label(window, text="label2",bg="red", fg="white")# Establecemos los parametros ipadx(ancho de etiqueta) ipady(alto de etiqueta)
# La propiedad expand tiene dos valores, True o False, y sirve para expandir la etiqueta en la ventana 
# La propiedad <<side>> tiene tres valores, left/bottom/rigth, y posiciona la etiqueta en uno u otro lado dentro de la ventana
label2.pack(ipadx=45, ipady=15, expand=True)

label3=tkinter.Label(window, text="label3", bg="yellow", fg="black")
label3.pack(ipadx=45, ipady=15, expand=True, fill = "both")

label4 = tkinter.Label(window, text="label4", bg="red", fg="white")
label4.pack(ipadx=5, ipady=15, side="left")

label5 = tkinter.Label(window, text="label5", bg="yellow", fg="black")
label5.pack(ipadx=15, ipady=15, side="left")

label6=tkinter.Label(window, text="label6", bg="green", fg="white")
label6.pack(ipadx=15, ipady=15, side="right")


label7 = tkinter.Label(window, text= "other text box",bg= "lightgreen", fg="lightblue")
label7.pack(ipadx=33, ipady=33, expand=True, side="bottom")
window.mainloop()  # mantiene en ejecucción la ventana


