import tkinter
window=tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def funcionReset():
    variable="None"

selected = tkinter.StringVar()
r1 = tkinter.Radiobutton(window, text="Si", value='1', variable=selected)
r2 = tkinter.Radiobutton(window, text="No", value='2', variable=selected)
r3 = tkinter.Radiobutton(window, text="Quizás", value='3', variable=selected)
r4 = tkinter.Radiobutton(window, text="Reset", value='4', command=funcionReset)

r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)
r3.grid(column=0, row=2, padx=5, pady=5)
r4.grid(column=3, row=3, padx=5, pady=5)

window.mainloop()