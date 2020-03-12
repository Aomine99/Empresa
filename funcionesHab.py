# coding=utf-8
"""
    Módulo que gestiona las habitaciones
"""
import variables, conexion, sqlite3

def clearEntry(fila):
    """
    Limpiar los entry de la interfaz de habitación
    :param fila:
        Contiene el listado de widgets que van a limpiar tras ejecutar un evento
    :return:
        No retorna
    """
    variables.lblerrordni[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')

def insertarhab(fila):
    """
    Inserta las habitaciones en la base de datos
    :param fila:
        Contiene los datos necesarios para dar de alta la habitación
    :return:
        No retorna
    """

    try:
        conexion.cur.execute('insert into habitaciones (numeroHabitacion,tipo,precio) values (?,?,?)',fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajaHab(numero):
    """
    Elimina una habitación
    :param numero:
        Es el numero de la habitación a borrar
    :return:
        No retorna
    """

    try:
        conexion.cur.execute("delete from habitaciones where numeroHabitacion = ?", (numero,))
        listadohab(variables.listhabitaciones)
        clearEntry(variables.filahab)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modificarHab(registro):
    """
    Modifica los datos de una habitación
    :param registro:
        Contiene el _numero, _tipo, _precio, _ocupado
    :return:
        No retorna
    """

    try:

        conexion.cur.execute("update habitaciones set numeroHabitacion = ?, tipo = ?, precio = ? where numeroHabitacion = ?",(registro[0],registro[1],registro[2], registro[0],))
        conexion.conex.commit()

    except Exception as e:
        print("Error funcion modificar",e)

def listar():
    """
    Carga una variable con todos los datos de las habitaciones
    :return:
        Retorna una variable con los datos de las habitaciones
    """
    try:
        conexion.cur.execute('Select * from habitaciones')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        conexion.conex.rollback()

def listadohab(listhabitaciones):
    """
    Carga los datos de las habitaciones en el listView
    :param listhabitaciones:
        Contiene datos de las habitaciones
    :return:
        No retorna
    """
    try:
        variables.listado = listar()
        listhabitaciones.clear()
        for registro in variables.listado:
            listhabitaciones.append(registro[0:3])

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def findPrecio(habitacion):

    """
    Busca el precio de la habitación
    :param habitacion:
        Contiene el numero de la habitación a buscarº
    :return:
        Retorna el precio de la habitación
    """

    try:

        conexion.cur.execute('select precio from habitaciones where numeroHabitacion = ?',(habitacion,))
        precio = conexion.cur.fetchall()
        conexion.conex.commit()
        return precio[0][0]

    except Exception as e:
        print("Error funcion buscar precio",e)


def precioTotal(noches, precio):
    """
    Calcula el precio total
    :param noches:
        Contiene el numero de noches
    :param precio:
        Contiene el precio de la habitación
    :return:
        Retorna el precio total una vez comentada
    """
    total = int(noches) * precio
    round(total)
    variables.precionoches = total
    return total