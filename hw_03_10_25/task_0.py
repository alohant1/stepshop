import tkinter as tk
from tkinter.ttk import Label

window = tk.Tk()
window.title("tkinter")
window.geometry('1920x1080')

smile = Label(window, text=':)  :)  :)', font=('Arial Bold', 500))
smile.grid(column=1, row=0)

window.mainloop()

