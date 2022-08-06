import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from CONEXION_BD.Connection import conexion
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime

class Eliminados(conexion):

    def insert_eliminados(self,tabla,contenido):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO eliminados (TABLA,CONTENIDO,FECHA) VALUES (%s,%s,%s)"""
            cursor.execute(sql, (tabla,contenido,datetime.today().strftime('%Y-%m-%d')))
            self.conn.commit()






