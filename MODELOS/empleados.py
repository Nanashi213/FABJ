import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox

class Empleados(conexion):

    def insert_empl(self,idemp,nombre,apellido,direccion,telefono,maquina):
        if nombre!="" and apellido!="" and idemp!="" and telefono!="" :
            if idemp.isdigit() and idemp.isdigit():
                if self.rev_cod(idemp):
                    QMessageBox.information(None, 'Fail', 'El ID ya esta registrado')
                else:
                    if  direccion == "":
                        with self.conn.cursor() as cursor:
                            sql = """INSERT INTO empleados (IDEMP,NOMBRE,APELLIDO,TELEFONO,MAQUINA) VALUES (%s,%s,%s,%s,%s)"""
                            cursor.execute(sql, (idemp,nombre.upper(),apellido.upper(),telefono,maquina))
                            self.conn.commit()
                            QMessageBox.information(None, 'Success', 'Empleado Agregado')
                    else:
                        with self.conn.cursor() as cursor:
                            sql = """INSERT INTO empleados (IDEMP,NOMBRE,APELLIDO,DIRECCION,TELEFONO,MAQUINA) VALUES (%s,%s,%s,%s,%s,%s)"""
                            cursor.execute(sql, (idemp,nombre.upper(),apellido.upper(),direccion,telefono,maquina))
                            self.conn.commit()
                            QMessageBox.information(None, 'Success', 'Empleado Agregado')
            else:
                QMessageBox.information(None, 'Fail', 'ID y Telefono deben ser numeros')
        else:
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')


    def list_empl(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM empleados"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def bus_emple(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM empleados WHERE IDEMP = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchone()
            print()
            if result:
                return result

    def cam_maq(self,idemp,maquina):
        with self.conn.cursor() as cursor:
            sql = """UPDATE empleados SET   MAQUINA = %s WHERE IDEMP = %s """
            cursor.execute(sql,(maquina,idemp))
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Maquina cambiada')
      
    def act_emple(self,idemp,nombre,apellido,direccion,telefono):
        with self.conn.cursor() as cursor:
            sql = """UPDATE empleados SET  NOMBRE = %s, APELLIDO = %s,DIRECCION = %s, TELEFONO = %s WHERE IDEMP = %s """
            cursor.execute(sql,(nombre.upper(),apellido.upper(),direccion,telefono,idemp))
            self.conn.commit()
            

    def delete_empl(self,idemp):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM empleados WHERE IDEMP = %s"""
            cursor.execute(sql, idemp)
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Empleado borrado')
    
    def obt_maq(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT MAQUINA FROM maquinas"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def rev_cod(self,idemp):
        with self.conn.cursor() as cursor:
            sql = """SELECT IDEMP FROM empleados"""
            cursor.execute(sql)
            result = cursor.fetchall()
            lista = []
            for i in result:
                lista.append(i[0])
            if idemp in lista:
                return True

    def insert_maq(self,nombre):
        if nombre != "":
            with self.conn.cursor() as cursor:
                sql = """INSERT INTO maquinas (MAQUINA) VALUES (%s)"""
                cursor.execute(sql, (nombre.upper()))
                self.conn.commit()
                QMessageBox.information(None, 'Success', 'Maquina Agregada')
        else:
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')

    def insert_ope(self,nombre,precio,maquina):
        if nombre != "" and precio!="":
            if precio.isdigit():
                if isinstance(precio, int): 
                    with self.conn.cursor() as cursor:
                        sql = """INSERT INTO operaciones (NOMBRE,PRECIO,MAQUINA) VALUES (%s,%s,%s)"""
                        cursor.execute(sql, (nombre.upper(),precio,maquina))
                        self.conn.commit()
                        QMessageBox.information(None, 'Success', 'Operacion Agregada')
            else:
                QMessageBox.information(None, 'Fail', 'Precio debe ser numero positivo sin signos')
        else:
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')


 