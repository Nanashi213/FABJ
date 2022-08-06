from PyQt5 import QtCore, QtGui, QtWidgets
from CONTROLADORES.control_sueldo import SueldoController
import datetime

class Ui_sueldo(object):
    def __init__(self) -> None:
        self.controlador = SueldoController(self) 


    def setupUi(self, sueldo):
        sueldo.setObjectName("sueldo")
        sueldo.resize(821, 545)
        sueldo.setStyleSheet("")
        self.table_mos_sueldo = QtWidgets.QTableWidget(sueldo)
        self.table_mos_sueldo.setGeometry(QtCore.QRect(330, 100, 451, 411))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_sueldo.setFont(font)
        self.table_mos_sueldo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_sueldo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_sueldo.setAutoScroll(True)
        self.table_mos_sueldo.setObjectName("table_mos_sueldo")
        self.table_mos_sueldo.setColumnCount(4)
        self.table_mos_sueldo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_sueldo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_sueldo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_sueldo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_sueldo.setHorizontalHeaderItem(3, item)
        self.T_emo = QtWidgets.QWidget(sueldo)
        self.T_emo.setGeometry(QtCore.QRect(80, 20, 621, 41))
        self.T_emo.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo.setObjectName("T_emo")
        self.label_2 = QtWidgets.QLabel(self.T_emo)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(sueldo)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.b_actualizar = QtWidgets.QPushButton(sueldo)
        self.b_actualizar.setGeometry(QtCore.QRect(100, 220, 121, 39))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_actualizar.setFont(font)
        self.b_actualizar.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_actualizar.setObjectName("b_actualizar")
        self.b_total = QtWidgets.QPushButton(sueldo)
        self.b_total.setGeometry(QtCore.QRect(100, 300, 121, 39))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_total.setFont(font)
        self.b_total.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_total.setObjectName("b_total")
        self.Texto_total = QtWidgets.QLabel(sueldo)
        self.Texto_total.setGeometry(QtCore.QRect(120, 360, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Texto_total.setFont(font)
        self.Texto_total.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.Texto_total.setAlignment(QtCore.Qt.AlignCenter)
        self.Texto_total.setObjectName("Texto_total")
        self.b_reinicia = QtWidgets.QPushButton(sueldo)
        self.b_reinicia.setGeometry(QtCore.QRect(90, 410, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.b_reinicia.setFont(font)
        self.b_reinicia.setStyleSheet("background-color: rgb(255, 26, 87);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_reinicia.setObjectName("b_reinicia")
        self.label_9 = QtWidgets.QLabel(sueldo)
        self.label_9.setGeometry(QtCore.QRect(30, 270, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(sueldo)
        self.label_10.setGeometry(QtCore.QRect(20, 190, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(sueldo)
        self.label_11.setGeometry(QtCore.QRect(30, 100, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.widget = QtWidgets.QWidget(sueldo)
        self.widget.setGeometry(QtCore.QRect(30, 130, 261, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.caja_maquina = QtWidgets.QComboBox(self.widget)
        self.caja_maquina.setObjectName("caja_maquina")
        self.horizontalLayout.addWidget(self.caja_maquina)
        self.b_elegir_maq = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_elegir_maq.setFont(font)
        self.b_elegir_maq.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_elegir_maq.setObjectName("b_elegir_maq")
        self.horizontalLayout.addWidget(self.b_elegir_maq)

        self.retranslateUi(sueldo)
        QtCore.QMetaObject.connectSlotsByName(sueldo)
        self.ele = self.b_elegir_maq.clicked.connect(lambda:self.controlador.elegir_maquina(self.caja_maquina.currentText()))
        self.act = self.b_actualizar.clicked.connect(lambda:self.controlador.updateCant())
        self.total = self.b_total.clicked.connect(lambda:self.controlador.total())
        self.reinicia = self.b_reinicia.clicked.connect(lambda:self.controlador.reinicia())


    def retranslateUi(self, sueldo):
        _translate = QtCore.QCoreApplication.translate
        sueldo.setWindowTitle(_translate("sueldo", "Sueldo"))
        item = self.table_mos_sueldo.horizontalHeaderItem(0)
        item.setText(_translate("sueldo", "NOMBRE OPERACION"))
        item = self.table_mos_sueldo.horizontalHeaderItem(1)
        item.setText(_translate("sueldo", "PRECIO_U"))
        item = self.table_mos_sueldo.horizontalHeaderItem(2)
        item.setText(_translate("sueldo", "CANTIDAD"))
        item = self.table_mos_sueldo.horizontalHeaderItem(3)
        item.setText(_translate("sueldo", "TOTAL OPE"))
        self.label_2.setText(_translate("sueldo", "CALCULAR SUELDO"))
        self.label_7.setText(_translate("sueldo", "TOTAL:"))
        self.b_actualizar.setText(_translate("sueldo", "ACTUALIZAR"))
        self.b_total.setText(_translate("sueldo", "TOTAL"))
        self.Texto_total.setText(_translate("sueldo", "------------"))
        self.b_reinicia.setText(_translate("sueldo", "REINICIAR"))
        self.label_9.setText(_translate("sueldo", "CALCULAR TOTAL DE OPERACIONES"))
        self.label_10.setText(_translate("sueldo", "GUARDA CANTIDAD Y CALCULA TOTAL OPERACION"))
        self.label_11.setText(_translate("sueldo", "PONER OPERACIONES POR MAQUINA"))
        self.b_elegir_maq.setText(_translate("sueldo", "ELEGIR MAQUINA"))
        self.table_mos_sueldo.setColumnWidth(0,150)
        self.caja_maquina.addItem("")
        self.caja_maquina.setItemText(0, _translate("sueldo","NINGUNA"))

        maq = self.controlador.maquinas()
        x= 1
        for i in maq:
            self.caja_maquina.addItem("")
            self.caja_maquina.setItemText(x, _translate("sueldo",i[0]))
            x = x+1




#PyInstaller --windowed --onefile --icon=./calcu.ico CALCULADORA_SUELDO.py