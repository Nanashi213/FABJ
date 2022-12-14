import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from MODELOS.lotes import Lotes
from CONTROLADORES.control_lotes import LotesController

        


class Ui_lotes(object):
    def __init__(self) -> None:
        self.lotclie = Lotes()
        self.controlador = LotesController(self)

    def setupUi(self, lotes):
        lotes.setObjectName("lotes")
        lotes.resize(780, 456)
        lotes.setStyleSheet("")
        self.Opciones = QtWidgets.QTabWidget(lotes)
        self.Opciones.setGeometry(QtCore.QRect(0, 0, 781, 491))
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
        self.OpcionesPage2_2 = QtWidgets.QWidget()
        self.OpcionesPage2_2.setObjectName("OpcionesPage2_2")
        self.table_mos_lotes = QtWidgets.QTableWidget(self.OpcionesPage2_2)
        self.table_mos_lotes.setGeometry(QtCore.QRect(50, 90, 511, 261))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_lotes.setFont(font)
        self.table_mos_lotes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_lotes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_lotes.setAutoScroll(True)
        self.table_mos_lotes.setObjectName("table_mos_lotes")
        self.table_mos_lotes.setColumnCount(6)
        self.table_mos_lotes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_lotes.setHorizontalHeaderItem(5, item)
        self.T_emo = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_emo.setGeometry(QtCore.QRect(80, 20, 621, 41))
        self.T_emo.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo.setObjectName("T_emo")
        self.label_2 = QtWidgets.QLabel(self.T_emo)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.b_mostrar = QtWidgets.QPushButton(self.OpcionesPage2_2)
        self.b_mostrar.setGeometry(QtCore.QRect(50, 360, 119, 39))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_mostrar.setFont(font)
        self.b_mostrar.setStyleSheet("")
        self.b_mostrar.setObjectName("b_mostrar")
        self.b_actualizar = QtWidgets.QPushButton(self.OpcionesPage2_2)
        self.b_actualizar.setGeometry(QtCore.QRect(190, 360, 119, 39))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_actualizar.setFont(font)
        self.b_actualizar.setStyleSheet("")
        self.b_actualizar.setObjectName("b_actualizar")
        self.b_eliminar = QtWidgets.QPushButton(self.OpcionesPage2_2)
        self.b_eliminar.setGeometry(QtCore.QRect(330, 360, 119, 39))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_eliminar.setFont(font)
        self.b_eliminar.setStyleSheet("")
        self.b_eliminar.setObjectName("b_eliminar")
        self.layoutWidget_2 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(600, 160, 131, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.caja_cam_est = QtWidgets.QComboBox(self.layoutWidget_2)
        self.caja_cam_est.setObjectName("caja_cam_est")
        self.caja_cam_est.addItem("")
        self.caja_cam_est.addItem("")
        self.caja_cam_est.addItem("")
        self.verticalLayout_3.addWidget(self.caja_cam_est)
        self.b_cam_est = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_cam_est.setFont(font)
        self.b_cam_est.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_cam_est.setObjectName("b_cam_est")
        self.verticalLayout_3.addWidget(self.b_cam_est)
        self.layoutWidget_3 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(600, 260, 131, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.Caja_cambiar_cliente = QtWidgets.QComboBox(self.layoutWidget_3)
        self.Caja_cambiar_cliente.setObjectName("Caja_cambiar_cliente")
        self.verticalLayout_4.addWidget(self.Caja_cambiar_cliente)
        self.b_cam_clie = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_cam_clie.setFont(font)
        self.b_cam_clie.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_cam_clie.setObjectName("b_cam_clie")
        self.verticalLayout_4.addWidget(self.b_cam_clie)
        self.e_refe_cam = QtWidgets.QLineEdit(self.OpcionesPage2_2)
        self.e_refe_cam.setGeometry(QtCore.QRect(590, 110, 151, 40))
        self.e_refe_cam.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.e_refe_cam.setText("")
        self.e_refe_cam.setObjectName("e_refe_cam")
        self.Opciones.addTab(self.OpcionesPage2_2, "")
        self.OpcionesPage3 = QtWidgets.QWidget()
        self.OpcionesPage3.setObjectName("OpcionesPage3")
        self.T_agre_emp = QtWidgets.QWidget(self.OpcionesPage3)
        self.T_agre_emp.setGeometry(QtCore.QRect(220, 100, 321, 51))
        self.T_agre_emp.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_agre_emp.setObjectName("T_agre_emp")
        self.label = QtWidgets.QLabel(self.T_agre_emp)
        self.label.setGeometry(QtCore.QRect(50, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.OpcionesPage3)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 180, 291, 207))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.t_referencia = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_referencia.setFont(font)
        self.t_referencia.setAlignment(QtCore.Qt.AlignCenter)
        self.t_referencia.setObjectName("t_referencia")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_referencia)
        self.e_referencia = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_referencia.setFont(font)
        self.e_referencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_referencia.setText("")
        self.e_referencia.setFrame(True)
        self.e_referencia.setObjectName("e_referencia")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.e_referencia)
        self.t_cantidad = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_cantidad.setFont(font)
        self.t_cantidad.setAlignment(QtCore.Qt.AlignCenter)
        self.t_cantidad.setObjectName("t_cantidad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_cantidad)
        self.e_cantidad = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_cantidad.setFont(font)
        self.e_cantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_cantidad.setObjectName("e_cantidad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.e_cantidad)
        self.t_apellido = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_apellido.setFont(font)
        self.t_apellido.setAlignment(QtCore.Qt.AlignCenter)
        self.t_apellido.setObjectName("t_apellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_apellido)
        self.e_precio = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_precio.setFont(font)
        self.e_precio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_precio.setObjectName("e_precio")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.e_precio)
        self.t_direccion = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_direccion.setFont(font)
        self.t_direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.t_direccion.setObjectName("t_direccion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.t_direccion)
        self.t_cliente = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_cliente.setFont(font)
        self.t_cliente.setAlignment(QtCore.Qt.AlignCenter)
        self.t_cliente.setObjectName("t_cliente")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.t_cliente)
        self.caja_agre_est = QtWidgets.QComboBox(self.layoutWidget)
        self.caja_agre_est.setObjectName("caja_agre_est")
        self.caja_agre_est.addItem("")
        self.caja_agre_est.addItem("")
        self.caja_agre_est.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.caja_agre_est)
        self.caja_agre_clie = QtWidgets.QComboBox(self.layoutWidget)
        self.caja_agre_clie.setObjectName("caja_agre_clie")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.caja_agre_clie)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.b_agregar = QtWidgets.QPushButton(self.layoutWidget)
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
        self.verticalLayout_2.addWidget(self.b_agregar)
        self.T_emo_2 = QtWidgets.QWidget(self.OpcionesPage3)
        self.T_emo_2.setGeometry(QtCore.QRect(80, 20, 621, 41))
        self.T_emo_2.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_2.setObjectName("T_emo_2")
        self.label_3 = QtWidgets.QLabel(self.T_emo_2)
        self.label_3.setGeometry(QtCore.QRect(260, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Opciones.addTab(self.OpcionesPage3, "")
        self.OpcionesPage1_2 = QtWidgets.QWidget()
        self.OpcionesPage1_2.setObjectName("OpcionesPage1_2")
        self.table_mos_abonos = QtWidgets.QTableWidget(self.OpcionesPage1_2)
        self.table_mos_abonos.setGeometry(QtCore.QRect(40, 150, 701, 261))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_abonos.setFont(font)
        self.table_mos_abonos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_abonos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_abonos.setAutoScroll(True)
        self.table_mos_abonos.setObjectName("table_mos_abonos")
        self.table_mos_abonos.setColumnCount(7)
        self.table_mos_abonos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mos_abonos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_abonos.setHorizontalHeaderItem(6, item)
        self.T_emo_3 = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.T_emo_3.setGeometry(QtCore.QRect(80, 20, 621, 41))
        self.T_emo_3.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_3.setObjectName("T_emo_3")
        self.label_6 = QtWidgets.QLabel(self.T_emo_3)
        self.label_6.setGeometry(QtCore.QRect(260, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 100, 211, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.e_refe_bus = QtWidgets.QLineEdit(self.layoutWidget1)
        self.e_refe_bus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.e_refe_bus.setText("")
        self.e_refe_bus.setObjectName("e_refe_bus")
        self.horizontalLayout.addWidget(self.e_refe_bus)
        self.b_buscar = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_buscar.setFont(font)
        self.b_buscar.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"")
        self.b_buscar.setObjectName("b_buscar")
        self.horizontalLayout.addWidget(self.b_buscar)
        self.label_7 = QtWidgets.QLabel(self.OpcionesPage1_2)
        self.label_7.setGeometry(QtCore.QRect(400, 70, 139, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 12px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.layoutWidget_4 = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(370, 100, 231, 42))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.caja_bus_estad = QtWidgets.QComboBox(self.layoutWidget_4)
        self.caja_bus_estad.setObjectName("caja_bus_estad")
        self.caja_bus_estad.addItem("")
        self.caja_bus_estad.addItem("")
        self.caja_bus_estad.addItem("")
        self.horizontalLayout_2.addWidget(self.caja_bus_estad)
        self.b_bus_est = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_bus_est.setFont(font)
        self.b_bus_est.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"")
        self.b_bus_est.setObjectName("b_bus_est")
        self.horizontalLayout_2.addWidget(self.b_bus_est)
        self.Opciones.addTab(self.OpcionesPage1_2, "")

        self.retranslateUi(lotes)
        self.Opciones.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lotes)
        #----------------BOTONES--------------------------#
        self.mos = self.b_mostrar.clicked.connect(lambda:self.controlador.list_Lotes())
        self.agre = self.b_agregar.clicked.connect(lambda:self.controlador.insert_Lote(self.e_referencia.text().upper(),self.e_cantidad.text(),self.e_precio.text(),str(self.caja_agre_est.currentText()),str(self.caja_agre_clie.currentText())))   
        self.act = self.b_actualizar.clicked.connect(lambda:self.controlador.act_Lotes())
        self.bus = self.b_buscar.clicked.connect(lambda:self.controlador.bus_Lote(self.e_refe_bus.text()))
        self.bus_est = self.b_bus_est.clicked.connect(lambda:self.controlador.buscar_lote_estado(str(self.caja_bus_estad.currentText())))
        self.cam_es = self.b_cam_est.clicked.connect(lambda:self.controlador.act_Est_clie(1,self.e_refe_cam.text(),str(self.caja_cam_est.currentText()),int(self.Caja_cambiar_cliente.currentText())))
        self.cam_clie = self.b_cam_clie.clicked.connect(lambda:self.controlador.act_Est_clie(2,self.e_refe_cam.text(),str(self.caja_cam_est.currentText()),int(self.Caja_cambiar_cliente.currentText())))
        self.eliemp = self.b_eliminar.clicked.connect(lambda:self.controlador.delete_Lote())

    def retranslateUi(self, lotes):
        _translate = QtCore.QCoreApplication.translate
        lotes.setWindowTitle(_translate("lotes", "Lotes"))
        item = self.table_mos_lotes.horizontalHeaderItem(0)
        item.setText(_translate("lotes", "REFERENCIA"))
        item = self.table_mos_lotes.horizontalHeaderItem(1)
        item.setText(_translate("lotes", "CANTIDAD"))
        item = self.table_mos_lotes.horizontalHeaderItem(2)
        item.setText(_translate("lotes", "PRECIO_U"))
        item = self.table_mos_lotes.horizontalHeaderItem(3)
        item.setText(_translate("lotes", "ESTADO"))
        item = self.table_mos_lotes.horizontalHeaderItem(4)
        item.setText(_translate("lotes", "IDCLIENTE"))
        item = self.table_mos_lotes.horizontalHeaderItem(5)
        item.setText(_translate("lotes", "OBSERVACIONES"))
        self.table_mos_lotes.setColumnWidth(5,200)
        self.label_2.setText(_translate("lotes", "LOTES"))
        self.b_mostrar.setText(_translate("lotes", "REFRESCAR"))
        self.b_actualizar.setText(_translate("lotes", "ACTUALIZAR"))
        self.b_eliminar.setText(_translate("lotes", "ELIMINAR"))
        self.label_4.setText(_translate("lotes", "CAMBIAR ESTADO"))
        self.caja_cam_est.setItemText(0, _translate("lotes", "ESPERA"))
        self.caja_cam_est.setItemText(1, _translate("lotes", "EN PROCESO"))
        self.caja_cam_est.setItemText(2, _translate("lotes", "TERMINADO"))
        self.b_cam_est.setText(_translate("lotes", "CAMBIAR"))
        self.label_5.setText(_translate("lotes", "CAMBIAR CLIENTE"))
        self.b_cam_clie.setText(_translate("lotes", "CAMBIAR"))
        self.e_refe_cam.setPlaceholderText(_translate("lotes", "REFERENCIA"))
        self.label.setText(_translate("lotes", "AGREGAR LOTE"))
        self.t_referencia.setText(_translate("lotes", "REFERENCIA*:"))
        self.t_cantidad.setText(_translate("lotes", "CANTIDAD*:"))
        self.t_apellido.setText(_translate("lotes", "PRECIO_UNIDAD*:"))
        self.t_direccion.setText(_translate("lotes", "ESTADO*:"))
        self.t_cliente.setText(_translate("lotes", "CLIENTE*:"))
        self.caja_agre_est.setItemText(0, _translate("lotes", "ESPERA"))
        self.caja_agre_est.setItemText(1, _translate("lotes", "EN PROCESO"))
        self.caja_agre_est.setItemText(2, _translate("lotes", "TERMINADO"))
        self.b_agregar.setText(_translate("lotes", "AGREGAR"))
        self.label_3.setText(_translate("lotes", "LOTES"))
        item = self.table_mos_abonos.horizontalHeaderItem(0)
        item.setText(_translate("lotes", "REFERENCIA"))
        item = self.table_mos_abonos.horizontalHeaderItem(1)
        item.setText(_translate("lotes", "CANTIDAD"))
        item = self.table_mos_abonos.horizontalHeaderItem(2)
        item.setText(_translate("lotes", "PRECIO_U"))
        item = self.table_mos_abonos.horizontalHeaderItem(3)
        item.setText(_translate("lotes", "ESTADO"))
        item = self.table_mos_abonos.horizontalHeaderItem(4)
        item.setText(_translate("lotes", "IDCLIENTE"))
        item = self.table_mos_abonos.horizontalHeaderItem(5)
        item.setText(_translate("lotes", "TOTAL"))
        item = self.table_mos_abonos.horizontalHeaderItem(6)
        item.setText(_translate("lotes", "ABONADO"))
        self.label_6.setText(_translate("lotes", "LOTES"))
        self.e_refe_bus.setPlaceholderText(_translate("lotes", "REFERENCIA"))
        self.b_buscar.setText(_translate("lotes", "BUSCAR"))
        self.label_7.setText(_translate("lotes", "BUSCAR POR ESTADO"))
        self.caja_bus_estad.setItemText(0, _translate("lotes", "ESPERA"))
        self.caja_bus_estad.setItemText(1, _translate("lotes", "EN PROCESO"))
        self.caja_bus_estad.setItemText(2, _translate("lotes", "TERMINADO"))
        self.b_bus_est.setText(_translate("lotes", "BUSCAR"))
        #----------------Llenar cajas--------------------------#
        clie = self.lotclie.obt_clien()
        x= 0
        for i in clie:
            self.caja_agre_clie.addItem("")
            self.caja_agre_clie.setItemText(x, _translate("lotes",str(i[0])))
            self.Caja_cambiar_cliente.addItem("")
            self.Caja_cambiar_cliente.setItemText(x, _translate("lotes",str(i[0])))
            x = x+1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_lotes()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())

