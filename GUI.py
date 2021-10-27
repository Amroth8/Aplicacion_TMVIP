from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import Func

#raiz principal
root = Tk()
root.title("Todo Market VIP")
root.iconbitmap("img/Logo.ico")
root.config(bg="#000")


#frame opciones
opcionesFrame = Frame()
opcionesFrame.pack(
    fill="both", 
    expand="True"
)
opcionesFrame.config(bg="#E5E5E5")
opcionesFrame.config(width="650", height="350")


#frame ventas
ventasFrame = Frame(opcionesFrame)
ventasFrame.config(
    bg="#f5f5dc", 
    width=550, 
    height=460
)
ventasFrame.grid(
    row=0, 
    rowspan=100, 
    column=1, 
    columnspan=100, 
    sticky=NSEW
)
ventasFrame.grid_propagate(False)
    #label
buscarLabel_ventas = Label(ventasFrame, text="Buscar producto")
buscarLabel_ventas.grid(
    row=0, 
    column=0, 
    sticky=NSEW
)
    #cuadro
buscarCuadro_ventas = Entry(ventasFrame)
buscarCuadro_ventas.grid(
    row=1, 
    column=0, 
    sticky=NSEW
)
    #boton
buscarBoton_ventas = Button(ventasFrame, text="Buscar") #, command = funcion para insertar frame 
buscarBoton_ventas.grid(
    row=1,
    column=1,
    sticky=NSEW
)
buscarBoton_ventas.config(
    cursor="hand2",
    pady=1, 
    padx=4,
    bd=2,
    overrelief="raised"
)
    #lista de la busqueda
listaBusqFrame_ventas = Frame(ventasFrame)
listaBusqFrame_ventas.config(
    bd=3, 
    relief=SUNKEN, 
    width=150, 
    height=400
)
listaBusqFrame_ventas.grid(
    row=2, 
    column=0, 
    columnspan=2, 
    sticky=NSEW
)
listaBusqFrame_ventas.propagate(0)
    #scroll para la lista
scrollBusqueda_ventas = ttk.Scrollbar(listaBusqFrame_ventas)
scrollBusqueda_ventas.pack(side=RIGHT, fill=Y)
        ##bucle para mostrar toda la busqueda
        #marcar los productos
    #lista de productos de la venta
listaLabel_ventas = Label(ventasFrame, text="Lista de Productos")
listaLabel_ventas.grid(
    row=0, 
    column=2, 
    sticky=NSEW
)


#frame de revisar ventas
revVentasFrame = Frame(opcionesFrame)
revVentasFrame.config(
    bg="#f5f5dc", 
    width=550, 
    height=460
)
revVentasFrame.grid_propagate(False)
    #label
buscarVentasLabel_revVentas = Label(revVentasFrame, text="Revisar Ventas")
buscarVentasLabel_revVentas.grid(
    row=0, 
    column=0, 
    sticky=NSEW
)
    #cuadro
buscarCuadro_revVentas = Entry(revVentasFrame)
buscarCuadro_revVentas.grid(
    row=1, 
    column=0,
    columnspan=2, 
    sticky=NSEW
)
    #boton
buscarBoton_revVentas = Button(revVentasFrame, text="Buscar") #, command = funcion para insertar frame 
buscarBoton_revVentas.grid(
    row=1,
    column=1,
    sticky=NSEW
)
buscarBoton_revVentas.config(
    cursor="hand2",
    pady=1, 
    padx=4,
    bd=2,
    overrelief="raised"
)
    #radio boton para las opciones de informe de ventas
rb_semanal = Radiobutton(
    revVentasFrame, 
    text="Informe semanal"
).grid(
    row=2,
    column=0,
    sticky=NSEW
)
rb_mensual = Radiobutton(
    revVentasFrame, 
    text="Informe mensual"
).grid(
    row=3,
    column=0,
    sticky=NSEW
)
rb_masVendidos = Radiobutton(
    revVentasFrame, 
    text="Informe de los mas vendidos"
).grid(
    row=4,
    column=0,
    sticky=NSEW
)
rb_menosVendidos = Radiobutton(
    revVentasFrame, 
    text="Informe de los menos vendidos"
).grid(
    row=5,
    column=0,
    sticky=NSEW
)
    #lista de la busqueda
