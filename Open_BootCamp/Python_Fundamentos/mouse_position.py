import tkinter
from tkinter import Tk
from tkinter import mainloop, Message


def motion(event):
    print("Mouse position: (%s %s)"% (event.x, event.y))
    return

master=Tk()
texto="Demo de texto en un widget msg para ver el movimiento del raton"
msg= Message(master, text=texto)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
