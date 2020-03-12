# coding=utf-8
"""

    Módulo que gestiona los clientes

"""

import conexion, sqlite3, variables, datetime

def clearEntry(fila):
    """
    Limpia los entries
    :param fila:
        Contiene el listado de widgets que van a limpiar tras ejecutar un evento
    :return:
        No devuelve nada
    """
    variables.lblerrordni[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')

def validarDNI(dni):

    """
    Comprueba que el dni sea válido
    :param dni:
        Valor del dni del cliente
    :return:
        Retorna un boolean
    """
    try:

        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0','Y':'1','Z':'2'}
        numeros = "1234567890"
        dni = dni.upper()

        if len(dni) == 9:

            dig_control = dni[8]
            dni = dni[:8]

            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])

            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control

        return False

    except Exception as e:
         print (e)
         return None


def insertarcli(fila):
    """
    Inserta un cliente en la BD.
    :param fila:
        Contiene los datos necesarios para cargar el cliente
    :return:
        No retorna
    """

    try:
        conexion.cur.execute('insert into clientes (dni,Apellidos,Nombre,Fecha) values (?,?,?,?)',fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listar():

    """
    Recoge todos los datos de los clientes de la bd y los carga en una variable
    :return:
        Retorna el listado con todos los clientes que ha encontrado en la bd
    """

    try:
        conexion.cur.execute('Select * from clientes')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def bajaCli(dni):
    """
    Elimina un cliente de la BD.
    :param dni:
        Dni del cliente a eliminar
    :return:
        No retorna
    """

    try:
        conexion.cur.execute("delete from clientes where dni = ?",(dni,))
        listadocli(variables.listclientes)
        clearEntry(variables.filacli)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifCli(registro,cod):

    """
    Modificar datos a un cliente
    :param registro:
        Contiene los nuevos datos del cliente
    :param cod:
        Codigo autogenerado del cliente
    :return:
        No retorna
    """

    try:
        conexion.cur.execute("update clientes set dni = ?, Apellidos = ? , Nombre = ?, Fecha = ? where id = ?",(registro[0],registro[1],registro[2],registro[3],cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadocli(listclientes):

    """
    Carga los datos de los clientes en el listView
    :param listclientes:
        Lista de los clientes ya registrados
    :return:
        No retorna
    """

    try:
        variables.listado = listar()
        print(variables.listado)
        listclientes.clear()
        for registro in variables.listado:
            codigo = variables.listado[0]
            listclientes.append(registro[1:5])

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def selectcli(dni):

    """
    Busca el id del cliente
    :param dni:
        Dni del cliente a buscar
    :return:
        Retorna el id del cliente
    """

    try:
        conexion.cur.execute('select id from clientes where dni = ?',(dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def findNombre(dni):

    """
    Busca el nombre del cliente
    :param dni:
        Contiene el dni del cliente
    :return:
        Retorna el nombre del cliente
    """

    try:

        conexion.cur.execute('select nombre from clientes where dni = ? ',(dni,))
        nombre = conexion.cur.fetchall()
        conexion.conex.commit()
        return nombre[0][0]
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def findApellidos(dni):

    """
    Busca los apellidos del cliente
    :param dni:
        Contiene el dni del cliente
    :return:
        Retorna el campo apellido del cliente
    """

    try:

        conexion.cur.execute('select apellidos from clientes where dni = ? ',(dni,))
        apellido = conexion.cur.fetchall()
        conexion.conex.commit()
        return apellido[0][0]
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def apelnomfac(dni):

    """
    Busca el nombre y los apellidos del cliente
    :param dni:
        Contiene el dni del cliente
    :return:
        Retorna el nombre y los apellidos del cliente con dicho dni.
    """

    try:

        conexion.cur.execute('select Apellidos, Nombre from clientes where dni = ?',(dni,))
        apelnome = conexion.cur.fetchall()
        conexion.conex.commit()
        return apelnome[0]

    except sqlite3.OperationalError as e:
        print(e)


def convertirFecha(fecha):

    """
    Convierte la fecha a formato excel
    :param fecha:
        Fecha a convertir
    :return:
        Retorna la fecha convertida
    """

    temp = datetime.datetime(1899, 12, 30)
    delta = fecha - temp
    return float(delta.days) + (float(delta.secondas)/ 86400)