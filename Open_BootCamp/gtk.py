#!/usr/bin/env python
import gtk

def crear_ventana():
    ventana = gtk.Window()
    ventana.set_default_size(200, 200)
    ventana.connect('destroy', gtk.main_quit)

    etiqueta = gtk.Label('Hola mundo')
    ventana.add(etiqueta)

    etiqueta.show()
    ventana.show()

crear_ventana()
gtk.main()