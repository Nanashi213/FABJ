from PyQt5 import QtCore, QtGui, QtWidgets
from CONTROLADORES.control_abon import AbonosController
import datetime
from MODELOS.abonos import Abonos

class Ui_abonos(object):

    def __init__(self) -> None:
        self.controlador = AbonosController(self)
        self.abon = Abonos()
    def setupUi(self, abonos):
        abonos.setObjectName("abonos")
        abonos.resize(671, 437)
        abonos.setStyleSheet("")
        self.Opciones = QtWidgets.QTabWidget(abonos)
        self.Opciones.setGeometry(QtCore.QRect(0, 0, 681, 451))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Opciones.setFont(font)
        self.Opciones.setStyleSheet("QStackedWidget{\n"
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
"#b_busca_mod{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
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
        self.Opciones.setObjectName("Opciones")
        self.OpcionesPage1_2 = QtWidgets.QWidget()
        self.OpcionesPage1_2.setObjectName("OpcionesPage1_2")
        self.table_mos_abon = QtWidgets.QTableWidget(self.OpcionesPage1_2)
        self.table_mos_abon.setGeometry(QtCore.QRect(10, 120, 521, 261))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_abon.setFont(font)
        self.table_mos_abon.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_abon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_abon.setAutoScroll(True)
        self.table_mos_abon.setObjectName("table_mos_abon")
        self.table_mos_abon.setColumnCount(5)
        self.table_mos_abon.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abon.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abon.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abon.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abon.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abon.setHorizontalHeaderItem(4, item)
        self.b_buscar = QtWidgets.QPushButton(self.OpcionesPage1_2)
        self.b_buscar.setGeometry(QtCore.QRect(190, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_buscar.setFont(font)
        self.b_buscar.setStyleSheet("")
        self.b_buscar.setObjectName("b_buscar")
        self.e_num_abo = QtWidgets.QLineEdit(self.OpcionesPage1_2)
        self.e_num_abo.setGeometry(QtCore.QRect(30, 70, 141, 41))
        self.e_num_abo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.e_num_abo.setText("")
        self.e_num_abo.setObjectName("e_num_abo")
        self.layoutWidget = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 120, 121, 151))
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
        self.b_eliminar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_eliminar.setFont(font)
        self.b_eliminar.setStyleSheet("")
        self.b_eliminar.setObjectName("b_eliminar")
        self.verticalLayout.addWidget(self.b_eliminar)
        self.T_abo = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.T_abo.setGeometry(QtCore.QRect(80, 20, 511, 41))
        self.T_abo.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_abo.setObjectName("T_abo")
        self.label_2 = QtWidgets.QLabel(self.T_abo)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Opciones.addTab(self.OpcionesPage1_2, "")
        self.OpcionesPage2_2 = QtWidgets.QWidget()
        self.OpcionesPage2_2.setObjectName("OpcionesPage2_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 160, 271, 154))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.t_referencia = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_referencia.setFont(font)
        self.t_referencia.setAlignment(QtCore.Qt.AlignCenter)
        self.t_referencia.setObjectName("t_referencia")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_referencia)
        self.cajarefe = QtWidgets.QComboBox(self.layoutWidget1)
        self.cajarefe.setObjectName("cajarefe")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cajarefe)
        self.t_fecha = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_fecha.setFont(font)
        self.t_fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.t_fecha.setObjectName("t_fecha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_fecha)
        self.fechaabo = QtWidgets.QDateEdit(self.layoutWidget1)
        self.fechaabo.setObjectName("fechaabo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fechaabo)
        self.t_telefono = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_telefono.setFont(font)
        self.t_telefono.setAlignment(QtCore.Qt.AlignCenter)
        self.t_telefono.setObjectName("t_telefono")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_telefono)
        self.e_abonado = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_abonado.setFont(font)
        self.e_abonado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_abonado.setObjectName("e_abonado")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.e_abonado)
        self.t_direccion = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_direccion.setFont(font)
        self.t_direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.t_direccion.setObjectName("t_direccion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.t_direccion)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.b_agregar = QtWidgets.QPushButton(self.layoutWidget1)
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
        self.verticalLayout_3.addWidget(self.b_agregar)
        self.T_abo_2 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_abo_2.setGeometry(QtCore.QRect(80, 30, 511, 41))
        self.T_abo_2.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_abo_2.setObjectName("T_abo_2")
        self.label_5 = QtWidgets.QLabel(self.T_abo_2)
        self.label_5.setGeometry(QtCore.QRect(180, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.T_emo_4 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_emo_4.setGeometry(QtCore.QRect(180, 100, 281, 41))
        self.T_emo_4.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_4.setObjectName("T_emo_4")
        self.label_6 = QtWidgets.QLabel(self.T_emo_4)
        self.label_6.setGeometry(QtCore.QRect(90, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.b_bus_clie = QtWidgets.QPushButton(self.OpcionesPage2_2)
        self.b_bus_clie.setGeometry(QtCore.QRect(470, 161, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_bus_clie.setFont(font)
        self.b_bus_clie.setStyleSheet("    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"")
        self.b_bus_clie.setText("")
        self.b_bus_clie.setObjectName("b_bus_clie")
        self.Opciones.addTab(self.OpcionesPage2_2, "")
        self.fechaabo.setDisplayFormat('yyyy-MM-dd')

        self.retranslateUi(abonos)
        self.Opciones.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(abonos)
         #----------------BOTONES--------------------------#
        self.mos = self.b_mostrar.clicked.connect(lambda:self.controlador.list_Abo())
        self.agre = self.b_agregar.clicked.connect(lambda:self.abon.insert_abonos(str(self.cajarefe.currentText()),self.fechaabo.text(),self.e_abonado.text()))   
        self.bus = self.b_buscar.clicked.connect(lambda:self.controlador.buscar_Abon(self.e_num_abo.text()))
        self.eliemp = self.b_eliminar.clicked.connect(lambda:self.controlador.delete_Abo())
        self.poncli = self.b_bus_clie.clicked.connect(lambda:self.ponclie(str(self.cajarefe.currentText())))

    def retranslateUi(self, abonos):
        _translate = QtCore.QCoreApplication.translate
        abonos.setWindowTitle(_translate("abonos", "Abonos"))
        item = self.table_mos_abon.horizontalHeaderItem(0)
        item.setText(_translate("abonos", "NUM_ABONO"))
        item = self.table_mos_abon.horizontalHeaderItem(1)
        item.setText(_translate("abonos", "REFERENCIA"))
        item = self.table_mos_abon.horizontalHeaderItem(2)
        item.setText(_translate("abonos", "FECHA"))
        item = self.table_mos_abon.horizontalHeaderItem(3)
        item.setText(_translate("abonos", "ABONADO"))
        item = self.table_mos_abon.horizontalHeaderItem(4)
        item.setText(_translate("abonos", "NOMBRE CLIENTE"))
        self.table_mos_abon.setColumnWidth(4,110)
        self.b_buscar.setText(_translate("abonos", "BUSCAR"))
        self.e_num_abo.setPlaceholderText(_translate("abonos", "NUM_ABONO"))
        self.b_mostrar.setText(_translate("abonos", "REFRESCAR"))
        self.b_eliminar.setText(_translate("abonos", "ELIMINAR"))
        self.label_2.setText(_translate("abonos", "ABONOS"))
        self.t_referencia.setText(_translate("abonos", "REFERENCIA*:"))
        self.t_fecha.setText(_translate("abonos", "FECHA*:"))
        self.t_telefono.setText(_translate("abonos", "ABONADO*:"))
        self.t_direccion.setText(_translate("abonos", "CLIENTE*:"))
        self.label.setText(_translate("abonos", "-------------------"))
        self.b_agregar.setText(_translate("abonos", "AGREGAR"))
        self.label_5.setText(_translate("abonos", "ABONOS"))
        self.label_6.setText(_translate("abonos", "AGREGAR"))
        #------------------Llenar cajas------------------------#
        ref = self.abon.obt_ref()
        x= 0
        for i in ref:
            self.cajarefe.addItem("")
            self.cajarefe.setItemText(x, _translate("UI_empleados",i[0]))
            x = x+1

    def ponclie(self,referencia):
        _translate = QtCore.QCoreApplication.translate
        a = self.abon.obt_idclie(referencia)
        self.label.setText(_translate("abonos",a))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_abonos()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())