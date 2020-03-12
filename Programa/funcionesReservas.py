# coding=utf-8
import conexion, sqlite3, variables
from datetime import datetime


# --------------------------------------------------------------------
def clearEntry(fila):
    """
    Limpia los entries
    :param fila:
        Contiene el listado de widgets que van a limpiar tras ejecutar un evento
    :return:
        No devuelve nada
    """
    for i in range(len(fila)):
        fila[i].set_text('')
    variables.cmbreserhabitacion.set_active(-1)

# --------------------------------------------------------------------
def calculardias():
    """
    Calcula los dias que hay entre dos fechas
    :return:
        No retorna
    """

    diaentrada = variables.filareserva[2].get_text()
    diasalida = variables.filareserva[3].get_text()
    if diaentrada != '' and diasalida !='':
        date_in = datetime.strptime(diaentrada, '%d/%m/%Y').date()
        date_out = datetime.strptime(diasalida, '%d/%m/%Y').date()
        noches = (date_out-date_in).days
        if noches < 0:
            variables.lblnumnoches.set_text("0")
        else:
            variables.lblnumnoches.set_text(str(noches))

# --------------------------------------------------------------------
def insertarReservas(fila):
    """
    Inserta reservas en la BD
    :param fila:
        Contiene los datos necesarios para cargar una reserva
    :return:
        No retorna
    """

    try:

        conexion.cur.execute('insert into reservas (dni,Apellidos,numHabitacion,checkIn,checkOut,Noches) values(?,?,?,?,?,?)',fila)
        conexion.conex.commit()
        clearEntry(variables.filareserva)
    except Exception as e:
        print("Insertar Reserva Funcion",e)

# --------------------------------------------------------------------
def bajasReservas(dni,fecha):
    """
    Elimina una reserva
    :param dni:
        Contiene el dni dueño de la reserva
    :param fecha:
        Contiene la fecha de dicha reserva
    :return:
        No retorna
    """
    try:

        conexion.cur.execute('delete from Reservas where dni = ? and checkIn = ?',(dni,fecha,))
        conexion.conex.commit()
        listadoreservas(variables.listreservas)
        clearEntry(variables.filareserva)

    except Exception as e:
        print("Error bajas reservas",e)

# --------------------------------------------------------------------
def modificarReserva(registro):
    """
    Modifica una reserva
    :param registro:
        Contiene los datos modificados mas los no modificados
    :return:
        No retorna
    """

    try:
        if len(registro) < 6:
            conexion.cur.execute('update reservas set dni = ?, Apellidos = ?, numHabitacion = ?,checkIn = ?,checkOut = ?, Noches = ? where dni = ?',(registro[0],registro[1], registro[2],registro[3],registro[4],registro[5],registro[0]))
            conexion.conex.commit()
        else:
            conexion.cur.execute('update reservas set dni = ?, Apellidos = ?, numHabitacion = ?,checkIn = ?,checkOut = ?, Noches = ? where dni = ?',(registro[0],registro[1], registro[2],registro[3],registro[4],registro[5],registro[6]))
            conexion.conex.commit()

    except Exception as e:
        print("Error modificar funcion",e)
        conexion.conex.rollback()

def listar():
    """
    Carga todos los datos de las reservas en la bd
    :return:
        Retorna una variable con todos los datos cargados
    """

    try:
        conexion.cur.execute('Select * from reservas')
        listadoReservas = conexion.cur.fetchall()
        conexion.conex.commit()
        return listadoReservas

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

# --------------------------------------------------------------------
def listadonumhab(self):

    """
    Carga los numeros de las habitaciones en un variable y luego los carga en el comboBox
    :return:
        No retorna
    """
    try:
        conexion.cur.execute('select numeroHabitacion from habitaciones')
        listado = conexion.cur.fetchall()
        variables.listhabitacionescombobox.clear()
        for row in listado:
            variables.listhabitacionescombobox.append(row)
            conexion.conex.commit()
    except Exception as e:
        print(e)
        conexion.conex.rollback()

# --------------------------------------------------------------------
def listadoreservas(listreservas):
    """
    Carga en el listView los datos de las reservas
    :param listreservas:
        Contiene el listView de reservas
    :return:
        No retorna
    """
    try:
        variables.listado = listar()
        print(variables.listado)
        listreservas.clear()
        for registro in variables.listado:
            listreservas.append(registro[0:6])


    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

# --------------------------------------------------------------------
def buscarHabitacion(habitacion):
    """
    Cambia el valor del comboBox al hacer click en el treeView
    :param habitacion:
        Numero de la habitacion a marcar en el comboBox
    :return:
        No retorna
    """
    try:
        contador = 0
        conexion.cur.execute('select numeroHabitacion from habitaciones')
        variables.numhab = conexion.cur.fetchall()
        conexion.conex.commit()

        for numero in variables.numhab:

            if numero[0] == habitacion:
                variables.cmbreserhabitacion.set_active(contador)
            else:
                contador += 1

    except Exception as e:
        print(e)

# --------------------------------------------------------------------
def findID(dni,habitacion):

    """
    Buscar el id de la reserva
    :param dni:
        Contiene el dni a buscar del dueño de la reserva
    :param habitacion:
            Contiene el numero de la habitación que pertenece a dicha reserva
    :return:
        Retorna el código de la reserva
    """

    try:

        conexion.cur.execute('select codigo from reservas where dni = ? and numHabitacion = ?',(dni,habitacion,))
        codigo = conexion.cur.fetchall()
        conexion.conex.commit()
        return codigo[0][0]

    except Exception as e:
        print("funcion buscar ID",e)

