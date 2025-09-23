#Importar las ibrerias
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
#Funcion para enmascarar fechas
def guardar_en_archivo_doctores():
    with open("doctoresRegistro.txt","w",encoding="utf-8") as archivo:  #open abre el archico txt, "w" modo write(escritura), encoding(aceptar caracteres especiales)
            for doctor in doctores_data:
                archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['AñosExp']}|{doctor['Genero']}|{doctor['Hospital']}\n")
#lista de pacientes
doctores_data=[]
#funcion para registrar pacientes
def registrar_doctor():
    #crear un diccionario cp los datos ingresados
    doctor={
        "Nombre":NombreEntry.get(),
        "Especialidad":especialidad.get(),
        "AñosExp":spin.get(),
        "Genero":genero.get(),
        "Hospital":Hospital.get()
    }
    #Agregar paciente a la lista
    doctores_data.append(doctor)
    guardar_en_archivo_doctores()
    #Cargar el treeview
    cargar_treeviewD()
def cargar_treeviewD():
    #Limpiar el treeview
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    #Insertar cada paciente
    for i, item in enumerate(doctores_data):
        treeviewD.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["AñosExp"],
                item["Genero"],
                item["Hospital"]
            )
        )
def cargar_desde_archivo_doctores():
    try:
        with open("doctoresRegistro.txt","r",encoding="utf-8")as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==5:
                    doctor={
                        "Nombre":datos[0],
                        "Especialidad":datos[1],
                        "AñosExp":datos[2],
                        "Genero":datos[3],
                        "Hospital":datos[4]
                    }
                    doctores_data.append(doctor)
        cargar_treeviewD()
    except FileNotFoundError:
        open("doctoresRegistro.txt","w",encoding="utf-8").close()
#Crear ventana principal
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("700x600")
#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#Crear frames(uno por pestaña)
frame_doctores=ttk.Frame(pestañas)
#Agregar pestañas a Notebook
pestañas.add(frame_doctores,text="Doctores")
titulo=tk.Label(ventanaPrincipal,text="Registro de Doctores",font=("Arial",14,"bold"))
titulo.grid(row=0,column=1,padx=200,sticky="w")
#Nombre
NombreD=tk.Label(ventanaPrincipal,text="Nombre:")
NombreD.grid(row=2,column=0,padx=5,pady=5,sticky="w")
NombreEntry=tk.Entry(ventanaPrincipal)
NombreEntry.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#Especialidad
labelEspecialidad=tk.Label(ventanaPrincipal,text="Especialidad:")
labelEspecialidad.grid(row=3,column=0,padx=5,pady=5,sticky="w")
especialidad=tk.StringVar()
especialidad.set("Cirujia")
comboEspecialidad=ttk.Combobox(ventanaPrincipal,values=["Cirujia","Oftalmologia","Ninguna"],textvariable=especialidad)
comboEspecialidad.grid(row=3,column=1,padx=5,pady=5,sticky="w")
#Edad
labelEdadD=tk.Label(ventanaPrincipal,text="Años de experiencia")
labelEdadD.grid(row=4,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(ventanaPrincipal,from_=1,to=40)
spin.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#Genero
labelGenero=tk.Label(ventanaPrincipal,text="Genero:")
labelGenero.grid(row=5,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=tk.Radiobutton(ventanaPrincipal,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=5,column=1,padx=4,sticky="w")
radioFemenino=tk.Radiobutton(ventanaPrincipal,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=6,column=1,padx=5,sticky="w")
#Especialidad
labelHospital=tk.Label(ventanaPrincipal,text="Hospital:")
labelHospital.grid(row=7,column=0,padx=5,pady=5,sticky="w")
Hospital=tk.StringVar()
Hospital.set("CNS")
comboHospital=ttk.Combobox(ventanaPrincipal,values=["CNS","CPS","HF"],textvariable=Hospital)
comboHospital.grid(row=7,column=1,padx=5,pady=5,sticky="w")
#Frame para los botones
btn_frameD=tk.Frame(ventanaPrincipal)
btn_frameD.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")
#Boton registrar
btn_registrarD=tk.Button(btn_frameD,text="Registrar",command=registrar_doctor)
btn_registrarD.grid(row=0,column=0,padx=5)
#Crear Treeview para mostrar pacientes
treeviewD=ttk.Treeview(ventanaPrincipal,columns=("Nombre","Especialidad","AñosExp","Genero","Hospital"),show="headings")
#Definir encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("AñosExp",text="Años de especialidad")
treeviewD.heading("Genero",text="Genero")
treeviewD.heading("Hospital",text="Hospital")
#Definir anchos de columnas
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("AñosExp",width=50,anchor="center")
treeviewD.column("Genero",width=60,anchor="center")
treeviewD.column("Hospital",width=60,anchor="center")
#Ubicar el Treeview en la cuadricula
treeviewD.grid(row=9,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar vertical
scroll_yD=ttk.Scrollbar(ventanaPrincipal,orient="vertical",command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=9,column=2,sticky="ns")


cargar_desde_archivo_doctores()
ventanaPrincipal.mainloop()