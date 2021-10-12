from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

#raiz principal
root = Tk()
root.title("Todo Market VIP")
root.iconbitmap("img/Logo.ico")
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

    #boton revisar ventas
botonRevVentas = Button(opcionesFrame, text="Revisar Ventas") #, command = funcion para insertar frame 
botonRevVentas.grid(row=1,column=0,sticky=NSEW)
botonRevVentas.config(cursor="hand2")
botonRevVentas.config(pady=12, padx=5)
botonRevVentas.config(bd=2)
botonRevVentas.config(overrelief="raised")

    #boton actualizar base de datos
botonActualizarBBDD = Button(opcionesFrame, text="Actualizar datos de productos") #, command = funcion para insertar frame 
botonActualizarBBDD.grid(row=2,column=0,sticky=NSEW)
botonActualizarBBDD.config(cursor="hand2")
botonActualizarBBDD.config(pady=12, padx=5)
botonActualizarBBDD.config(bd=2)
botonActualizarBBDD.config(overrelief="raised")

    #boton visualizar base de datos
botonVisualBBDD = Button(opcionesFrame, text="Visualizar datos de productos") #, command = funcion para insertar frame 
botonVisualBBDD.grid(row=3,column=0,sticky=NSEW)
botonVisualBBDD.config(cursor="hand2")
botonVisualBBDD.config(pady=12, padx=5)
botonVisualBBDD.config(bd=2)
botonVisualBBDD.config(overrelief="raised")

#frame ventas
ventasFrame = Frame(opcionesFrame)
ventasFrame.config(bg="#f5f5dc")
ventasFrame.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)

#widgets dentro de ventas
    #buscar y anadir producto
        #label
buscarLabel = Label(ventasFrame, text="Buscar producto")
buscarLabel.grid(row=0, column=0, sticky=NSEW)
        #cuadro
buscarCuadro = Entry(ventasFrame)
buscarCuadro.grid(row=1, column=0, sticky=NSEW)
        #boton
buscarBoton = Button(ventasFrame, text="Buscar") #, command = funcion para insertar frame 
buscarBoton.grid(row=1,column=1,sticky=NSEW)
buscarBoton.config(cursor="hand2")
buscarBoton.config(pady=1, padx=4)
buscarBoton.config(bd=2)
buscarBoton.config(overrelief="raised")
        #lista de la busqueda
listaBusqFrame = Frame(ventasFrame)
listaBusqFrame.config(bd=3, relief=SUNKEN, width=150, height=400)
listaBusqFrame.grid(row=2, column=0, columnspan=2, sticky=NSEW)
listaBusqFrame.propagate(0)
        #scroll para la lista
scrollBusqueda = ttk.Scrollbar(listaBusqFrame)
scrollBusqueda.pack(side=RIGHT, fill=Y)
        ##bucle para mostrar toda la busqueda
        #marcar los productos
imagen_ = Image.open("img/stockimg.png")
imagen_ = imagen_.resize((50,50), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(imagen_)
for i in range(10):
    Radiobutton(listaBusqFrame,image=imagen).pack(anchor=W)
    Label(listaBusqFrame, text="Producto1", padx=5).pack(anchor=W)

    #lista de productos de la venta
buscarLabel = Label(ventasFrame, text="Lista de Productos")
buscarLabel.grid(row=0, column=2, sticky=NSEW)

root.mainloop()