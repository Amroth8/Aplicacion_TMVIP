from tkinter import *

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

def nuevos_datos(nombre,codigo,precio,marca):
    print(nombre,' ',codigo,' ',precio,' ',marca)

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