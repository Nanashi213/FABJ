import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox

class Sueldo(conexion):

    def __init__(self):             
        with self.conn.cursor() as cursor:
            sql = """TRUNCATE sueldo"""
            cursor.execute(sql)
            self.conn.commit()

    def insert_sueldo(self,maquina):             
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO sueldo (sueldo.NOMBRE,sueldo.PRECIO) SELECT operaciones.NOMBRE,operaciones.PRECIO
FROM operaciones WHERE MAQUINA = %s"""
            cursor.execute(sql, maquina)
            self.conn.commit()
            
    def obt_sueldo(self):             
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM sueldo"""
            cursor.execute(sql)
            self.conn.commit()
            result = cursor.fetchall()
            return result

    def act_sueldo(self,cantidad,operacion):
        with self.conn.cursor() as cursor:
            sql = """UPDATE sueldo SET sueldo.CANTIDAD = %s WHERE NOMBRE = %s;"""
            cursor.execute(sql,(cantidad,operacion))
            self.conn.commit()
            return True

    def total_ope(self):
        with self.conn.cursor() as cursor:
            sql = """UPDATE sueldo SET sueldo.TOTAL=(sueldo.CANTIDAD*sueldo.PRECIO)"""
            cursor.execute(sql)
            self.conn.commit()
            return True

    def total_sueldo(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT SUM(TOTAL) FROM sueldo"""
            cursor.execute(sql)
            self.conn.commit()
            result = cursor.fetchall()
            return result[0][0]

    def reiniciar_sueldo(self):
        with self.conn.cursor() as cursor:
            sql = """TRUNCATE sueldo"""
            cursor.execute(sql)
            self.conn.commit()


    def obt_maq(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT MAQUINA FROM maquinas"""
            cursor.execute(sql)
            self.conn.commit()
            result = cursor.fetchall()
            return result

