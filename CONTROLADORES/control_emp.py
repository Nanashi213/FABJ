import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MODELOS.empleados import Empleados
from MODELOS.eliminados import Eliminados

class EmpController():

    def __init__(self, ventana):
        self.empleados = Empleados()
        self.elim = Eliminados()
        self.ventana= ventana
    
    def list_Emp(self):
        table = self.ventana.table_mos_empleado
        empleados = self.empleados.list_empl()
        table.setRowCount(0)
        for row_number, row_data in enumerate(empleados):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def act_Emp(self):
        table = self.ventana.table_mos_empleado
        emples = []
        fila = []
        x=0
        y=0
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                emples.append(fila)
            fila = []
        if len(emples)>0:
            for emp in emples:
                if emp[1]!="" and emp[2]!="" and emp[4].isdigit():
                    self.empleados.act_emple(int(emp[0]),emp[1],emp[2],emp[3],emp[4])
                    x=1
                else:
                    y=1
            
            if x==1 and y==0:
                QMessageBox.information(None, 'Success', 'Empleado actualizado')
            else:
                QMessageBox.information(None, 'Fail', 'Datos no validos')

    def bus_Emp(self,idemp):
        table = self.ventana.table_mos_empleado
        emplead = self.empleados.bus_emple(idemp)
        if emplead:
            table.setRowCount(1)
            tablerow = 0
            row = emplead
            table.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            table.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            table.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            table.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            table.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            table.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[5])))
        else:
            QMessageBox.information(None, 'Fail', 'ID no encontrado')
 
    def bus_emp_maq(self,idemp):
        if idemp.isdigit():
            emplead = self.empleados.bus_emple(idemp)
            if emplead:
                _translate = QtCore.QCoreApplication.translate
                nombre = self.ventana.text_mos_nom
                apellido = self.ventana.texto_mos_ape
                nombre.setText(_translate("UI_empleados",emplead[1]))
                apellido.setText(_translate("UI_empleados",emplead[2]))
            else:
                QMessageBox.information(None, 'Fail', 'ID no encontrado')

        else:
            QMessageBox.information(None, 'Fail', 'Datos no validos')

    def delete_Emp(self):
        table = self.ventana.table_mos_empleado
        if table.currentItem() != None:
            idemp = table.currentItem().text()
            empleado = self.empleados.bus_emple(idemp)
            if empleado:
                self.elim.insert_eliminados("empleados",str(empleado))
                self.empleados.delete_empl(idemp)
        self.list_Emp()





