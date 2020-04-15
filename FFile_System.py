from tkinter import *
import os
import random

fg_color="Gold"
fg_color1="brown"
bg_color="Dark Slate Grey"
bg_color1="black"

root=Tk()
root.title("File Manager")
root.geometry('1350x750+0+0')
root.configure(bg="Dark Slate Grey")
lblTitle = Label(root, text="Teo's File Manager", bd=7, font=('Baskerville Old Face' ,40, 'bold'), bg=bg_color1, fg=fg_color, justify=CENTER)
lblTitle.grid(row=0, column=0, pady=10, padx=10)



root.mainloop()