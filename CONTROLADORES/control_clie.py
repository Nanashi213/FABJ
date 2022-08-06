import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.clientes import Clientes
from MODELOS.eliminados import Eliminados

class ClieController():

    def __init__(self, ventana):
        self.clies = Clientes()
        self.elim = Eliminados()
        self.ventana= ventana

    def insert_Clie(self,idclie,nombre,direccion,tipo,contacto):
        if idclie=="" or nombre=="" or contacto=="":
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')
        else:
            if idclie.isdigit() and contacto.isdigit():  
                self.clies.insert_clie(idclie,nombre,direccion,tipo,contacto)
            else:
                QMessageBox.information(None, 'Fail', 'Datos no valida')

    
    def list_Clie(self):
        table = self.ventana.table_mos_clien
        clientes = self.clies.list_clie()
        table.setRowCount(0)
        for row_number, row_data in enumerate(clientes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def act_Clie(self):
        table = self.ventana.table_mos_clien
        clientes = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                clientes.append(fila)
            fila = []
        if len(clientes)>0:
            for clie in clientes:
                if clie[1]!=""  and clie[4].isdigit():
                    x = self.clies.act_clie(clie[0],clie[1],clie[2],clie[3],clie[4])
                else:
                    QMessageBox.information(None, 'Fail', 'Datos no validos')
            if x:
                QMessageBox.information(None, 'Success', 'Cliente actualizado')
            

    def bus_Clie(self,idclie):
        if idclie.isdigit():
            table = self.ventana.table_mos_clien
            clie = self.clies.bus_clie(idclie)
            if clie:
                table.setRowCount(0)
                for row_number, row_data in enumerate(clie):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                QMessageBox.information(None, 'Fail', ' NO EXISTE')
        else:
            QMessageBox.information(None, 'Fail', 'El ID no es valido')

    def delete_Clie(self):
        table = self.ventana.table_mos_clien
        if table.currentItem() != None:
            clie = table.currentItem().text()
            empleado = self.clies.bus_clie(clie)
            if empleado:
                self.elim.insert_eliminados("clientes",str(empleado))
                self.clies.delete_clie(clie)
        self.list_Clie()

    def clie_abn_pen(self,idclie):
        if idclie.isdigit():
            cliente = self.clies.clie_abo(idclie)
            if cliente:
                total = self.clies.clie_total(idclie)
                print(total,cliente[3])
                if cliente[3]==None or total == None:
                    deuda = 0
                else:
                    deuda =total - cliente[3]
                _translate = QtCore.QCoreApplication.translate
                self.ventana.Tex_ID.setText(_translate("clientes",str(cliente[0])))
                self.ventana.Tex_Nom.setText(_translate("clientes",str(cliente[1])))
                self.ventana.Text_Tipo.setText(_translate("clientes",str(cliente[2])))
                self.ventana.Text_Pag.setText(_translate("clientes",str(cliente[3])))
                self.ventana.Tex_deuda.setText(_translate("clientes",str(deuda)))
            else:
                QMessageBox.information(None, 'Fail', ' NO EXISTE')
        else:
            QMessageBox.information(None, 'Fail', 'El ID no es valido')




