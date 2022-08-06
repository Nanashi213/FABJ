import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox

class Abonos(conexion):

    def insert_abonos(self,referencia,fecha,abonado):
        if abonado=="":
            QMessageBox.information(None, 'Fail', 'Debe ingresar datos en los campos con *')
        else:
            if abonado.isdigit():       
                with self.conn.cursor() as cursor:
                    sql = """INSERT INTO abonos ( REFERENCIA, FECHA, ABONADO) VALUES  (%s,%s,%s)"""
                    cursor.execute(sql, (referencia.upper(),fecha,abonado))
                    self.conn.commit()
                    QMessageBox.information(None, 'Success', 'Abono Agregado')
            else:
                QMessageBox.information(None, 'Fail', 'Abonado debe ser positivo sin signos')





    def list_abono(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT abonos.NUM_AB, abonos.REFERENCIA,abonos.FECHA,abonos.ABONADO, clientes.NOMBRE FROM (lotes INNER JOIN clientes ON lotes.IDCLIENTE = clientes.IDCLIE)INNER JOIN abonos ON lotes.REFERENCIA = abonos.REFERENCIA;"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def bus_abono(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT  abonos.NUM_AB, abonos.REFERENCIA,abonos.FECHA,abonos.ABONADO, clientes.NOMBRE FROM (lotes INNER JOIN clientes ON lotes.IDCLIENTE = clientes.IDCLIE)INNER JOIN abonos ON lotes.REFERENCIA = abonos.REFERENCIA WHERE abonos.NUM_AB = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchall()
            print()
            if result:
                return result
      

    def delete_abono(self,idclie):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM abonos WHERE NUM_AB = %s"""
            cursor.execute(sql, idclie)
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Abono borrado')
    
    def obt_idclie(self,referencia):
        with self.conn.cursor() as cursor:
            sql = """SELECT clientes.NOMBRE FROM lotes INNER JOIN clientes ON lotes.IDCLIENTE = clientes.IDCLIE WHERE lotes.REFERENCIA= %s"""
            cursor.execute(sql,referencia)
            result = cursor.fetchall()
            return result[0][0]
    
    def obt_ref(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT REFERENCIA FROM lotes ORDER BY REFERENCIA"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


