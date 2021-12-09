from logging import lastResort
from tkinter import *
from tkinter import ttk
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


def buscarAdmVentas(dato,lbox,):
    resultados=CON_PROC.buscarprodVenta(dato)
    lbox.delete(0, END)
    for item in range(len(resultados)):
        lbox.insert(END, resultados[item][0]+' - "'+resultados[item][4]+'" - ('+str(resultados[item][1])+') - $'+str(resultados[item][3]))
        lbox.itemconfig(item)

def getPrecio(dato):
    precio=''
    for letra in reversed(dato):
        if letra == '$' or letra == ' ':
            break
        precio=letra+precio
    return int(precio)

def getCant(dato):
    cantidad1=''
    cantidad=''
    for letra in dato:
        if letra == ')':
            break
        cantidad1=cantidad1+letra
    for letra in reversed(cantidad1):
        if letra == '(':
            break
        cantidad=letra+cantidad
    return int(cantidad)

def updateDatos(datos,cant):
    mitad1=''
    mitad2=''
    for letra in datos:
        mitad1=mitad1+letra
        if letra == '(':
            break
    for letra in reversed(datos):
        mitad2=letra+mitad2
        if letra == ')':
            break
    return mitad1+str(cant)+mitad2

def datosFrame2(datos):
    mitad1=''
    mitad2=''
    for letra in datos:
        if letra == '(':
            break
        mitad1=mitad1+letra
    for letra in reversed(datos):
        if letra == ')':
            break
        mitad2=letra+mitad2
    return mitad1[:len(mitad1)-2]+mitad2

def updateLbox(lbox,cant,datoAct):
    for i in range(lbox.size()):
        if lbox.get(i)==datoAct:
            lbox.delete(i)
            lbox.insert(i, updateDatos(datoAct,cant))

def mismoProducto(dato1,dato2):
    if datosFrame2(dato1)==dato2:
        return True
    else:
        return False

def updateLboxBorrar(lbox,datoAct):
    for i in range(lbox.size()):
        if mismoProducto(lbox.get(i),datoAct):
            datos=lbox.get(i)
            cant=getCant(lbox.get(i))
            lbox.delete(i)
            lbox.insert(i, updateDatos(datos,cant+1))

def agregarAdmVentas(lbox, lbox2,totalVenta):
    selecciones=[]
    for i in lbox.curselection():
        ag = lbox.get(i)
        cant=getCant(ag)
        if cant>0:
            updateLbox(lbox,cant-1,ag)
            selecciones.append(ag)
    for item in range(len(selecciones)):
        venta=getPrecio(selecciones[item])+getPrecio(totalVenta['text'])
        totalVenta['text']="Total: "+str(venta)
        lbox2.insert(END, datosFrame2(selecciones[item]))
        lbox2.itemconfig(item)

def borrarAdmVentas(lbox,lbox2,totalVenta):
    seleccion = lbox2.curselection()
    pos = 0
    for i in seleccion:
        indice = int(i) - pos
        venta=getPrecio(totalVenta['text'])-getPrecio(lbox2.get(indice))
        totalVenta['text']="Total: "+str(venta)
        updateLboxBorrar(lbox,lbox2.get(i))
        lbox2.delete(indice,indice)
        pos = pos + 1

def venderAdmVentas(lbox):
    print('excel')

def verificar_datos_act(codigo,precio,label):
    try:
        if codigo!='':
            codigo=int(codigo)
            if codigo<0:
                label['text']='Error en el tipo de dato codigo barra'
                label.grid(row=7,column=5,sticky=NSEW)
                return False
        if precio!='':
            precio=int(precio)
            if precio<=0:
                label['text']='Error precio menor a 0'
                label.grid(row=7,column=5,sticky=NSEW)
                return False
    except:
        label['text']='Error en el tipo de dato'
        label.grid(row=7,column=5,sticky=NSEW)
        return False
    return True

def sentecia_actualizar(nombre,codigo,precio,marca,codigoAntiguo,datoAntiguo):
    sentencia = "UPDATE producto SET"
    segundo=False
    cant=0
    datos=[]
    if nombre!='':
        sentencia = sentencia+" nom='{}'"
        segundo=True
        datos.append(nombre)
        cant+=1
    if codigo!='':
        if segundo:
            sentencia = sentencia+", cod_bar ={}"
            datos.append(codigo)
            cant+=1
        else:
            segundo=True
            sentencia = sentencia+" cod_bar ={}"
            datos.append(codigo)
            cant+=1
    if precio!='':
        if segundo:
            sentencia = sentencia+", prec ={}"
            datos.append(precio)
            cant+=1
        else:
            segundo=True
            sentencia = sentencia+" prec ={}"
            datos.append(precio)
            cant+=1
    if marca!='':
        if segundo:
            sentencia = sentencia+", marca ='{}'"
            datos.append(marca)
            cant+=1
        else:
            segundo=True
            sentencia = sentencia+" marca ='{}'"
            datos.append(marca)
            cant+=1
    sentencia = sentencia+" WHERE cod_bar = {} and nom='{}' #"
    datos.append(codigoAntiguo)
    datos.append(datoAntiguo)
    while cant < 4:
        sentencia = sentencia+"{}"
        cant+=1
        datos.append(0)
    return datos,sentencia