listaBusqFrame_revVentas = Frame(revVentasFrame)
listaBusqFrame_revVentas.config(
    bd=3, 
    relief=SUNKEN, 
    width=250, 
    height=300
)
listaBusqFrame_revVentas.grid(
    padx=7,
    pady=1,
    row=1, 
    column=3, 
    rowspan=20, 
    columnspan=2, 
    sticky=NSEW
)
listaBusqFrame_revVentas.propagate(0)
        #scroll para la lista
    #boton para expotar datos de la venta
exportarBoton_revVentas = Button(revVentasFrame, text="Exportar") #, command = funcion para insertar frame 
exportarBoton_revVentas.grid(
    row=21,
    column=4,
    sticky=NSEW
)
exportarBoton_revVentas.config(
    cursor="hand2",
    pady=1, 
    padx=4,
    bd=2,
    overrelief="raised"
)


#frame de actualizar datos
actDatosFrame = Frame(opcionesFrame)
actDatosFrame.config(
    bg="#f5f5dc", 
    width=550, 
    height=460
)
actDatosFrame.grid_propagate(False)
    #label
buscarProdLabel_actDatos = Label(actDatosFrame, text="Buscar Producto")
buscarProdLabel_actDatos.grid(
    row=0, 
    column=0, 
    sticky=NSEW
)
    #cuadro
buscarCuadro_actDatos = Entry(actDatosFrame)
buscarCuadro_actDatos.grid(
    row=1, 
    column=0,
    columnspan=2, 
    sticky=NSEW
)
    #boton buscar
buscarBoton_actDatos = Button(actDatosFrame, text="Buscar")
buscarBoton_actDatos.grid(
    row=1,
    column=3,
    sticky=NSEW
)
    #label actualizar
actualizarLabel_actDatos = Label(actDatosFrame, text="Actualizar Producto")
actualizarLabel_actDatos.grid(
    row=0, 
    column=3, 
    sticky=NSEW
)
    #labels
labelNombre_actDatos = Label(actDatosFrame, text="Nombre")
labelNombre_actDatos.grid(
    row=2, 
    column=3, 
    sticky=NSEW
)
laberCod_actDatos = Label(actDatosFrame, text="Codigo de Barra")
laberCod_actDatos.grid(
    row=3, 
    column=3, 
    sticky=NSEW
)
labelPrec_actDatos = Label(actDatosFrame, text="Precio")
labelPrec_actDatos.grid(
    row=4, 
    column=3, 
    sticky=NSEW
)
labelMarca_actDatos = Label(actDatosFrame, text="Marca")
labelMarca_actDatos.grid(
    row=5, 
    column=3, 
    sticky=NSEW
)
    #cuadros
cuadroNombre_actDatos = Entry(actDatosFrame)
cuadroNombre_actDatos.grid(
    row=2, 
    column=4,
    columnspan=2, 
    sticky=NSEW
)
cuadroCod_actDatos = Entry(actDatosFrame)
cuadroCod_actDatos.grid(
    row=3, 
    column=4,
    columnspan=2, 
    sticky=NSEW
)
cuadroPrec_actDatos = Entry(actDatosFrame)
cuadroPrec_actDatos.grid(
    row=4, 
    column=4,
    columnspan=2, 
    sticky=NSEW
)
cuadroMarca_actDatos = Entry(actDatosFrame)
cuadroMarca_actDatos.grid(
    row=5, 
    column=4,
    columnspan=2, 
    sticky=NSEW
)
    #boton actualizar
actualizarBoton_actDatos = Button(actDatosFrame, text="Actualizar")
actualizarBoton_actDatos.grid(
    row=6,
    column=4,
    sticky=NSEW
)
    #label
listaDatosLabel_ventas = Label(actDatosFrame, text="Datos Actuales")
listaDatosLabel_ventas.grid(
    row=2, 
    column=0, 
    sticky=NSEW
)


