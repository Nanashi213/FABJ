import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.lotes import Lotes
from MODELOS.eliminados import Eliminados

class LotesController():

    def __init__(self, ventana):
        self.lotes = Lotes()
        self.elim = Eliminados()
        self.ventana= ventana

    def insert_Lote(self,referencia,cantidad,precio_u,estado,idcliente):
        if referencia!="" and idcliente!="":
            if cantidad.isdigit() and precio_u.isdigit() and idcliente.isdigit():  
                self.lotes.insert_lote(referencia,cantidad,precio_u,estado,idcliente)
            else:
                QMessageBox.information(None, 'Fail', 'Cantidad Precio IDcliente deben ser numeros positivos sin signos')
        else:
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')

    
    def list_Lotes(self):
        table = self.ventana.table_mos_lotes
        Lotes = self.lotes.list_lotes()
        table.setRowCount(0)
        for row_number, row_data in enumerate(Lotes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def act_Lotes(self):
        table = self.ventana.table_mos_lotes
        clientes = []
        fila = []
        x=0
        y=0
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                clientes.append(fila)
            fila = []
        if len(clientes)>0:
            for clie in clientes:
                if clie[1].isdigit() and clie[2].isdigit():
                    self.lotes.act_lote(clie[0],clie[1],clie[2],clie[5].upper())
                    x=1
                else:
                    y=1
            if x==1 and y==0:
                QMessageBox.information(None, 'Success', 'Lote actualizado')
                self.list_Lotes()
            else:
                QMessageBox.information(None, 'Fail', 'Datos no validos')

            

    def bus_Lote(self,referencia):
        table = self.ventana.table_mos_abonos
        lote = self.lotes.bus_lote(referencia)
        if lote:
            table.setRowCount(0)
            for row_number, row_data in enumerate(lote):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
        else:
            QMessageBox.information(None, 'Fail', ' Referencia no encotrada')

    def buscar_lote_estado(self,estado):
        table = self.ventana.table_mos_abonos
        lote = self.lotes.bus_lotes_est(estado)
        if lote:
            table.setRowCount(0)
            for row_number, row_data in enumerate(lote):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.list_Lotes()
        else:
            QMessageBox.information(None, 'Fail', 'Referencia no encontrada')

    def act_Est_clie(self,opcion,referencia,estado,idcliente):
        lote = self.lotes.bus_lote_cam(referencia)
        if lote:
            self.lotes.act_est_clie(opcion,referencia,estado,idcliente)
            self.list_Lotes()
        else:
            QMessageBox.information(None, 'Success', 'Referencia no encontrada')

        
        
    def delete_Lote(self):
        table = self.ventana.table_mos_lotes
        if table.currentItem() != None:
            referencia = table.currentItem().text()
            lote = self.lotes.bus_lote_cam(referencia)
            if lote:
                self.elim.insert_eliminados("lotes",str(lote))
                self.lotes.delete_lote(referencia)
        self.list_Lotes()



