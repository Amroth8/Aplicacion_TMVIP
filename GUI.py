from tkinter import *

#raiz principal
root = Tk()
root.title("Todo Market VIP")
#root.iconbitmap("img/Logo.ico")
root.config(bg="#000")

#frame opciones
opcionesFrame = Frame()
opcionesFrame.pack(fill="both", expand="True")
opcionesFrame.config(bg="#E5E5E5")
opcionesFrame.config(width="650", height="350")

#botones opciones principales
    #boton ventas
botonVentas = Button(opcionesFrame, text="Administrar ventas") #, command = funcion para insertar frame 
botonVentas.grid(row=0,column=0,sticky=NSEW)
botonVentas.config(cursor="hand2")
botonVentas.config(pady=12, padx=5)
botonVentas.config(bd=2)
botonVentas.config(overrelief="raised")

    #boton actualizar base de datos
botonActualizarBBDD = Button(opcionesFrame, text="Actualizar datos de productos") #, command = funcion para insertar frame 
botonActualizarBBDD.grid(row=1,column=0,sticky=NSEW)
botonActualizarBBDD.config(cursor="hand2")
botonActualizarBBDD.config(pady=12, padx=5)
botonActualizarBBDD.config(bd=2)
botonActualizarBBDD.config(overrelief="raised")

    #boton visualizar base de datos
botonVisualBBDD = Button(opcionesFrame, text="Visualizar datos de productos") #, command = funcion para insertar frame 
botonVisualBBDD.grid(row=2,column=0,sticky=NSEW)
botonVisualBBDD.config(cursor="hand2")
botonVisualBBDD.config(pady=12, padx=5)
botonVisualBBDD.config(bd=2)
botonVisualBBDD.config(overrelief="raised")

#frame ventas
ventasFrame = Frame()
ventasFrame.config(bg="#f5f5dc")
ventasFrame.config(width="650", height="350")
ventasFrame.grid(in_=opcionesFrame, row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)

root.mainloop()