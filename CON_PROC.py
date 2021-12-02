from typing import Counter
import mysql.connector
from mysql.connector import Error

#Buscar producto (si se pasa una tupla se cae xd)
def buscarprod (datos)  :
    resultados=[]
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
        )
        if conexion.is_connected() :
            print("Conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = "SELECT * FROM producto WHERE nom like '%{}%'"
            cursor.execute(sentencia.format(datos))
            resultados = cursor.fetchall()
            for fila in resultados  :
                print(fila[1],fila[2],fila[3],fila[4],fila[5])
        else    :
            print("Dato no encontrado") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
            return resultados
        return resultados
                        
#Agregar producto
def agregarprod (datos)  :
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
    )
        if conexion.is_connected() :
            print("Conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = "INSERT INTO producto (nom, cant, cod_bar, prec, marca) VALUES ('{0}',{1},{2},{3},'{4}')".format(datos[0], datos[1], datos [2],datos [3],datos[4])
            cursor.execute(sentencia)
            conexion.commit()
            print("Registro insertado con exito") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")

#Eliminar producto
def eliminarProd (datos)  :
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
    )
        if conexion.is_connected() :
            print("conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = "DELETE FROM producto WHERE nom='{}' AND cod_bar ={}".format(datos[0],datos[2])
            cursor.execute(sentencia)
            conexion.commit()
            print("Registro eliminado con exito") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
                
#Actualizar producto
def actualizarProd (datos,_sentencia)  :
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
    )
        if conexion.is_connected() :
            print("conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = _sentencia
            cursor.execute(sentencia.format(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
            conexion.commit()
            print("Registro actualizado con exito") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")

def existe (nom,cod)  :
    resultados=[]
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
    )
        if conexion.is_connected() :
            print("conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = "SELECT * FROM producto WHERE nom='{}' and cod_bar={}"
            cursor.execute(sentencia.format(nom,cod))
            resultados = cursor.fetchall()
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
    if resultados==[]:
        return False
    return True
 
            
#BUSCAR STOCK DE UN PRODUCTO
def buscarstockUnico (nom)  :
    resultados=[]
    try :
        conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'admin1234',
        db = 'todomarket_vip'
        )
        if conexion.is_connected() :
            print("Conexion exitosa.")
            cursor=conexion.cursor()
            sentencia = "SELECT producto.nom, stock_local.cant FROM stock_local, producto WHERE producto.nom = '{}'"
            cursor.execute(sentencia.format(nom))
            resultados = cursor.fetchall()
        else    :
            print("Dato no encontrado") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
            return resultados
        return resultados
    
    #PPRUEBAS
nombre = 'azucar '#'coca cola' #"pampita"
cantidad = 10 #110
codigo_de_barras = 55
precio = 1500 #20000
    
producto = (nombre, cantidad, codigo_de_barras, precio) 
 
#agregarprod(producto)  
#eliminarProd(producto)
#actualizarProd(producto)
#buscarprod('azucar') 
#buscar = buscarstockUnico('leche')
#for fila in buscar  :
    #print(fila[0], fila[1])