#frame de añadir productos
añadirProdFrame = Frame(opcionesFrame)
añadirProdFrame.config(
    bg="#f5f5dc", 
    width=550, 
    height=460
)
añadirProdFrame.grid_propagate(False)
    #labels
label_añadirProd = Label(añadirProdFrame, text="Añadir Nuevos Productos")
label_añadirProd.grid(
    row=0, 
    column=0, 
    sticky=NSEW
)
labelNombre_añadirProd = Label(añadirProdFrame, text="Nombre")
labelNombre_añadirProd.grid(
    row=2, 
    column=0, 
    sticky=NSEW
)
laberCod_añadirProd = Label(añadirProdFrame, text="Codigo de Barra")
laberCod_añadirProd.grid(
    row=3, 
    column=0, 
    sticky=NSEW
)
labelPrec_añadirProd = Label(añadirProdFrame, text="Precio")
labelPrec_añadirProd.grid(
    row=4, 
    column=0, 
    sticky=NSEW
)
labelMarca_añadirProd = Label(añadirProdFrame, text="Marca")
labelMarca_añadirProd.grid(
    row=5, 
    column=0, 
    sticky=NSEW
)
    #cuadros
cuadroNombre_añadirProd = Entry(añadirProdFrame)
cuadroNombre_añadirProd.grid(
    row=2, 
    column=1,
    columnspan=2, 
    sticky=NSEW
)
cuadroCod_añadirProd = Entry(añadirProdFrame)
cuadroCod_añadirProd.grid(
    row=3, 
    column=1,
    columnspan=2, 
    sticky=NSEW
)
cuadroPrec_añadirProd = Entry(añadirProdFrame)
cuadroPrec_añadirProd.grid(
    row=4, 
    column=1,
    columnspan=2, 
    sticky=NSEW
)
cuadroMarca_añadirProd = Entry(añadirProdFrame)
cuadroMarca_añadirProd.grid(
    row=5, 
    column=1,
    columnspan=2, 
    sticky=NSEW
)
    #boton actualizar
actualizarBoton_añadirProd = Button(añadirProdFrame, text="Añadir")
actualizarBoton_añadirProd.grid(
    row=6,
    column=1,
    sticky=NSEW
)


#botones opciones principales
    #boton ventas
botonVentas = Button(
    opcionesFrame, 
    text="Administrar ventas", 
    command=lambda: Func.cambiarFrame("ventas",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame)
)
botonVentas.grid(row=0,column=0,sticky=NSEW)
botonVentas.config(cursor="hand2")
botonVentas.config(pady=12, padx=5)
botonVentas.config(bd=2)
botonVentas.config(overrelief="raised")
    #boton revisar ventas
botonRevVentas = Button(
    opcionesFrame, 
    text="Revisar Ventas", 
    command=lambda: Func.cambiarFrame("revVentas",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame)
)
botonRevVentas.grid(row=1,column=0,sticky=NSEW)
botonRevVentas.config(cursor="hand2")
botonRevVentas.config(pady=12, padx=5)
botonRevVentas.config(bd=2)
botonRevVentas.config(overrelief="raised")
    #boton ver/actualizar datos
botonActualizarBBDD = Button(
    opcionesFrame, 
    text="Actualizar datos de productos", 
    command=lambda: Func.cambiarFrame("actDatos",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame)
)
botonActualizarBBDD.grid(row=2,column=0,sticky=NSEW)
botonActualizarBBDD.config(cursor="hand2")
botonActualizarBBDD.config(pady=12, padx=5)
botonActualizarBBDD.config(bd=2)
botonActualizarBBDD.config(overrelief="raised")
    #boton añadir productos
botonVisualBBDD = Button(
    opcionesFrame, 
    text="Añadir nuevos productos", 
    command=lambda: Func.cambiarFrame("verDatos",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame)
)
botonVisualBBDD.grid(row=3,column=0,sticky=NSEW)
botonVisualBBDD.config(cursor="hand2")
botonVisualBBDD.config(pady=12, padx=5)
botonVisualBBDD.config(bd=2)
botonVisualBBDD.config(overrelief="raised")


root.mainloop()