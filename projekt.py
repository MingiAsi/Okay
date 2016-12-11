from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = 'Tere ' + nimi.get()
    messagebox.showinfo(message=tervitus)


raam = Tk()
raam.title("Tervitaja")

silt = ttk.Label(raam, text="Nimi")
silt.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W))

nimi = ttk.Entry(raam)
nimi.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))

nupp = ttk.Button(raam, text="Tervita!", command=tervita)
nupp.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, W, E))

raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)

# kuvame akna ekraanile
raam.mainloop()

tervita()