# coding=utf-8
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os, funcionesCli, variables, funcionesServicios

"""
    Módulo que permite crear nuestros PDFs
"""

def basico():
    """
    Contiene el molde del pdf
    :return:
        No retorna
    """
    try:

        global bill
        bill = canvas.Canvas('prueba.pdf', pagesize = A4)
        text1 = 'Bienvenido a nuestro hotel'
        text2 = 'CIF:00000000A'
        bill.drawImage("../img/hotel.png", 475, 670, width=64, height=64)
        bill.setFont('Helvetica-Bold', size= 16)
        bill.drawString(250, 780, 'Hote Lite')

        bill.setFont('Times-Italic', size = 8)
        bill.drawString(240, 765, text1)
        bill.drawString(260,755,text2)

        bill.line(50, 660, 540, 660)

        textpie = ('Hotel Lite, CIF = 000000000A, Tlf = 986000000, email =  info@hotelite.com')
        bill.setFont('Times-Italic', size = 7)
        bill.drawString(170, 20, textpie)

        bill.line(50, 30, 540, 30)


    except Exception as e:
        print('Error módulo basico', e)

def factura():
    """
    Estructura de los datos en el pdf
    :return:
        No retorna
    """
    try:
        basico()

        bill.setTitle('FACTURA:')

        bill.setFont('Helvetica-Bold', size = 8)
        text3 = 'Número de Factura:'
        bill.drawString(50, 735, text3)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(140,735,variables.datosfactura[0].get_text())

    # --------------------------------------------------------------

        bill.setFont('Helvetica-Bold', size = 8)
        text4 = 'Fecha Factura:'
        bill.drawString(300,735, text4)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(380,735, variables.datosfactura[1].get_text())

    # --------------------------------------------------------------

        bill.setFont('Helvetica-Bold', size=8)
        text5 = 'DNI Cliente:'
        bill.drawString(50,710, text5)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(120, 710, variables.datosfactura[2].get_text())

    # --------------------------------------------------------------

        bill.setFont('Helvetica-Bold', size=8)
        text6 = 'Nº de Habitacion: '
        bill.drawString(300, 710,text6)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(380,710, variables.datosfactura[3].get_text())

    # --------------------------------------------------------------

        apelnome = funcionesCli.apelnomfac(variables.datosfactura[2].get_text())
        bill.setFont('Helvetica-Bold',size = 8)
        text7 = 'Apellidos: '
        bill.drawString(50,680,text7)
        bill.setFont('Helvetica', size=8)
        bill.drawString(110,680, apelnome[0])

    # ---------------------------------------------------------------

        bill.setFont('Helvetica-Bold',size = 8)
        text8 = 'Nombre:'
        bill.drawString(300,680,text8)
        bill.setFont('Helvetica', size=9)
        bill.drawString(350,680, apelnome[1])

    # ---------------------------------------------------------------

        bill.setFont('Helvetica-Bold', size = 10)
        text9 = ['CONCEPTO', 'UNIDADES', 'PRECIO/UNIDAD', 'TOTAL']
        x = 75

    # ---------------------------------------------------------------
        bill.line(50, 635, 540, 635)

        for i in range(0, 4):
            bill.drawString(x, 645, text9[i])
            x += 132
        listado = funcionesServicios.listarserviciosprecio(variables.datosfactura[0].get_text())
        x = 75
        y = 620

    # ---------------------------------------------------------------
        for i in range(4):
            if i == 0:
                bill.drawString(x, y, variables.filafacturacion[0].get_text())
                x += 150
            else:
                if i == 3:
                    x += 34
                    bill.drawRightString(x, y, (variables.filafacturacion[i].get_text() + '€'))
                else:
                    bill.drawString(x, y, variables.filafacturacion[i].get_text())
                x = x + 123
        x = 75
        y = y - 20

    # ---------------------------------------------------------------
        for registro in listado:
            for i in range(2):
                if i == 1:
                    x += 40
                    bill.drawRightString(x, y, str(registro[i]) + '€')
                else:
                    bill.drawString(x, y, str(registro[i]))
                x = x + 390
            y = y - 20
            x = 75

    # ---------------------------------------------------------------
        bill.line(50, 120, 540, 120)
    # ---------------------------------------------------------------
        textSubTotal = ('Subtotal :   '+variables.facturafinal[0].get_text()+"€")
        bill.drawRightString(495, 100, str(textSubTotal))
    # ---------------------------------------------------------------
        textIva = ('IVA :     ' + variables.facturafinal[1].get_text()+"€")
        bill.drawRightString(495, 80, str(textIva))
    # ---------------------------------------------------------------
        textTotal = ('TOTAL :   '+ variables.facturafinal[2].get_text())
        bill.drawRightString(495, 60, str(textTotal))
    # -----------------------------------------------------------------

        bill.showPage()
        bill.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/prueba.pdf')

    except Exception as e:
        print('Error en el módulo factura ',e)

def clientes():

    try:

        lista_clientes = canvas.Canvas('clientes.pdf', pagesize=A4)
        lista_clientes.setTitle('Listado De Clientes')
        lista_clientes.setFont('Helvetica-Bold', size=16)
        lista_clientes.drawString(230, 780, 'Listado Clientes')
        lista_clientes.setFont('Helvetica-Bold', size=12)
        lista_clientes.drawString(50, 740, 'DNI')
        lista_clientes.drawString(250, 740, 'Apellidos')
        lista_clientes.drawString(450, 740, 'Nombre')
        lista_clientes.line(50, 760, 540, 760)
        lista_clientes.setFont('Helvetica', size=8)
        lista_clientes.line(50, 730, 540, 730)

        listado = funcionesCli.listar()
        y = 710
        pagina = 1
        cambiar = True

        for registro in listado:

            if y > 10:
                lista_clientes.drawString(50, y, registro[1])
                lista_clientes.drawString(250, y, registro[2])
                lista_clientes.drawString(450, y, registro[3])
                lista_clientes.line(50, y-2, 540, y-2)
                y = y - 10
            else:
                if cambiar:
                    lista_clientes.showPage()
                    canvas.Canvas._pageNumber = pagina + 1
                    y = 710
                    lista_clientes.setFont('Helvetica-Bold', size=16)
                    lista_clientes.setFont('Helvetica-Bold', size=12)
                    lista_clientes.drawString(50, 740, 'DNI')
                    lista_clientes.drawString(250, 740, 'Apellidos')
                    lista_clientes.drawString(450, 740, 'Nombre')
                    lista_clientes.line(50, 760, 540, 760)
                    lista_clientes.setFont('Helvetica', size=8)
                    lista_clientes.line(50, 730, 540, 730)
                lista_clientes.setFont('Helvetica', size = 8)
                lista_clientes.drawString(50, y, registro[1])
                lista_clientes.drawString(250, y, registro[2])
                lista_clientes.drawString(450, y, registro[3])
                lista_clientes.line(50, y-2, 540, y-2)
                cambiar = False
                y = y - 10

        lista_clientes.showPage()
        lista_clientes.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open '+ dir + '/clientes.pdf')

    except Exception as e:
        print("Error imprimir clientes ", e)