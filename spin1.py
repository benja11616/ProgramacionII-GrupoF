import tkinter as tk
from tkinter import messagebox
def mostrarEdad():
    messagebox.showinfo("Edad",f"La edad seleccionada es: {spin.get()}")
def mostrarGenero():
    messagebox.showinfo("Genero",f"Genero seleccionado: {spinTexto.get()}")
ventana=tk.Tk()
ventana.title("ejemplo")
ventana.geometry("400x400")
labelEdad=tk.Label(ventana,text="Edad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)
boton=tk.Button(ventana,text="Obtener valor",command=mostrarEdad)
boton.grid(row=2,column=0,padx=10,pady=10)
generoLabel=tk.Label(ventana,text="Genero")
generoLabel.grid(row=1,column=0,padx=5,pady=5,sticky="w")
spinTexto=tk.Spinbox(ventana,values=("Masculino","Femenino","Otro"))
spinTexto.grid(row=1,column=1,padx=10,pady=10)
botongenero=tk.Button(ventana,text="Obtener genero",command=mostrarGenero)
botongenero.grid(row=2,column=1,padx=10,pady=10)
ventana.mainloop()