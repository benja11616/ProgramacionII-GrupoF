import tkinter as tk 
from tkinter import messagebox

def nuevoDoctor():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal) 
    ventanaRegistro.title("Sistema de Registro de Doctores")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="paleTurquoise")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre completo : ")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    entryNombre.configure(bg="mintCream")
   
    fechaLabel=tk.Label(ventanaRegistro,text="fecha : ")
    fechaLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w",)
    entryfecha=tk.Entry(ventanaRegistro)
    entryfecha.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    entryfecha.configure(bg="mintCream")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion: ")
    direccionLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w",)
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    entryDireccion.configure(bg="mintCream")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono: ")
    telefonoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w",)
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=3, column=1, padx=10, pady=5, sticky="we")
    entryTelefono.configure(bg="mintCream")
   
    EspecialidadLabel=tk.Label(ventanaRegistro, text="Especialidad:")
    EspecialidadLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Espacialidad=tk.StringVar(value="Pediatria")
    Espacialidad=tk.StringVar(value="Cardiologia")
    Espacialidad=tk.StringVar(value="Neurologia")
    
    rbPediatria=tk.Radiobutton(ventanaRegistro, text="pediatria", variable=Espacialidad, value="pediatria")
    rbPediatria.grid(row=4, column=1, sticky="w")    
    
    rbCardiologia=tk.Radiobutton(ventanaRegistro, text="Cardiologia", variable=Espacialidad, value="Cardiologia")
    rbCardiologia.grid(row=5, column=1, sticky="w")
    
    rbNeurologia=tk.Radiobutton(ventanaRegistro, text="Neurologia", variable=Espacialidad, value="Neurologia")
    rbNeurologia.grid(row=6, column=1, sticky="w")
   
    turnoLabel=tk.Label(ventanaRegistro, text="Disponibilidad")
    turnoLabel.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    mañana=tk.BooleanVar()
    tarde=tk.BooleanVar()
    noche=tk.BooleanVar()
   
    cdMañana=tk.Checkbutton(ventanaRegistro,text="Mañana", variable=mañana)
    cdMañana.grid(row=7, column=1, sticky="w")
    cdTarde=tk.Checkbutton(ventanaRegistro,text="Tarde", variable=tarde)
    cdTarde.grid(row=8, column=1, sticky="w")
    cdNoche=tk.Checkbutton(ventanaRegistro,text="Noche", variable=noche)
    cdNoche.grid(row=9, column=1, sticky="w")
   
    def registrarDatos():
        disponibilidad=[]
        if mañana.get():
            disponibilidad.append("mañana")
        if tarde.get():
            disponibilidad.append("tarde")
        if noche.get():
            disponibilidad.append("noche")
        if len(disponibilidad)>0:
            disponibilidadTextos=','.join(disponibilidad)
        else:
            disponibilidadTextos='No tiene disponibilidad'
        
        info = (
            f"nombre:{entryNombre.get()}\n"
            f"fecha:{entryfecha.get()}\n"
            f"Dirección:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"especialidad:{Espacialidad.get()}\n"
            f"turno:{disponibilidadTextos}\n"
            )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()
        
    btnRegistrar=tk.Button(ventanaRegistro, text="Guardar Datos", command=registrarDatos)
    btnRegistrar.grid(row=15, column=1, columnspan=5, pady=18)
         
ventanaPrincipal = tk.Tk ()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#8bedfa")
 
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)

menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)

ventanaPrincipal.mainloop()