import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.abonos import Abonos
from MODELOS.eliminados import Eliminados

class AbonosController():

    def __init__(self, ventana):
        self.abonos = Abonos()
        self.elim = Eliminados()
        self.ventana= ventana
    
    def list_Abo(self):
        table = self.ventana.table_mos_abon
        abonos = self.abonos.list_abono()
        table.setRowCount(0)
        for row_number, row_data in enumerate(abonos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscar_Abon(self,numab):
        table = self.ventana.table_mos_abon
        abonos = self.abonos.bus_abono(numab)
        if abonos:
            table.setRowCount(0)
            for row_number, row_data in enumerate(abonos):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            QMessageBox.information(None, 'Success', ' NO EXISTE')
 

    def delete_Abo(self):
        table = self.ventana.table_mos_abon
        if table.currentItem() != None:
            idemp = table.currentItem().text()
            empleado = self.abonos.bus_abono(idemp)
            if empleado:
                self.abonos.delete_abono(idemp)
        self.listabo()