def separNomCod(dato):
    pos=0
    codigo=[]
    for letra in reversed(dato):
        if letra == ' ':
            break
        pos+=1
    if pos >= len(dato):
        codigo=0
    else:
        codigo=dato[len(dato)-pos:]
    dato=dato[:len(dato)-pos-1]
    if dato[0]=='{':
        dato=dato[1:len(dato)-1]
    return codigo,dato

def actualizar_datos(nombre,codigo,precio,marca,label,datoAntiguo):
    label.grid_remove()
    if datoAntiguo!='':
        codigoAntiguo,datoAntiguo=separNomCod(datoAntiguo)
        if verificar_datos_act(codigo.get(),precio.get(),label):
            if CON_PROC.existe(datoAntiguo,codigoAntiguo):
                datos,sentencia=sentecia_actualizar(nombre.get(),codigo.get(),precio.get(),marca.get(),codigoAntiguo,datoAntiguo)
                CON_PROC.actualizarProd(datos,sentencia)
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

def verificar_datos_stock(_local,_bodega,label):
    try:
        local=int(_local)
        bodega=int(_bodega)
        if bodega < 0:
            label['text']='Error cantidad bodega menor a 0'
            label.grid(row=6,column=2,stick=NSEW)
            return False
        elif local<0:
            label['text']='Error cantidad local menor a 0'
            label.grid( row=6,column=2,stick=NSEW)
            return False
    except:
        if _local!='' or _bodega!='':
            label['text']='Error en el tipo de dato'
            label.grid(row=8,column=2,stick=NSEW)
            return False
        return True
    return True

def getCantidad(_cantLocal,_cantBodega):
    cantLocal=_cantLocal
    cantBodega=_cantBodega
    if _cantLocal=='':
        cantLocal=0
    if _cantBodega=='':
        cantBodega=0
    return cantLocal,cantBodega

def añadir_productos(cuadroNombre,cuadroCod,cuadroPrec,cuadroMarca,cuadroLocal,cuadroBodega,label_errorProd):
    label_errorProd.grid_remove()
    if verificar_datos(cuadroCod.get(),cuadroPrec.get(),label_errorProd) and verificar_datos_stock(cuadroLocal.get(),cuadroBodega.get(),label_errorProd):
        cantLocal,cantBodega=getCantidad(cuadroLocal.get(),cuadroBodega.get())
        nuevos_datos(cuadroNombre.get(),cuadroCod.get(),cuadroPrec.get(),cuadroMarca.get(),cantLocal,cantBodega)
    cuadroMarca.delete(0,END)
    cuadroCod.delete(0,END)
    cuadroPrec.delete(0,END)
    cuadroNombre.delete(0,END)
    cuadroLocal.delete(0,END)
    cuadroBodega.delete(0,END)

def nuevos_datos(nombre,codigo,precio,marca,cantLocal,cantBodega):
    datos=[nombre,int(cantLocal)+int(cantBodega),codigo,precio,marca,cantLocal,cantBodega]
    CON_PROC.agregarprod(datos)

def cantCorrecta(cant,label):
    try:
        cant=int(cant)
        if cant<=0:
            label['text']='Cantidad menor o igual a 0'
            return False
        return True
    except:
        label['text']='Tipo de dato erroneo'
        return False

def actualizar_stock(cant,opcion,label,nom,cod,opcionLocal):
    _cant=cant.get()
    cant.delete(0,END)
    label['text']=""
    if nom['text']==" " or cod['text']==" ":
        label['text']="Seleccione un Producto"
    elif opcion == 'None':
        label['text']="Marque un destino"
    elif cantCorrecta(_cant,label):
        if opcion == 'Tienda':
            if opcionLocal=='0':
                CON_PROC.actualizarStockLocal(nom['text'],cod['text'],int(_cant))
            elif opcionLocal=='1':
                if not(CON_PROC.actualizarStockLocalBodega(nom['text'],cod['text'],int(_cant))):
                    label['text']="No hay cantidad suficiente en bodega"
            else:
                label['text']="Marque una opcion"
        elif opcion == 'Bodega':
            CON_PROC.actualizarStockBodega(nom['text'],cod['text'],int(_cant))


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

def MostrarStock(combobox,nombre,codigo,precio,marca,stock,bodega,local):
    if combobox.get() != '':
        cod,nom=separNomCod(combobox.get())
        datos=list(CON_PROC.buscarprodUnico(nom,cod))
        nombre['text']=str(datos[1])
        codigo['text']=str(datos[3])
        precio['text']=str(datos[4])
        marca['text']=str(datos[5])
        stock['text']=str(datos[2])
        bodega['text']=str(datos[6])
        local['text']=str(datos[7])

