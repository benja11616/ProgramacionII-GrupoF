import tkinter as tk
from tkinter import messagebox
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(VentanaPrincipal)  #Toplevel crea una ventana secundaria independite pero asociada a la ventana princiapal
    ventanaRegistro.title("Registro de pacientes")
    ventanaRegistro.geometry("500x300")
    ventanaRegistro.configure(bg="#ffffff")
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:",bg="#ffffff")
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="w") #para alinear el texto n=norte, s=sur, e=este, w=oeste, we, ns
    nombreEntry=tk.Entry(ventanaRegistro)
    nombreEntry.grid(row=0,column=1,padx=10,pady=5,sticky="we")
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo:",bg="#ffffff")
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="w")
    sexo=tk.StringVar(value="Masculino") #es una variable especial de tkinter que se utiliza para anlazar widgets como RadioButtons
    rbMaculino=tk.Radiobutton(ventanaRegistro,text="Masculino",variable=sexo,value="Masculino",bg="#ffffff")
    rbMaculino.grid(row=3,column=1,sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo,value="Femenino",bg="#ffffff")
    rbFemenino.grid(row=4,column=1,sticky="w")
    #cadena para mostrar todos los datos del formulario
    def registrarDatos():
        info=(
            f"Nombre:{nombreEntry.get()}\n"
            f"Sexo:{sexo.get()}\n"
        )
        messagebox.showinfo("Datos registrados:",info)
        ventanaRegistro.destroy()
    botonAgregar=tk.Button(ventanaRegistro,text="Aceptar",command=registrarDatos)
    botonAgregar.grid(row=6,column=0,columnspan=2,pady=15)
def busacarPaciente():
    messagebox.showinfo("buscarPaciente","Busacar Paciente")
def eliminarPaciente():
    messagebox.showinfo("eliminarPaciente","Eliminar Paciente")
VentanaPrincipal=tk.Tk()
VentanaPrincipal.title("Sistema de regristro de pacientes")
VentanaPrincipal.geometry("1000x600")
VentanaPrincipal.configure(bg="#2e7885")
#Crear la barra del menu
barraMenu=tk.Menu(VentanaPrincipal)
VentanaPrincipal.configure(menu=barraMenu)

menuPacientes=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
#agrega las opciones
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command=eliminarPaciente)
menuPacientes.add_command(label="Busacar Paciente",command=busacarPaciente)
#agrega separadores
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir",command=VentanaPrincipal.quit)


menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)

menuDoctores.add_command(label="Nuevo Doctor",command=lambda:print("Nuevo doctor"))
menuDoctores.add_command(label="Buscar Doctor",command=lambda:print("Buscar doctor"))
menuDoctores.add_command(label="Eliminar Doctor",command=lambda:print("Eliminar doctor"))

menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=VentanaPrincipal.quit)
#MENU AYUDA
menuAyuda=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de",command=lambda:messagebox.showinfo("Acerca de","Version 1.0 - Sistema de Biomedicina"))

VentanaPrincipal.mainloop()