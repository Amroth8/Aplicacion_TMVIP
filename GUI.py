from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import Func

# Colores

back = "#cbcdde"
bt1 = "#e7e9ff"
btfg= "#202129"
fgn = "#33354a"

#tamaño subtitulos
t_subt = 11

Lista_Productos = ["Producto1","Producto2","Producto3","Mroducto4","Producto5","Producto6"]
Lista_Ver_Stock = []
Fechas = []

#raiz principal
root = Tk()
root.title("Todo Market VIP")
root.iconbitmap("img/Logo.ico")
root.config(bg=back, bd=25)

#frame opciones
opcionesFrame = Frame()
opcionesFrame.pack(
    fill="both", 
    expand="True"
)
opcionesFrame.config(bg=back)
opcionesFrame.config(width="650", height="350")


#frame ventas
ventasFrame = Frame(opcionesFrame)
ventasFrame.config(
    bg= back, 
    width=600,
    height=510
)
ventasFrame.grid(
    row=0, 
    rowspan=100, 
    column=1, 
    columnspan=100, 
    sticky=NSEW
)
ventasFrame.grid_propagate(False)
#espacio extra...
buscarLabel_ventas = Label(ventasFrame, text="            ")
buscarLabel_ventas.config(bg=back, fg=fgn)
buscarLabel_ventas.grid(
    row=0,
    column=0,
    sticky=NSEW
)

    #label
buscarLabel_ventas = Label(ventasFrame, text="Realizar Venta", font="arial")
buscarLabel_ventas.config(bg=back,fg=fgn)
buscarLabel_ventas.grid(
    row=0, 
    column=1, 
    columnspan=6,
    sticky=NSEW
)
    #label
buscarLabel_ventas = Label(ventasFrame, text="Buscar producto", font=("arial",t_subt+1))
buscarLabel_ventas.config(bg=back, fg=fgn)
buscarLabel_ventas.grid(
    row=1, 
    column=1, 
    sticky=NSEW
)
    #cuadro
buscarCuadro_ventas = Entry(ventasFrame)
buscarCuadro_ventas.config(fg=fgn)
buscarCuadro_ventas.grid(
    row=2, 
    column=1,
    sticky=NSEW
)
    #boton
