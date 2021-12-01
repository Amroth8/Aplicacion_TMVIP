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

def verificar_datos_act(codigo,precio,label):
    try:
        if codigo!='':
            codigo=int(codigo)
            if codigo<0:
                label['text']='Error en el tipo de dato codigo barra'
                label.grid(row=7,column=5,padx=30,sticky=NSEW)
                return False
        if precio!='':
            precio=int(precio)
            if precio<=0:
                label['text']='Error precio menor a 0'
                label.grid(row=7,column=5,padx=30,sticky=NSEW)
                return False
    except:
        label['text']='Error en el tipo de dato'
        label.grid(row=7,column=5,padx=30,sticky=NSEW)
        return False
    return True

def sentecia_actualizar(nombre,codigo,precio,marca):
    sentencia = "UPDATE producto SET"
    segundo=False
    if nombre!='':
        sentencia = sentencia+" nom='{}'"
        segundo=True
    if codigo!='':
        if segundo:
            sentencia = sentencia+", cod_bar ={}"
        else:
            segundo=True
            sentencia = sentencia+" cod_bar ={}"
    if precio!='':
        if segundo:
            sentencia = sentencia+", prec ={}"
        else:
            segundo=True
            sentencia = sentencia+" prec ={}"
    if marca!='':
        if segundo:
            sentencia = sentencia+", marca ='{}'"
        else:
            segundo=True
            sentencia = sentencia+" pmarca ='{}'"
    sentencia = sentencia+" WHERE cod_bar = {} and nom={}"
    print(sentencia)

def actualizar_datos(nombre,codigo,precio,marca,label):
    label.grid_remove()
    if verificar_datos_act(codigo.get(),precio.get(),label):
        sentecia_actualizar(nombre.get(),codigo.get(),precio.get(),marca.get())
    nombre.delete(0,END)
    codigo.delete(0,END)
    precio.delete(0,END)
    marca.delete(0,END)

def verificar_datos(codigo,precio,label):
    try:
        codigo=int(codigo)
        precio=int(precio)
        if codigo<0:
            label['text']='Error en el tipo de dato codigo barra'
            label.grid(row=6,column=2,stick=NSEW)
            return False
        elif precio<=0:
            label['text']='Error precio menor a 0'
            label.grid( row=6,column=2,stick=NSEW)
            return False
    except:
        label['text']='Error en el tipo de dato'
        label.grid(row=6,column=2,stick=NSEW)
        return False
    return True

def añadir_productos(cuadroNombre,cuadroCod,cuadroPrec,cuadroMarca,label_errorProd):
    label_errorProd.grid_remove()
    if verificar_datos(cuadroCod.get(),cuadroPrec.get(),label_errorProd):
        nuevos_datos(cuadroNombre.get(),cuadroCod.get(),cuadroPrec.get(),cuadroMarca.get())
    cuadroMarca.delete(0,END)
    cuadroCod.delete(0,END)
    cuadroPrec.delete(0,END)
    cuadroNombre.delete(0,END)

def nuevos_datos(nombre,codigo,precio,marca):
    datos=[nombre,0,codigo,precio,marca]
    CON_PROC.agregarprod(datos)

def actualizar_stock(cant,opcion):
    print(cant)

def actualizarLista(buscarCuadro_revVentas,busqueda):
    lista=CON_PROC.buscarprod(busqueda)
    aux=[]
    for fila in lista:
        aux.append([fila[1],fila[3]])
    buscarCuadro_revVentas['values']=tuple(aux)

def actualizarListaINI(busqueda):
    lista=CON_PROC.buscarprod(busqueda)
    aux=[]
    for fila in lista:
        aux.append([fila[1],fila[3]])
    return tuple(aux)

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

def mostrarLabel(labelNombre,labelCodigo,labelPrecio,labelMarca,dato):
    pos=0
    codigo=[]
    for letra in reversed(dato):
        if letra == ' ':
            break
        pos+=1
    codigo=dato[len(dato)-pos:]
    dato=dato[:len(dato)-pos-1]
    datos=list(CON_PROC.buscarprodUnico(dato,codigo))
    labelNombre['text']=str(datos[1])
    labelCodigo['text']=str(datos[3])
    labelPrecio['text']=str(datos[4])
    labelMarca['text']=str(datos[5])