def actualizarListaStock(buscarCuadro_revVentas,busqueda,opcionStock):
    lista=CON_PROC.buscarprod(busqueda)
    aux=[]
    for fila in lista:
        aux.append([fila[1],fila[3]])
    buscarCuadro_revVentas['values']=tuple(aux)

def mostrarLabel(labelNombre,labelCodigo,labelPrecio,labelMarca,dato):
    if dato != '':
        codigo,dato=separNomCod(dato)
        datos=list(CON_PROC.buscarprodUnico(dato,codigo))
        labelNombre['text']=str(datos[1])
        labelCodigo['text']=str(datos[3])
        labelPrecio['text']=str(datos[4])
        labelMarca['text']=str(datos[5])

def eliminar_producto(nombre,codigo,labelNom,labelCod,labelPrec,labelMarca):
    dato=[nombre['text'],codigo['text']]
    labelNom['text']=''
    labelCod['text']=''
    labelPrec['text']=''
    labelMarca['text']=''
    CON_PROC.eliminarProd(dato)

def mostrar_opciones(label,rbS,rbN):
    rbN.grid(row=3,column=6,sticky=W)
    rbS.grid(row=2,column=6,sticky=W)
    label.grid(row=1,column=6,sticky=W)

def esconder_opciones(label,rbS,rbN):
        rbS.grid_remove()
        rbN.grid_remove()
        label.grid_remove()

def mostrar_combobox_verStock(combobox,buttom):
    buttom.grid(row=5,column=2,sticky=NSEW)
    combobox.grid(row=5,column=1,sticky=NSEW)

def esconder_combobox_verStock(combobox,buttom):
    buttom.grid_remove()
    combobox.grid_remove()

def frame_verStock(frame,resultado,opcion):
    for widget in frame.winfo_children():
        widget.destroy()
    if opcion=='Producto':
        resultado=resultado[0]
        label='Stock General de '+resultado[0]+' ('+str(resultado[1])+') '+resultado[3]+' $'+str(resultado[2])
        labelNombre=Label(frame,text=label)
        labelNombre.pack()
        tree=ttk.Treeview(frame,column=("c1","c2"),show='headings')
        tree.column("# 1",anchor=CENTER,width=120)
        tree.heading("# 1",text='Almacenamiento')
        tree.column("# 2",anchor=CENTER,width=100)
        tree.heading("# 2",text='Cantidad')
        tree.insert('', 'end',text= "1",values=('General',resultado[4]))
        tree.insert('', 'end',text= "1",values=(resultado[8],resultado[7]))
        tree.insert('', 'end',text= "1",values=(resultado[6],resultado[5]))
        tree.pack()
    else:  
        tree=ttk.Treeview(frame,column=("c1","c2","c3","c4","c5"),show='headings')
        tree.column("# 1",anchor=CENTER,width=70)
        tree.heading("# 1",text='Nombre')
        tree.column("# 2",anchor=CENTER,width=100)
        tree.heading("# 2",text='Codigo Barra')
        tree.column("# 3",anchor=CENTER,width=70)
        tree.heading("# 3",text='Precio')
        tree.column("# 4",anchor=CENTER,width=70)
        tree.heading("# 4",text='Marca')
        tree.column("# 5",anchor=CENTER,width=70)
        tree.heading("# 5",text='Cantidad')
        for dato in resultado:
            tree.insert('', 'end',text= "1",values=dato)
        if opcion=='Bodega': 
            labelNombre=Label(frame,text='Stock en Bodega')
            labelNombre.pack()
            tree.pack()
        elif opcion=='Tienda':
            labelNombre=Label(frame,text='Stock en Tienda')
            labelNombre.pack()
            tree.pack()

def GenerarInformeStock(datosProd,opcion,frame):
    resultado=[]
    if opcion=='Producto':
        if datosProd!='':
            codigo,nombre=separNomCod(datosProd)
            resultado=CON_PROC.stock_producto(nombre,codigo)
            frame_verStock(frame,resultado,opcion)
    elif opcion=='Bodega':
        sentecia="select p.nom,p.cod_bar,p.prec,p.marca,sb.cant,b.direcb from producto as p, stock_bodega as sb, bodega as b where sb.id_bod=b.id_bod and b.id_bod=1 and sb.id_prod=p.id_prod;"
        resultado=CON_PROC.stocks_loc_bod(sentecia)
        frame_verStock(frame,resultado,opcion)
    elif opcion=='Tienda':
        sentecia="select p.nom,p.cod_bar,p.prec,p.marca,sl.cant,l.nom from producto as p, stock_local as sl, locall as l where sl.id_loc=l.id_loc and l.id_loc=1 and sl.id_prod=p.id_prod;"
        resultado=CON_PROC.stocks_loc_bod(sentecia)
        frame_verStock(frame,resultado,opcion)