buscarBoton_ventas = Button(
    ventasFrame, 
    text="Buscar",
    command=lambda:Func.buscar(buscarCuadro_ventas.get())
) #, command = funcion para insertar frame
buscarBoton_ventas.config(bg=bt1, fg=btfg)
buscarBoton_ventas.grid(
    row=2,
    column=2,
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
    bg="#ffffff",
    bd=3, 
    relief=SUNKEN, 
    width=150, 
    height=400
)
listaBusqFrame_ventas.grid(
    row=3, 
    column=1,
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
listaLabel_ventas = Label(ventasFrame, text="    Lista de Productos", font=("arial",t_subt+1))
listaLabel_ventas.config(bg=back,fg=fgn)
listaLabel_ventas.grid(
    row=1, 
    column=3,
    sticky=NSEW
)


#frame de informe de ventas
revVentasFrame = Frame(opcionesFrame)
revVentasFrame.config(
    bg=back,
    width=550, 
    height=460
)
revVentasFrame.grid_propagate(False)
 #espacio extra...
buscarVentasLabel_revVentas = Label(revVentasFrame, text="            ")
buscarVentasLabel_revVentas.config(bg=back)
buscarVentasLabel_revVentas.grid(
    row=0,
    column=0,
    sticky=NSEW
)
    #label
buscarVentasLabel_revVentas = Label(revVentasFrame, text="Informe de Ventas", font=("arial",t_subt+1))
buscarVentasLabel_revVentas.config(bg=back,fg=fgn)
buscarVentasLabel_revVentas.grid(
    row=1,
    column=2,
    columnspan=6, 
    sticky=NSEW
)
    #label
tipoInfVentasLabel_revVentas = Label(revVentasFrame, text="Seleccione Tipo de Informe", font=("arial",t_subt+1))
tipoInfVentasLabel_revVentas.config(bg=back,fg=fgn)
tipoInfVentasLabel_revVentas.grid(
    row=1, 
    column=1,
    sticky=NSEW
)
    #label
tipoInfVentasLabel_revVentas = Label(revVentasFrame, text="Seleccione Periodo de Tiempo",font=("arial",t_subt))
tipoInfVentasLabel_revVentas.config(bg=back,fg=btfg)
tipoInfVentasLabel_revVentas.grid(
    row=7, 
    column=1,
    sticky=NSEW
)
opcionFecha = StringVar()
opcionFecha.set(None)
opcionOrden = StringVar()
opcionOrden.set(None)
    #radio boton para las opciones de informe de ventas
rb_semanal = Radiobutton(
    revVentasFrame, 
    text="Informe semanal",
    value='Semanal',
    bg=back,fg=btfg,
    variable=opcionFecha
).grid(
    row=2,
    column=1,
    sticky=NSEW
)
rb_mensual = Radiobutton(
    revVentasFrame, 
    text="Informe mensual",
    value='Mensual',
    bg=back,fg=btfg,
    variable=opcionFecha
).grid(
    row=3,
    column=1,
    sticky=NSEW
)
rb_masVendidos = Radiobutton(
    revVentasFrame, 
    text="Mas vendidos",
    value='Mas',
    bg=back,fg=btfg,
    variable=opcionOrden
).grid(
    row=5,
    column=1,
    sticky=NSEW
)
rb_menosVendidos = Radiobutton(
    revVentasFrame, 
    text="Menos vendidos",
    value='Menos',
    bg=back,fg=btfg,
    variable=opcionOrden
).grid(
    row=6,
    column=1,
    sticky=NSEW
)
    #cuadro
buscarCuadro_revVentas = ttk.Combobox(
    revVentasFrame,
    values=Fechas
)
buscarCuadro_revVentas.grid(
    row=8, 
    column=1,
    columnspan=1, 
    sticky=NSEW
)
    #boton
buscarBoton_revVentas = Button(
    revVentasFrame, 
    text="Buscar",
    command=lambda *args :Func.actualizarListaFechas(buscarCuadro_revVentas,buscarCuadro_revVentas.get(),opcionFecha.get(),opcionOrden.get())
)
buscarBoton_revVentas.config(bg=bt1,fg=btfg)
buscarBoton_revVentas.grid(
    row=8,
    column=2,
    sticky=NSEW
)
    #label
tipoInfVentasLabel_revVentas = Label(revVentasFrame, text="Seleccione Orden",font=("arial",t_subt))
tipoInfVentasLabel_revVentas.config(bg=back,fg=btfg)
tipoInfVentasLabel_revVentas.grid(
    row=4, 
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
    row=2, 
    column=4,
    rowspan=20, 
    columnspan=2, 
    sticky=NSEW
)
listaBusqFrame_revVentas.propagate(0)
        #scroll para la lista
    #boton para expotar datos de la venta
exportarBoton_revVentas = Button(revVentasFrame, text="Exportar") #, command = funcion para insertar frame
exportarBoton_revVentas.grid(
    row=28,
    column=5,
    sticky=NSEW
)
exportarBoton_revVentas.config(
    cursor="hand2",
    pady=1, 
    padx=4,
    bg=bt1,fg=btfg,
    bd=2,
    overrelief="raised"
)


#frame de actualizar datos
actDatosFrame = Frame(opcionesFrame)
actDatosFrame.config(
    bg=back,
    width=550, 
    height=460
)
actDatosFrame.grid_propagate(False)
#espacio extra...
buscarProdLabel_actDatos = Label(actDatosFrame, text="            ")
buscarProdLabel_actDatos.config(bg=back)
buscarProdLabel_actDatos.grid(
    row=0,
    column=0,
    sticky=NSEW)
    #label
buscarProdLabel_actDatos = Label(actDatosFrame, text="Buscar Producto",font="arial")
buscarProdLabel_actDatos.config(bg=back,fg=fgn)
buscarProdLabel_actDatos.grid(
    row=0, 
    column=1,
    sticky=NSEW
)
    #cuadro
buscarCuadro_actDatos = ttk.Combobox(
    actDatosFrame,
    values=Lista_Productos
)
buscarCuadro_actDatos.grid(
    row=1, 
    column=1,
    sticky=NSEW
)
    #boton buscar
buscarBoton_actDatos = Button(
    actDatosFrame, 
    text="Buscar",
    bg=bt1,fg=btfg,
    command=lambda *args :Func.actualizarLista(buscarCuadro_actDatos,buscarCuadro_actDatos.get())
)
buscarBoton_actDatos.grid(
    row=1,
    column=3,
    sticky=NSEW
)
    #label actualizar
actualizarLabel_actDatos = Label(actDatosFrame, text="Actualizar Producto",font="arial")
actualizarLabel_actDatos.config(bg=back,fg=fgn)
actualizarLabel_actDatos.grid(
    row=1,
    column=5,
    sticky=NSEW
)
    #labels
labelNombre_actDatos = Label(actDatosFrame, text="Nombre")
labelNombre_actDatos.config(bg=back,fg=btfg)
labelNombre_actDatos.grid(
    row=2, 
    column=4, 
    sticky=NSEW
)
laberCod_actDatos = Label(actDatosFrame, text="Codigo de Barra")
laberCod_actDatos.config(bg=back,fg=btfg)
laberCod_actDatos.grid(
    row=3, 
    column=4, 
    sticky=NSEW
)
labelPrec_actDatos = Label(actDatosFrame, text="Precio")
labelPrec_actDatos.config(bg=back,fg=btfg)
labelPrec_actDatos.grid(
    row=4, 
    column=4, 
    sticky=NSEW
)
labelMarca_actDatos = Label(actDatosFrame, text="Marca")
labelMarca_actDatos.config(bg=back,fg=btfg)
labelMarca_actDatos.grid(
    row=5, 
    column=4, 
    sticky=NSEW
)
    #cuadros
cuadroNombre_actDatos = Entry(actDatosFrame)
cuadroNombre_actDatos.grid(
    row=2, 
    column=5,
    columnspan=2, 
    sticky=NSEW
)
cuadroCod_actDatos = Entry(actDatosFrame)
cuadroCod_actDatos.grid(
    row=3, 
    column=5,
    columnspan=2, 
    sticky=NSEW
)
cuadroPrec_actDatos = Entry(actDatosFrame)
cuadroPrec_actDatos.grid(
    row=4, 
    column=5,
    columnspan=2, 
    sticky=NSEW
)
cuadroMarca_actDatos = Entry(actDatosFrame)
cuadroMarca_actDatos.grid(
    row=5, 
    column=5,
    columnspan=2, 
    sticky=NSEW
)
    #boton actualizar
actualizarBoton_actDatos = Button(
    actDatosFrame, 
    text="Actualizar",
    bg=bt1,fg=btfg,
    command=lambda:Func.actualizar_datos(cuadroNombre_actDatos.get(),cuadroCod_actDatos.get(),cuadroPrec_actDatos.get(),cuadroMarca_actDatos.get())
)
actualizarBoton_actDatos.grid(
    row=6,
    column=5,
    sticky=NSEW
)
    #label
listaDatosLabel_actDatos = Label(actDatosFrame, text="Datos Actuales",font=("arial",t_subt))
listaDatosLabel_actDatos.config(bg=back,fg=btfg)
listaDatosLabel_actDatos.grid(
    row=2, 
    column=1,
    sticky=NSEW
)
    #boton eliminar producto
actualizarBoton_actDatos = Button(actDatosFrame, text="Eliminar")
actualizarBoton_actDatos.config(bg="#c7695c",fg="#561d14")
actualizarBoton_actDatos.grid(
    row=6,
    column=1,
    sticky=NSEW
)


#frame de añadir productos
añadirProdFrame = Frame(opcionesFrame)
añadirProdFrame.config(
    bg=back,
    width=550, 
    height=460
)
añadirProdFrame.grid_propagate(False)
    #labels
label_añadirProd = Label(añadirProdFrame, text="        Añadir Nuevos Productos", font="arial")
label_añadirProd.config(bg=back,fg=fgn)
label_añadirProd.grid(
    row=0, 
    column=0, 
    sticky=NSEW
)
labelNombre_añadirProd = Label(añadirProdFrame, text="Nombre")
labelNombre_añadirProd.config(bg=back,fg=btfg)
labelNombre_añadirProd.grid(
    row=2, 
    column=0, 
    sticky=NSEW
)
laberCod_añadirProd = Label(añadirProdFrame, text="Codigo de Barra")
laberCod_añadirProd.config(bg=back, fg=btfg)
laberCod_añadirProd.grid(
    row=3, 
    column=0, 
    sticky=NSEW
)
labelPrec_añadirProd = Label(añadirProdFrame, text="Precio")
labelPrec_añadirProd.config(bg=back,fg=btfg)
labelPrec_añadirProd.grid(
    row=4, 
    column=0, 
    sticky=NSEW
)
labelMarca_añadirProd = Label(añadirProdFrame, text="Marca")
labelMarca_añadirProd.config(bg=back,fg=btfg)
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
actualizarBoton_añadirProd = Button(
    añadirProdFrame, 
    text="Añadir",
    bg=bt1,fg=btfg,
    command=lambda:Func.nuevos_datos(cuadroNombre_añadirProd.get(),cuadroCod_añadirProd.get(),cuadroPrec_añadirProd.get(),cuadroMarca_añadirProd.get())
)
actualizarBoton_añadirProd.grid(
    row=6,
    column=1,
    sticky=NSEW
)


#frame de ver Stock
verStockFrame = Frame(opcionesFrame)
verStockFrame.config(
    bg=back,
    width=550, 
    height=460
)
verStockFrame.grid_propagate(False)
#espacio extra...
buscarVentasLabel_verStock = Label(verStockFrame, text="            ")
buscarVentasLabel_verStock.config(bg=back)
buscarVentasLabel_verStock.grid(
    row=0,
    column=0,
    sticky=NSEW)
    #label
buscarVentasLabel_verStock = Label(verStockFrame, text="Ver Stock",font="arial")
buscarVentasLabel_verStock.config(bg=back,fg=fgn)
buscarVentasLabel_verStock.grid(
    row=0, 
    column=1,
    columnspan=6,
    sticky=NSEW
)
    #label
buscarVentasLabel_verStock = Label(verStockFrame, text="Seleccionar Stock a Mostrar",font=("arial",t_subt))
buscarVentasLabel_verStock.config(bg=back,fg=btfg)
buscarVentasLabel_verStock.grid(
    row=1, 
    column=1,
    sticky=NSEW
)
opcionesStock = StringVar()
opcionesStock.set(None)
    #radio boton para las opciones mostrar el stock
rb_semanal_verStock = Radiobutton(
    verStockFrame, 
    text="Stock de Producto",
    value='Producto',
    bg=back,fg=btfg,
    variable=opcionesStock
).grid(
    row=2,
    column=1,
    sticky=NSEW
)
rb_mensual_verStock = Radiobutton(
    verStockFrame, 
    text="Stock en Tienda",
    value='Tienda',
    bg=back,fg=btfg,
    variable=opcionesStock
).grid(
    row=3,
    column=1,
    sticky=NSEW
)
rb_masVendido_verStock = Radiobutton(
    verStockFrame, 
    text="Stock en Bodega",
    value='Bodega',
    bg=back,fg=btfg,
    variable=opcionesStock
).grid(
    row=4,
    column=1,
    sticky=NSEW
)
    #cuadro
buscarCuadro_verStock = ttk.Combobox(
    verStockFrame,
    values=Lista_Ver_Stock
)
buscarCuadro_verStock.grid(
    row=5, 
    column=1,
    sticky=NSEW
)
    #boton
buscarBoton_verStock = Button(
    verStockFrame, 
    text="   Buscar   ",
    bg=bt1,fg=btfg,
    command=lambda:Func.actualizarListaStock(buscarCuadro_verStock,buscarCuadro_verStock.get(),opcionesStock.get())
)
buscarBoton_verStock.grid(
    row=5,
    column=2,
    sticky=NSEW
)
    #boton
mostrarBoton_verStock = Button(
    verStockFrame, 
    text="   Generar   ",
    bg=bt1,fg=btfg,
    command=lambda:Func.MostrarStock(buscarCuadro_verStock.get())
)
mostrarBoton_verStock.grid(
    row=6,
    column=2,
    sticky=NSEW
)
buscarBoton_verStock.config(
    cursor="hand2",
    pady=1, 
    padx=4,
    bd=2,
    overrelief="raised"
)
    #lista de la busqueda
listaBusqFrame_verStock = Frame(verStockFrame)
listaBusqFrame_verStock.config(
    bg="#ffffff",
    bd=3, 
    relief=SUNKEN, 
    width=250, 
    height=300
)
listaBusqFrame_verStock.grid(
    padx=7,
    pady=1,
    row=2, 
    column=4,
    rowspan=20, 
    columnspan=2, 
    sticky=NSEW
)
listaBusqFrame_verStock.propagate(0)
        #scroll para la lista
    #boton para expotar datos de la venta
exportarBoton_verStock = Button(verStockFrame, text="Exportar") #, command = funcion para insertar frame
exportarBoton_verStock.grid(
    row=23,
    column=5,
    sticky=NSEW
)
exportarBoton_verStock.config(
    cursor="hand2",
    bg=bt1,fg=btfg,
    pady=1, 
    padx=4,
    bd=2,
    overrelief="raised"
)


# frame de actualizar stock
actStockFrame = Frame(opcionesFrame)
actStockFrame.config(
    bg=back,
    width=550, 
    height=460
)
actStockFrame.grid_propagate(False)
#espacio extra...
buscarProdLabel_actStock = Label(actStockFrame, text="            ")
buscarProdLabel_actStock.config(bg=back)
buscarProdLabel_actStock.grid(
    row=0,
    column=0,
    sticky=NSEW)
    #label
buscarProdLabel_actStock = Label(actStockFrame, text="Actualizar Stock",font="arial")
buscarProdLabel_actStock.config(bg=back,fg=fgn)
buscarProdLabel_actStock.grid(
    row=0, 
    column=1,
    sticky=NSEW
)
    #cuadro
buscarCuadro_actStock = ttk.Combobox(
    actStockFrame,
    values=Lista_Productos
)
buscarCuadro_actStock.grid(
    row=1, 
    column=1,
    sticky=NSEW
)
    #boton buscar
buscarBoton_actStock = Button(
    actStockFrame, 
    text="Buscar:",
    bg=bt1,fg=btfg,
    command=lambda *args :Func.actualizarLista(buscarCuadro_actStock,buscarCuadro_actStock.get())
)
buscarBoton_actStock.grid(
    row=1,
    column=4,
    sticky=NSEW
)
    #labels
labelNombre_actStock = Label(actStockFrame, text="Nombre:")
labelNombre_actStock.config(bg=back,fg=btfg)
labelNombre_actStock.grid(
    row=2, 
    column=1,
    sticky=NSEW
)
laberCod_actStock = Label(actStockFrame, text="Codigo de Barra:")
laberCod_actStock.config(bg=back,fg=btfg)
laberCod_actStock.grid(
    row=3, 
    column=1,
    sticky=NSEW
)
labelPrec_actStock = Label(actStockFrame, text="Precio:")
labelPrec_actStock.config(bg=back,fg=btfg)
labelPrec_actStock.grid(
    row=4, 
    column=1,
    sticky=NSEW
)
labelMarca_actStock = Label(actStockFrame, text="Marca:")
labelMarca_actStock.config(bg=back,fg=btfg)
labelMarca_actStock.grid(
    row=5, 
    column=1,
    sticky=NSEW
)
labelMarca_actStock = Label(actStockFrame, text="Stock General:")
labelMarca_actStock.config(bg=back,fg=btfg)
labelMarca_actStock.grid(
    row=6, 
    column=1,
    sticky=NSEW
)
labelMarca_actStock = Label(actStockFrame, text="Stock Bodega:")
labelMarca_actStock.config(bg=back,fg=btfg)
labelMarca_actStock.grid(
    row=7, 
    column=1,
    sticky=NSEW
)
labelMarca_actStock = Label(actStockFrame, text="Stock Tienda:")
labelMarca_actStock.config(bg=back,fg=btfg)
labelMarca_actStock.grid(
    row=8, 
    column=1,
    sticky=NSEW
)
    #label
listaDatosLabel_actStock = Label(actStockFrame, text="Destino",font="arial")
listaDatosLabel_actStock.config(bg=back,fg=fgn)
listaDatosLabel_actStock.grid(
    row=1, 
    column=5,
    sticky=NSEW
)
opcionesIngreso = StringVar()
opcionesIngreso.set(None)
    #radio boton para las opciones de insertar el stock
rb_semanal_verStock = Radiobutton(
    actStockFrame, 
    text="Tienda",
    value='Tienda',
    bg=back,fg=btfg,
    variable=opcionesIngreso
).grid(
    row=2,
    column=5,
    sticky=NSEW
)
rb_mensual_verStock = Radiobutton(
    actStockFrame, 
    text="Bodega",
    value='Bodega',
    bg=back,fg=btfg,
    variable=opcionesIngreso
).grid(
    row=3,
    column=5,
    sticky=NSEW
)
    #label
cantLabel_actStock = Label(actStockFrame, text="Cantidad : ",font=("arial",11))
cantLabel_actStock.config(bg=back,fg=btfg)
cantLabel_actStock.grid(
    row=4, 
    column=5,
    sticky=NSEW
)
    #cuadros
cuadroCant_actStock = Entry(actStockFrame)
cuadroCant_actStock.grid(
    row=5, 
    column=5,
    sticky=NSEW
)
    #boton actualizar
actualizarBoton_actStock = Button(
    actStockFrame, 
    text="Actualizar",
    bg=bt1,fg=btfg,
    command=lambda:Func.actualizar_stock(cuadroCant_actStock.get(),opcionesIngreso.get())
)
actualizarBoton_actStock.grid(
    row=6,
    column=5,
    sticky=NSEW
)



#botones opciones principales
    #boton ventas
botonVentas = Button(
    opcionesFrame, 
    text="Administrar ventas", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("ventas",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonVentas.grid(row=0,column=0,sticky=NSEW)
botonVentas.config(bg=bt1, fg=btfg)
botonVentas.config(cursor="hand2")
botonVentas.config(pady=12, padx=5)
botonVentas.config(bd=2)
botonVentas.config(overrelief="raised")
    #boton revisar ventas
botonRevVentas = Button(
    opcionesFrame, 
    text="Revisar Ventas", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("revVentas",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonRevVentas.grid(row=1,column=0,sticky=NSEW)
botonRevVentas.config(bg=bt1,fg=btfg)
botonRevVentas.config(cursor="hand2")
botonRevVentas.config(pady=12, padx=5)
botonRevVentas.config(bd=2)
botonRevVentas.config(overrelief="raised")
    #boton ver/actualizar datos
botonActualizarBBDD = Button(
    opcionesFrame, 
    text="Actualizar datos de productos", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("actDatos",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonActualizarBBDD.grid(row=2,column=0,sticky=NSEW)
botonActualizarBBDD.config(bg=bt1,fg=btfg)
botonActualizarBBDD.config(cursor="hand2")
botonActualizarBBDD.config(pady=12, padx=5)
botonActualizarBBDD.config(bd=2)
botonActualizarBBDD.config(overrelief="raised")
    #boton añadir productos
botonVisualBBDD = Button(
    opcionesFrame, 
    text="Añadir nuevos productos", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("verDatos",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonVisualBBDD.grid(row=3,column=0,sticky=NSEW)
botonVisualBBDD.config(bg=bt1,fg=btfg)
botonVisualBBDD.config(cursor="hand2")
botonVisualBBDD.config(pady=12, padx=5)
botonVisualBBDD.config(bd=2)
botonVisualBBDD.config(overrelief="raised")
    #boton ver stock
botonVerStock = Button(
    opcionesFrame, 
    text="Ver Stock", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("verStock",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonVerStock.grid(row=4,column=0,sticky=NSEW)
botonVerStock.config(bg=bt1,fg=btfg)
botonVerStock.config(cursor="hand2")
botonVerStock.config(pady=12, padx=5)
botonVerStock.config(bd=2)
botonVerStock.config(overrelief="raised")
    #boton actualizar stock
botonVerStock = Button(
    opcionesFrame, 
    text="Actualizar Stock", font=("arial",t_subt),
    command=lambda: Func.cambiarFrame("actStock",revVentasFrame,ventasFrame,actDatosFrame,añadirProdFrame,verStockFrame,actStockFrame)
)
botonVerStock.grid(row=5,column=0,sticky=NSEW)
botonVerStock.config(bg=bt1,fg=btfg)
botonVerStock.config(cursor="hand2")
botonVerStock.config(pady=12, padx=5)
botonVerStock.config(bd=2)
botonVerStock.config(overrelief="raised")

root.mainloop()
