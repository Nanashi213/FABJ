import sys
import os
from this import d
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox


class Gastos(conexion):

    def insert_gasto(self,fecha,descripcion,total):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO gastos (FECHA,DESCRIPCION,TOTAL) VALUES (%s,%s,%s)"""
            cursor.execute(sql, (fecha,descripcion,total))
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Gasto Agregado')


    def list_gastos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM gastos ORDER BY FECHA"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def bus_gas_fecha(self, fecha1, fecha2):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM gastos WHERE FECHA BETWEEN %s AND %s;"""
            cursor.execute(sql,(fecha1,fecha2))
            result = cursor.fetchall()
            if result:
                return result

    def bus_gas_num(self, num):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM gastos WHERE NUMG = %s;"""
            cursor.execute(sql,(num))
            result = cursor.fetchall()
            if result:
                return result
      
    def act_gasto(self,numg,fecha,descripcion,monto):
        with self.conn.cursor() as cursor:
            sql = """UPDATE gastos SET  FECHA = %s, DESCRIPCION= %s,TOTAL = %s WHERE NUMG = %s """
            cursor.execute(sql,(fecha,descripcion,monto,numg))
            self.conn.commit()
            

    def delete_gast(self,numg):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM gastos WHERE NUMG = %s"""
            cursor.execute(sql, numg)
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Gasto eliminado')

    def total_gas(self, fecha1, fecha2):
        with self.conn.cursor() as cursor:
            sql = """SELECT sum(TOTAL) FROM `gastos` WHERE FECHA BETWEEN %s AND %s"""
            cursor.execute(sql,(fecha1,fecha2))
            result = cursor.fetchall()
            if result:
                return result
            else:
                return 0



    

