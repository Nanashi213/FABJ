import sys
import os
from weakref import ref
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox

class Lotes(conexion):

    def insert_lote(self,referencia,cantidad,precio_u,estado,idcliente):             
        if self.rev_ref(referencia):
            QMessageBox.information(None, 'Fail', 'Referencia ya registrada')
        else:
            with self.conn.cursor() as cursor:
                sql = """INSERT INTO lotes (REFERENCIA,CANTIDAD,PRECIO_U,ESTADO,IDCLIENTE) VALUES (%s,%s,%s,%s,%s)"""
                cursor.execute(sql, (referencia.upper(),cantidad,precio_u,estado,idcliente))
                self.conn.commit()
                QMessageBox.information(None, 'Success', 'Lote Agregado')


    def list_lotes(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM lotes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def bus_lote(self, referencia):
        with self.conn.cursor() as cursor:
            sql = """SELECT  lotes.REFERENCIA,CANTIDAD,PRECIO_U,ESTADO,IDCLIENTE,CANTIDAD*PRECIO_U,SUM(abonos.ABONADO) FROM lotes LEFT JOIN abonos ON lotes.REFERENCIA = abonos.REFERENCIA GROUP BY (lotes.REFERENCIA) HAVING REFERENCIA = %s;"""
            cursor.execute(sql,referencia)
            result = cursor.fetchall()
            if result:
                return result

    def bus_lotes_est(self, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT  lotes.REFERENCIA,CANTIDAD,PRECIO_U,ESTADO,IDCLIENTE,CANTIDAD*PRECIO_U,SUM(abonos.ABONADO) FROM lotes LEFT JOIN abonos ON lotes.REFERENCIA = abonos.REFERENCIA GROUP BY (lotes.REFERENCIA) HAVING ESTADO = %s"""
            cursor.execute(sql,estado)
            result = cursor.fetchall()
            if result:
                return result

    def bus_lote_cam(self, referencia):
        with self.conn.cursor() as cursor:
            sql = """
            SELECT * FROM lotes WHERE REFERENCIA = %s"""
            cursor.execute(sql,referencia)
            result = cursor.fetchall()
            if result:
                return result

    def act_lote(self,referencia,cantidad,precio_u,observacion):
        with self.conn.cursor() as cursor:
            sql = """UPDATE lotes SET  CANTIDAD = %s,PRECIO_U = %s, OBSERVACION = %s WHERE REFERENCIA = %s """
            cursor.execute(sql,(cantidad,precio_u,observacion,referencia))
            self.conn.commit()
            return True

    def act_est_clie(self,opcion,referencia,estado,idcliente):  
        if opcion == 1:    
            with self.conn.cursor() as cursor:
                sql = """UPDATE lotes SET  ESTADO = %s WHERE REFERENCIA = %s """
                cursor.execute(sql,(estado,referencia))
                self.conn.commit()
                return True
        else: 
            with self.conn.cursor() as cursor:
                sql = """UPDATE lotes SET IDCLIENTE = %s WHERE REFERENCIA = %s"""
                cursor.execute(sql,(idcliente,referencia))
                self.conn.commit()
                return True

    def delete_lote(self,referencia):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM lotes WHERE REFERENCIA = %s"""
            cursor.execute(sql, referencia)
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Lote borrado')

    def rev_ref(self,referencia):
        with self.conn.cursor() as cursor:
            sql = """SELECT REFERENCIA FROM lotes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            lista = []
            for i in result:
                lista.append(i[0])
            if referencia in lista:
                return True
    
    def obt_clien(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT IDCLIE FROM clientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
