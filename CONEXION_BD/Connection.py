import pymysql

class conexion():
    conn = pymysql.connect(
        host="localhost", port=3306, user="root",
        password="", db="fabj"
    )