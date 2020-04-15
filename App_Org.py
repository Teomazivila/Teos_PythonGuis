from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Teos App Organizer")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename =filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gold')
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

#def left_click(frame):
    #tk.Label(frame, text = app).pack()


def clearData():
    #frame.apps.delete(0, END)
    frame.app.delete(0, END)
    frame.label.delete(0, END)


canvas = tk.Canvas(root, height=500, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root, font=('Baskerville Old Face',14, 'bold'), text="Get File",
                     padx=10, pady=5, fg='Gold', bg='#263D42', command=addApp)
openfile.pack()

clearApps = tk.Button(frame, font=('Baskerville Old Face',14, 'bold'), text="Clear Apps", padx=10,
                    pady=5, fg='Gold', bg='#263D42', command=clearData)
clearApps.pack()

runApps = tk.Button(root, font=('Baskerville Old Face',14, 'bold'), text="Start Apps", padx=10,
                    pady=5, fg='Gold', bg='#263D42', command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')