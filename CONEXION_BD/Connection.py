import pymysql

class conexion():
    conn = pymysql.connect(
        host="localhost", port=3306, user="fabj",
        password="gU36r*n]FYDtM&D", db="fabj"
    )