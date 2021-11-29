from tkinter import *
import CON_PROC

def cambiarFrame(frame,revVentas,ventas,actDatos,añadirProd,verStock,actStock):
    if frame == "ventas":
        actStock.grid_remove()
        verStock.grid_remove()
        añadirProd.grid_remove()
        actDatos.grid_remove()
        revVentas.grid_remove()
        ventas.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        ventas.grid_propagate(False)
    if frame == "revVentas":
        actStock.grid_remove()
        verStock.grid_remove()
        añadirProd.grid_remove()
        actDatos.grid_remove()
        ventas.grid_remove()
        revVentas.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        revVentas.grid_propagate(False)
    if frame == "actDatos":
        actStock.grid_remove()
        verStock.grid_remove()
        añadirProd.grid_remove()
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        actDatos.grid_propagate(False)
    if frame == "verDatos":
        actStock.grid_remove()
        verStock.grid_remove()
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid_remove()
        añadirProd.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        añadirProd.grid_propagate(False)
    if frame == "verStock":
        actStock.grid_remove()
        añadirProd.grid_remove()
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid_remove()
        verStock.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        verStock.grid_propagate(False)
    if frame == "actStock":
        verStock.grid_remove()
        añadirProd.grid_remove()
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid_remove()
        actStock.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        actStock.grid_propagate(False)

def buscar(text):
    print(text)

def actualizar_datos(nombre,codigo,precio,marca):
    print(nombre,' ',codigo,' ',precio,' ',marca)

def verificar_datos(codigo,precio,label):
    try:
        codigo=int(codigo)
        precio=int(precio)
        if codigo<0:
            label['text']='Error en el tipo de dato codigo barra'
            label.grid(
                row=6,
                column=2,
                stick=NSEW
            )
            return False
        elif precio<=0:
            label['text']='Error precio menor a 0'
            label.grid(
                row=6,
                column=2,
                stick=NSEW
            )
            return False
    except:
        label['text']='Error en el tipo de dato'
        label.grid(
            row=6,
            column=2,
            stick=NSEW
        )
        return False

def añadir_productos(cuadroNombre,cuadroCod,cuadroPrec,cuadroMarca,label_errorProd):
    label_errorProd.grid_remove()
    if verificar_datos(cuadroCod.get(),cuadroPrec.get(),label_errorProd):
        nuevos_datos(cuadroNombre.get(),cuadroCod.get(),cuadroPrec.get(),cuadroMarca.get())
    cuadroMarca.delete(0,END)
    cuadroCod.delete(0,END)
    cuadroPrec.delete(0,END)
    cuadroNombre.delete(0,END)

def nuevos_datos(nombre,codigo,precio,marca):
    datos=[nombre,0,codigo,precio]
    CON_PROC.agregarprod(datos)

def actualizar_stock(cant,opcion):
    print(cant)

def actualizarLista(buscarCuadro_revVentas,busqueda):
    lista=list(buscarCuadro_revVentas['values'])
    lista.append(busqueda)
    buscarCuadro_revVentas['values']=tuple(lista)

def actualizarListaFechas(buscarCuadro_revVentas,busqueda,opcionFecha,opcionOrden):
    lista=list(buscarCuadro_revVentas['values'])
    lista.append(opcionFecha)
    buscarCuadro_revVentas['values']=tuple(lista)

def MostrarStock(text):
    print(text)

def actualizarListaStock(buscarCuadro_revVentas,busqueda,opcionStock):
    lista=list(buscarCuadro_revVentas['values'])
    lista.append(busqueda)
    buscarCuadro_revVentas['values']=tuple(lista)