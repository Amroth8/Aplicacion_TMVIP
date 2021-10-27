from tkinter import *

def cambiarFrame(frame,revVentas,ventas,actDatos,añadirProd):
    if frame == "ventas":
        añadirProd.grid_remove()
        actDatos.grid_remove()
        revVentas.grid_remove()
        ventas.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        ventas.grid_propagate(False)
    if frame == "revVentas":
        añadirProd.grid_remove()
        actDatos.grid_remove()
        ventas.grid_remove()
        revVentas.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        revVentas.grid_propagate(False)
    if frame == "actDatos":
        añadirProd.grid_remove()
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        ventas.grid_propagate(False)
    if frame == "verDatos":
        ventas.grid_remove()
        revVentas.grid_remove()
        actDatos.grid_remove()
        añadirProd.grid(row=0, rowspan=100, column=1, columnspan=100, sticky=NSEW)
        ventas.grid_propagate(False)