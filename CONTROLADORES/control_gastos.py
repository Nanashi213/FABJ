import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.gastos import Gastos
from MODELOS.eliminados import Eliminados
import datetime


class GastController():

    def __init__(self, ventana):
        self.gast= Gastos()
        self.elim = Eliminados()
        self.ventana= ventana

    def insert_Gastos(self,fecha,descripcion,total):
        if descripcion!="" and total!="":
            if total.isdigit():
                if (isinstance(total,float) or isinstance(total,int)):
                    self.gast.insert_gasto(fecha,descripcion,total)
            else:
                QMessageBox.information(None, 'Fail', 'Monto debe ser numero positivo sin signos')
        else:
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')


    def list_Gastos(self):
        table = self.ventana.table_mos_gastos
        gastos = self.gast.list_gastos()
        table.setRowCount(0)
        for row_number, row_data in enumerate(gastos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def bus_Entrefec(self,fecha1,fecha2):
        _translate = QtCore.QCoreApplication.translate
        total = self.ventana.texTOTAL
        table = self.ventana.table_mos_gastos
        gastos = self.gast.bus_gas_fecha(fecha1,fecha2)
    
        if gastos:
            texto = self.gast.total_gas(fecha1,fecha2)
            total.setText(_translate("Gastos",str(texto[0][0])))
            table.setRowCount(0)
            for row_number, row_data in enumerate(gastos):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            QMessageBox.information(None, 'Fail', 'Fechas no encontradas')


    def act_Gasto(self):
        table = self.ventana.table_mos_gastos
        gasts = []
        fila = []
        x=0
        y=0
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                gasts.append(fila)
            fila = []
        if len(gasts)>0:
            for gas in gasts:
                if gas[1]!="" and gas[2]!="" and gas[3].isdigit():
                    self.gast.act_gasto(int(gas[0]),gas[1],gas[2],gas[3])
                    x=1
                else:
                    y=1
            if x==1 and y==0:
                QMessageBox.information(None, 'Success', 'Gasto actualizado')
            else:
                QMessageBox.information(None, 'Fail', 'Datos no validos')

    def delete_Gast(self):
        table = self.ventana.table_mos_gastos
        if table.currentItem() != None:
            numg = table.currentItem().text()
            gasto = self.gast.bus_gas_num(numg)
            if gasto:
                self.gast.delete_gast(numg)
        self.list_Gastos()





