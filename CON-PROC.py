from typing import Counter
import mysql.connector
from mysql.connector import Error

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

def datosdeprueba ()    :
    nombre = "pampita"
    cantidad = 11
    codigo_de_barras = 4321
    precio = 150
    
    producto = (nombre, cantidad, codigo_de_barras, precio)
    return producto

#pruebas
productos = datosdeprueba()   
#agregarprod(productos)    

#eliminar producto
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
 
eliminarProd(productos)
                
            
