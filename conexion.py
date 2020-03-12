# coding=utf-8
import sqlite3, variables

#Clase de Examen

class Conexion:

    def abrirBBDD(self):
        """
        Abre la base de datos
        :return:
            No retorna
        """

        try:

            global bbdd, conex, cur

            bbdd = 'empresa.sqlite'         #Variable almacena base de datos

            conex = sqlite3.connect(bbdd)   #Abrimos la base de datos
            cur = conex.cursor()            #cursor

            print('Conexión a base de datos realizada correctamente')

        except sqlite3.OperationalError as e:
            print('Error al abrir: ', e)

    def cerrarBBDD(self):
        """
        Cierra la base de datos
        :return:
            No retorna
        """

        try:
            cur.close()
            conex.close()

            print('Conexion a base de datos cerrada correctamente')

        except sqlite3.OperationalError as e:
            print('Error al cerrar', e)