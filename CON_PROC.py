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
                print(fila[1],fila[2],fila[3],fila[4])
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

def buscarprodUnico (nom,cod)  :
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
            sentencia = "SELECT * FROM producto WHERE nom='{}' and cod_bar={}"
            cursor.execute(sentencia.format(nom,cod))
            resultados = cursor.fetchall()
        else    :
            print("Dato no encontrado") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
            return resultados[0]
        return resultados[0]
                        
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
            sentencia = "INSERT INTO producto (nom, cant, cod_bar, prec) VALUES ('{0}',{1},{2},{3})".format(datos[0], datos[1], datos [2],datos [3])
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
def actualizarProd (datos)  :
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
            sentencia = "UPDATE producto SET nom='{}', cant ={}, prec={} WHERE cod_bar = {}"
            cursor.execute(sentencia.format(datos[0], datos[1], datos[3], datos[2]))
            conexion.commit()
            print("Registro actualizado con exito") 
    except Error as ex :
        print("Error de conexion", ex)
    finally :
        if  conexion.is_connected() :
            conexion.close() #cierro conexion con la base
            print("Conexion finalizada.")
 
            
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