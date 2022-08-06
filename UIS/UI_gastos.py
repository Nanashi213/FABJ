from PyQt5 import QtCore, QtGui, QtWidgets
from CONTROLADORES.control_gastos import GastController
import datetime


class Ui_Gastos(object):

    def __init__(self) -> None:
        self.controlador = GastController(self)
    def setupUi(self, Gastos):
        Gastos.setObjectName("Gastos")
        Gastos.resize(717, 425)
        Gastos.setStyleSheet("")
        self.OpcionesGas = QtWidgets.QTabWidget(Gastos)
        self.OpcionesGas.setGeometry(QtCore.QRect(0, 0, 721, 431))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.OpcionesGas.setFont(font)
        self.OpcionesGas.setStyleSheet("QStackedWidget{\n"
"background-color: rgb(227, 227, 227);}\n"
"\n"
"\n"
"#b_actualizar{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"#b_buscar{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"#b_mostrar{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"#b_eliminar{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}\n"
"")
        self.OpcionesGas.setObjectName("OpcionesGas")
        self.OpcionesGasPage1_2 = QtWidgets.QWidget()
        self.OpcionesGasPage1_2.setObjectName("OpcionesGasPage1_2")
        self.table_mos_gastos = QtWidgets.QTableWidget(self.OpcionesGasPage1_2)
        self.table_mos_gastos.setGeometry(QtCore.QRect(130, 90, 431, 261))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_gastos.setFont(font)
        self.table_mos_gastos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_gastos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_gastos.setAutoScroll(True)
        self.table_mos_gastos.setObjectName("table_mos_gastos")
        self.table_mos_gastos.setColumnCount(4)
        self.table_mos_gastos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_gastos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_gastos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_gastos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_gastos.setHorizontalHeaderItem(3, item)
        self.layoutWidget = QtWidgets.QWidget(self.OpcionesGasPage1_2)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 90, 121, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_mostrar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_mostrar.setFont(font)
        self.b_mostrar.setStyleSheet("")
        self.b_mostrar.setObjectName("b_mostrar")
        self.verticalLayout.addWidget(self.b_mostrar)
        self.b_actualizar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_actualizar.setFont(font)
        self.b_actualizar.setStyleSheet("")
        self.b_actualizar.setObjectName("b_actualizar")
        self.verticalLayout.addWidget(self.b_actualizar)
        self.b_eliminar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_eliminar.setFont(font)
        self.b_eliminar.setStyleSheet("")
        self.b_eliminar.setObjectName("b_eliminar")
        self.verticalLayout.addWidget(self.b_eliminar)
        self.T_gastos = QtWidgets.QWidget(self.OpcionesGasPage1_2)
        self.T_gastos.setGeometry(QtCore.QRect(50, 20, 611, 41))
        self.T_gastos.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_gastos.setObjectName("T_gastos")
        self.label_2 = QtWidgets.QLabel(self.T_gastos)
        self.label_2.setGeometry(QtCore.QRect(240, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.texTOTAL = QtWidgets.QLabel(self.OpcionesGasPage1_2)
        self.texTOTAL.setGeometry(QtCore.QRect(310, 360, 171, 21))
        self.texTOTAL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.texTOTAL.setText("")
        self.texTOTAL.setObjectName("texTOTAL")
        self.label_6 = QtWidgets.QLabel(self.OpcionesGasPage1_2)
        self.label_6.setGeometry(QtCore.QRect(200, 360, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.OpcionesGasPage1_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 111, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.Primefecha = QtWidgets.QDateEdit(self.layoutWidget1)
        self.Primefecha.setObjectName("Primefecha")
        self.verticalLayout_2.addWidget(self.Primefecha)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.Segfecha = QtWidgets.QDateEdit(self.layoutWidget1)
        self.Segfecha.setObjectName("Segfecha")
        self.verticalLayout_2.addWidget(self.Segfecha)
        self.b_buscar = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_buscar.setFont(font)
        self.b_buscar.setStyleSheet("")
        self.b_buscar.setObjectName("b_buscar")
        self.verticalLayout_2.addWidget(self.b_buscar)
        self.OpcionesGas.addTab(self.OpcionesGasPage1_2, "")
        self.OpcionesGasPage2_2 = QtWidgets.QWidget()
        self.OpcionesGasPage2_2.setObjectName("OpcionesGasPage2_2")
        self.T_agre_emp = QtWidgets.QWidget(self.OpcionesGasPage2_2)
        self.T_agre_emp.setGeometry(QtCore.QRect(180, 110, 341, 51))
        self.T_agre_emp.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_agre_emp.setObjectName("T_agre_emp")
        self.label = QtWidgets.QLabel(self.T_agre_emp)
        self.label.setGeometry(QtCore.QRect(60, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget2 = QtWidgets.QWidget(self.OpcionesGasPage2_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(210, 180, 296, 130))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.t_fecha = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_fecha.setFont(font)
        self.t_fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.t_fecha.setObjectName("t_fecha")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_fecha)
        self.fech_agre = QtWidgets.QDateEdit(self.layoutWidget2)
        self.fech_agre.setObjectName("fech_agre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fech_agre)
        self.t_descrip = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_descrip.setFont(font)
        self.t_descrip.setAlignment(QtCore.Qt.AlignCenter)
        self.t_descrip.setObjectName("t_descrip")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_descrip)
        self.e_descripcion = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.e_descripcion.setFont(font)
        self.e_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_descripcion.setText("")
        self.e_descripcion.setObjectName("e_descripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.e_descripcion)
        self.t_monto = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_monto.setFont(font)
        self.t_monto.setAlignment(QtCore.Qt.AlignCenter)
        self.t_monto.setObjectName("t_monto")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_monto)
        self.e_monto = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.e_monto.setFont(font)
        self.e_monto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_monto.setObjectName("e_monto")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.e_monto)
        self.b_agregar = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_agregar.setFont(font)
        self.b_agregar.setStyleSheet("    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"")
        self.b_agregar.setObjectName("b_agregar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.b_agregar)
        self.T_gastos_2 = QtWidgets.QWidget(self.OpcionesGasPage2_2)
        self.T_gastos_2.setGeometry(QtCore.QRect(60, 20, 611, 41))
        self.T_gastos_2.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_gastos_2.setObjectName("T_gastos_2")
        self.label_4 = QtWidgets.QLabel(self.T_gastos_2)
        self.label_4.setGeometry(QtCore.QRect(240, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.OpcionesGas.addTab(self.OpcionesGasPage2_2, "")
        self.fech_agre.setDisplayFormat('yyyy-MM-dd')
        self.Primefecha.setDisplayFormat('yyyy-MM-dd')
        self.Segfecha.setDisplayFormat('yyyy-MM-dd')

        self.retranslateUi(Gastos)
        self.OpcionesGas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gastos)

        #----------------BOTONES--------------------------#
        self.agre = self.b_agregar.clicked.connect(lambda:self.controlador.insert_Gastos(self.fech_agre.text(),self.e_descripcion.text().upper(),self.e_monto.text()))
        self.mos = self.b_mostrar.clicked.connect(lambda:self.controlador.list_Gastos())
        self.bus = self.b_buscar.clicked.connect(lambda:self.controlador.bus_Entrefec(self.Primefecha.text(),self.Segfecha.text()))
        self.act = self.b_actualizar.clicked.connect(lambda:self.controlador.act_Gasto())
        self.eli = self.b_eliminar.clicked.connect(lambda:self.controlador.delete_Gast())


    def retranslateUi(self, Gastos):
        _translate = QtCore.QCoreApplication.translate
        Gastos.setWindowTitle(_translate("Gastos", "Gastos"))
        item = self.table_mos_gastos.horizontalHeaderItem(0)
        item.setText(_translate("Gastos", "NUM"))
        item = self.table_mos_gastos.horizontalHeaderItem(1)
        item.setText(_translate("Gastos", "FECHA"))
        item = self.table_mos_gastos.horizontalHeaderItem(2)
        item.setText(_translate("Gastos", "DESCRIPCION"))
        item = self.table_mos_gastos.horizontalHeaderItem(3)
        item.setText(_translate("Gastos", "GASTO"))
        self.b_mostrar.setText(_translate("Gastos", "REFRESCAR"))
        self.b_actualizar.setText(_translate("Gastos", "ACTUALIZAR"))
        self.b_eliminar.setText(_translate("Gastos", "ELIMINAR"))
        self.label_2.setText(_translate("Gastos", "GASTOS"))
        self.label_6.setText(_translate("Gastos", "TOTAL"))
        self.label_3.setText(_translate("Gastos", "BUSCAR ENTRE"))
        self.label_5.setText(_translate("Gastos", "Y"))
        self.b_buscar.setText(_translate("Gastos", "BUSCAR"))
        self.label.setText(_translate("Gastos", "AGREGAR GASTO"))
        self.t_fecha.setText(_translate("Gastos", "FECHA: "))
        self.t_descrip.setText(_translate("Gastos", "DESCRIPCION:"))
        self.t_monto.setText(_translate("Gastos", "MONTO:"))
        self.b_agregar.setText(_translate("Gastos", "AGREGAR"))
        self.label_4.setText(_translate("Gastos", "GASTOS"))
        self.table_mos_gastos.setColumnWidth(0,10)
        self.table_mos_gastos.setColumnWidth(2,190)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_Gastos()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())


