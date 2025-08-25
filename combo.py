import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("Ejemplo ComboBox")
ventana.geometry("300x200")
#etiqueta
etiqueta=tk.Label(ventana,text="Selecione especialidad:")
etiqueta.grid(row=0,column=0,padx=10,pady=10,sticky="w")
#Crear combobox
opciones=["Cardiologia","Neurologia","Pediatria","Dermatologia"]
combo=ttk.Combobox(ventana,values=opciones,state="readonly")
combo.current(0) #Selecicionar la primera opcion por defecto
combo.grid(row=0,column=1,padx=10,pady=10)
#Fucncion para mostrar la selecip
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Seleción",f"Has seleccionado:{seleccion}")
#Boton para coomfirmar seleccion
boton=tk.Button(ventana,text="Aceptar",command=mostrar)
boton.grid(row=1,column=0,columnspan=2,pady=15)
ventana.mainloop()