# coding=utf-8
from gi.repository import Gtk, Gdk
import gi, eventos, conexion, variables, funcionesCli, funcionesHab, funcionesReservas, funcionesServicios
gi.require_version('Gtk','3.0')

'''

El main contiene los elemnentos necesarios para lanzar la aplicación
asi como la decleración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas.

'''


class Empresa:
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('ventana2020.glade')

        self.vprincipal = b.get_object("vPrincipal")

        # Declaración de Widgets
        self.entdni = b.get_object('entDni')
        self.entapellidos = b.get_object('entApellidos')
        self.entnombre = b.get_object('entNombre')
        self.lblerrordni = b.get_object('lblErrorDni')
        self.lblcodcli = b.get_object('lblCodCli')
        self.vencalendar = b.get_object('venCalendar')
        self.calendar = b.get_object('Calendar')
        self.entfechaCli = b.get_object('entFechaCli')
        variables.panel = b.get_object('Panel')
        variables.filacli = (self.entdni, self.entapellidos, self.entnombre, self.entfechaCli)
        variables.listclientes = (b.get_object('listClientes'))
        variables.treeclientes = (b.get_object('treeClientes'))
        variables.lblerrordni = (self.lblerrordni, self.lblcodcli)
        variables.lbladded = b.get_object('lblAdded')
        variables.lblfecha = b.get_object('lblFecha')
        variables.vencalendar = self.vencalendar
        variables.calendar = self.calendar

        # Variables Habitaciones
        self.entnumero = b.get_object('entNumero')
        self.rbsimple = b.get_object('rbSimple')
        self.rbdouble = b.get_object('rbDouble')
        self.rbfamiliar = b.get_object('rbFamiliar')
        self.entprecio = b.get_object('entPrecio')
        variables.switch = b.get_object('Switch')

        # Variables Acerca de:
        variables.venacercade = b.get_object('venAbout')

        variables.venfile = b.get_object('venFile')
        variables.menubar = b.get_object('menuBar').get_style_context()

        # Preparando para backup
        #variables.vendialog = b.get_object('venDialog')
        variables.lblmensajedialog = b.get_object('lblMensajeDialog')
        variables.vendialogcorrecto = b.get_object('venDialogCorrecto')
        variables.venfiledialog = b.get_object('venFileDialog')

        variables.filahab = (self.entnumero, self.entprecio)
        variables.filarbt = (self.rbsimple, self.rbdouble, self.rbfamiliar)
        variables.listhabitaciones = (b.get_object('listHabitaciones'))
        variables.treehabitaciones =  (b.get_object('TreeHabitaciones'))

        # Reservas
        variables.lblreservasdni = b.get_object('lblReservasDni')
        variables.lblreservasapellidos = b.get_object('lblReservasApellidos')
        variables.listhabitacionescombobox = b.get_object('ListHabitacionesComboBox')
        variables.lblnumnoches = b.get_object('lblNumNoches')
        variables.btncheckin = b.get_object('btnCheckIn')
        variables.btncheckout = b.get_object('btnCheckOut')
        variables.entcheckin = b.get_object('entCheckIn')
        variables.entcheckout = b.get_object('entCheckOut')
        variables.cmbreserhabitacion = b.get_object('cmbReservasHabitacion')
        variables.filareserva = (variables.lblreservasdni, variables.lblreservasapellidos,variables.entcheckin,variables.entcheckout,variables.lblnumnoches)
        variables.listreservas = (b.get_object('listReservas'))
        variables.treereservas = (b.get_object('treeReservas'))
        variables.vencalendarr1 = self.vencalendar
        variables.vencalendarr2 = self.vencalendar

        # Variables Facturación
        variables.lbldnifacturacion = b.get_object('lblDniFacturacion')
        variables.lblapellidosfacturacion = b.get_object('lblApellidosFacturacion')
        variables.lblnombrefacturacion = b.get_object('lblNombreFacturacion')
        variables.lblcodigoreserva = b.get_object('lblCodigoReserva')
        variables.lblhabitacionfacturacion = b.get_object('lblHabitacionFacturacion')
        variables.lblfechafacturacion = b.get_object('lblFechaFacturacion')

        variables.lblnochesfac = b.get_object('lblNochesFac')
        variables.lblunidadesfac = b.get_object('lblUnidadesFac')
        variables.lblpreciounidadfac = b.get_object('lblPrecioUnidadFac')
        variables.lbltotalunifac = b.get_object('lblTotalUniFac')
        
        variables.filafacturacion = (variables.lblnochesfac, variables.lblunidadesfac, variables.lblpreciounidadfac, variables.lbltotalunifac)

        # Variables Servicios
        #-------------------------------------------------------------------------
        variables.lblreservaservicio = b.get_object('lblReservaServicio')
        variables.lblhabitacionservicio = b.get_object('lblHabitacionServicio')
        variables.btnradioalojamiento = b.get_object('btnRadioAlojamiento')
        variables.btnradiodesayuno = b.get_object('btnRadioDesayuno')
        variables.btnradiocomida = b.get_object('btnRadioComida')
        variables.radiobuttonservicios = (variables.btnradioalojamiento,variables.btnradiodesayuno,variables.btnradiocomida)
        variables.enttiposervicio = b.get_object('entTipoServicio')
        variables.entprecioservicio = b.get_object('entPrecioServicio')
        variables.listservicios = b.get_object('listServicios')
        variables.treeservicios = b.get_object('treeServicios')
        variables.btncheckparking = b.get_object('btnCheckParking')

        # Factura
        # ----------------------------------------------------------------
        variables.lbls0 = b.get_object('lblS0')
        variables.lbls4 = b.get_object('lblS4')
        variables.lbls8 = b.get_object('lblS8')
        variables.lbls12 = b.get_object('lblS12')
        variables.lbls16 = b.get_object('lblS16')
        variables.lbls20 = b.get_object('lblS20')
        variables.lbls24 = b.get_object('lblS24')
        variables.lbls28 = b.get_object('lblS28')
        variables.lbls32 = b.get_object('lblS32')
        variables.lbls36 = b.get_object('lblS36')
        variables.lbls40 = b.get_object('lblS40')
        variables.lbls44 = b.get_object('lblS44')

        variables.conceptosservicios = (
            variables.lbls0,
            variables.lbls4,
            variables.lbls8,
            variables.lbls12,
            variables.lbls16,
            variables.lbls20,
            variables.lbls24,
            variables.lbls28,
            variables.lbls32,
            variables.lbls36,
            variables.lbls40,
            variables.lbls44)

        variables.lbls3 = b.get_object('lblS3')
        variables.lbls7 = b.get_object('lblS7')
        variables.lbls11 = b.get_object('lblS11')
        variables.lbls15 = b.get_object('lblS15')
        variables.lbls19 = b.get_object('lblS19')
        variables.lbls23 = b.get_object('lblS23')
        variables.lbls27 = b.get_object('lblS27')
        variables.lbls31 = b.get_object('lblS31')
        variables.lbls35 = b.get_object('lblS35')
        variables.lbls39 = b.get_object('lblS39')
        variables.lbls43 = b.get_object('lblS43')
        variables.lbls47 = b.get_object('lblS47')

        variables.preciosconcepto = (
            variables.lbls3,
            variables.lbls7,
            variables.lbls11,
            variables.lbls15,
            variables.lbls19,
            variables.lbls23,
            variables.lbls27,
            variables.lbls31,
            variables.lbls35,
            variables.lbls39,
            variables.lbls43,
            variables.lbls47)

        variables.lblpreciosiniva = b.get_object('lblSinIva')
        variables.lblprecioiva = b.get_object('lblPrecioIva')
        variables.lblpreciototal = b.get_object('lblPrecioTotal')
        variables.facturafinal = (variables.lblpreciosiniva, variables.lblprecioiva, variables.lblpreciototal)


        b.connect_signals(eventos.Eventos())

        # Estilos
        self.set_styles()
        variables.menubar.add_class('menuBar')
        self.vprincipal.show_all()
        conexion.Conexion().abrirBBDD()
        funcionesCli.listadocli(variables.listclientes)
        funcionesHab.listadohab(variables.listhabitaciones)
        funcionesReservas.listadoreservas(variables.listreservas)
        funcionesReservas.listadonumhab(self)



    def set_styles(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('styles.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == '__main__':
    main = Empresa()
    Gtk.main()