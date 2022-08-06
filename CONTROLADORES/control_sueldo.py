import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.sueldo import Sueldo

class SueldoController():

    def __init__(self, ventana):
        self.sueldo= Sueldo()
        self.ventana= ventana
    
    def lista(self):
        table = self.ventana.table_mos_sueldo
        operaciones = self.sueldo.obt_sueldo()
        table.setRowCount(0)
        for row_number, row_data in enumerate(operaciones):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def elegir_maquina(self,maquina):
        self.sueldo.insert_sueldo(maquina)
        self.lista()

    def updateCant(self):
        table = self.ventana.table_mos_sueldo
        operaciones = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                operaciones.append(fila)
            fila = []
        if len(operaciones)>0:
            for ope in operaciones:
                ope[2]=int(ope[2])
                if isinstance(ope[2], int):
                    x = self.sueldo.act_sueldo(ope[2],ope[0])
            if x:
                self.sueldo.total_ope()
                self.lista()
                QMessageBox.information(None, 'Success', 'Cantidad Guardada')

 

    def reinicia(self):
        self.sueldo.reiniciar_sueldo()
        self.lista()
        _translate = QtCore.QCoreApplication.translate
        self.ventana.Texto_total.setText(_translate("sueldo", "------------"))


    def total(self):
        total = self.sueldo.total_sueldo()
        _translate = QtCore.QCoreApplication.translate
        self.ventana.Texto_total.setText(_translate("sueldo",str(total)))


    def maquinas(self):
        maquinas = self.sueldo.obt_maq()
        return maquinas





