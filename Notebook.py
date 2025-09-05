#Importar las ibrerias
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
#Funcion para enmascarar fechas
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#lista de pacientes
pacientes_data=[]
#funcion para registrar pacientes
def registrar_paciente():
    #crear un diccionario cp los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Grupo Sanguineo":entryGrupoSanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Médico":centro_medico.get()
    }
    #Agregar paciente a la lista
    pacientes_data.append(paciente)
    #Cargar el treeview
    cargar_treeview()
def cargar_treeview():
    #Limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i, item in enumerate(pacientes_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Médico"]
            )
        )

#Crear ventana principal
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("700x600")
#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
frame_doctores=ttk.Frame(pestañas)
#Agregar pestañas a Notebook
pestañas.add(frame_pacientes,text="Pacientes")
pestañas.add(frame_doctores,text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo:")
labelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#Fecha de Nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de nacimiento:")
labelFechaN.grid(row=1,column=0,padx=5,pady=5,sticky="w")
#llamando a la funcion enmascarar fecha
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#Edad
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar,state="readonly")
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#Genero
labelGenero=tk.Label(frame_pacientes,text="Genero:")
labelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=tk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=4,sticky="w")
radioFemenino=tk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,sticky="w")
#Grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")
#Tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro:")
labelTipoSeguro.grid(row=6,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Publico","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,padx=5,pady=5,sticky="w")
#Centros Medicos
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
labelCentroMedico.grid(row=7,column=0,padx=5,pady=5,sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clinica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,padx=5,pady=5,sticky="w")
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9,column=0,columnspan=2,pady=5,sticky="w")
#Boton registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrar_paciente)
btn_registrar.grid(row=0,column=0,padx=5)
#Boton eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=0,column=1,padx=5)
#Crear Treeview para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")
#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo Seguro")
treeview.heading("CentroM",text="Centro Médico")
#Definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
#Ubicar el Treeview en la cuadricula
treeview.grid(row=8,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=8,column=2,sticky="ns")


#doctores
titulo=tk.Label(frame_doctores,text="Registro de Doctores",font=("Arial",14,"bold"))
titulo.grid(row=0,column=1,padx=200,sticky="w")
#Nombre
NombreD=tk.Label(frame_doctores,text="Nombre:")
NombreD.grid(row=2,column=0,padx=5,pady=5,sticky="w")
NombreEntry=tk.Entry(frame_doctores)
NombreEntry.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#Especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad:")
labelEspecialidad.grid(row=3,column=0,padx=5,pady=5,sticky="w")
especialidad=tk.StringVar()
especialidad.set("Cirujia")
comboEspecialidad=ttk.Combobox(frame_doctores,values=["Cirujia","Oftalmologia","Ninguna"],textvariable=especialidad)
comboEspecialidad.grid(row=3,column=1,padx=5,pady=5,sticky="w")
#Edad
labelEdadD=tk.Label(frame_doctores,text="Edad")
labelEdadD.grid(row=4,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(frame_doctores,from_=1,to=100)
spin.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#Telefono
Telefono=tk.Label(frame_doctores,text="Teléfono")
Telefono.grid(row=5,column=0,padx=5,pady=5,sticky="w")
TelefonoEntry=tk.Entry(frame_doctores)
TelefonoEntry.grid(row=5,column=1,padx=5,pady=5,sticky="w")
#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=6,column=0,columnspan=2,pady=5,sticky="w")
#Boton registrar
btn_registrarD=tk.Button(btn_frameD,text="Registrar",command="")
btn_registrarD.grid(row=0,column=0,padx=5)
#Boton eliminar
btn_eliminarD=tk.Button(btn_frameD,text="Eliminar",command="")
btn_eliminarD.grid(row=0,column=1,padx=5)
#Crear Treeview para mostrar pacientes
treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Telefono"),show="headings")
#Definir encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("Edad",text="Edad")
treeviewD.heading("Telefono",text="Teléfono")
#Definir anchos de columnas
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("Edad",width=50,anchor="center")
treeviewD.column("Telefono",width=60,anchor="center")
#Ubicar el Treeview en la cuadricula
treeviewD.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#Scrollbar vertical
scroll_yD=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=7,column=2,sticky="ns")



ventanaPrincipal.mainloop()