import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox

class Clientes(conexion):

    def insert_clie(self,idclie,nombre,direccion,tipo,contacto):             
        if self.rev_cod(idclie):
            QMessageBox.information(None, 'ERROR', 'YA EXISTE ESTE CLIENTE')
        else:
            if  direccion == "":
                with self.conn.cursor() as cursor:
                    sql = """INSERT INTO clientes (`IDCLIE`, `NOMBRE`, `TIPO`, `CONTACTO`) VALUES (%s,%s,%s,%s)"""
                    cursor.execute(sql, (idclie,nombre.upper(),tipo,contacto))
                    self.conn.commit()
                    QMessageBox.information(None, 'Success', 'Cliente Agregado')
            else:
                with self.conn.cursor() as cursor:
                    sql = """INSERT INTO clientes (IDCLIE,NOMBRE,TIPO,DIRECCION,CONTACTO) VALUES (%s,%s,%s,%s,%s)"""
                    cursor.execute(sql, (idclie,nombre.upper(),direccion,tipo,contacto))
                    self.conn.commit()
                    QMessageBox.information(None, 'Success', 'Cliente Agregado')


    def list_clie(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM clientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def bus_clie(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM clientes WHERE IDCLIE = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchall()
            print()
            if result:
                return result
      
    def act_clie(self,idclie,nombre,tipo,direccion,contacto):
        if tipo == "EMPRESA" or tipo == "INDIVIDUO":
            with self.conn.cursor() as cursor:
                sql = """UPDATE clientes SET  NOMBRE = %s, TIPO = %s,DIRECCION = %s, CONTACTO = %s WHERE IDCLIE = %s """
                cursor.execute(sql,(nombre.upper(),tipo,direccion,contacto,idclie))
                self.conn.commit()
                return True
        else :
            QMessageBox.information(None, 'Fail', 'TIPO NO PERMITIDO')


    def delete_clie(self,idclie):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM clientes WHERE IDCLIE = %s"""
            cursor.execute(sql, idclie)
            self.conn.commit()
            QMessageBox.information(None, 'Success', 'Cliente borrado')
    
    def rev_cod(self,idemp):
        with self.conn.cursor() as cursor:
            sql = """SELECT IDCLIE FROM clientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            lista = []
            for i in result:
                lista.append(i[0])
            if idemp in lista:
                return True

    def clie_total(self, idclie):
        with self.conn.cursor() as cursor:
            sql = """SELECT SUM(lotes.PRECIO_U*lotes.CANTIDAD) FROM `lotes` GROUP BY IDCLIENTE HAVING IDCLIENTE = %s"""
            cursor.execute(sql,idclie)
            result = cursor.fetchall()
            print()
            if result:
                return result[0][0]

    def clie_abo(self, idclie):
        with self.conn.cursor() as cursor:
            sql = """SELECT clientes.IDCLIE, clientes.NOMBRE,clientes.TIPO ,SUM(abonos.ABONADO) FROM (lotes INNER JOIN clientes ON lotes.IDCLIENTE = clientes.IDCLIE)LEFT  JOIN abonos ON lotes.REFERENCIA = abonos.REFERENCIA WHERE clientes.IDCLIE=%s"""
            cursor.execute(sql,(idclie))
            result = cursor.fetchall()
            if result:
                return result[0]







