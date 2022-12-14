import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from MODELOS.empleados import Empleados
from CONTROLADORES.control_emp import EmpController


class Ui_UI_empleados(object):
    def __init__(self) -> None:
        self.emp = Empleados()
        self.controlador = EmpController(self)

    def setupUi(self, UI_empleados):
        UI_empleados.setObjectName("UI_empleados")
        UI_empleados.resize(781, 443)
        UI_empleados.setStyleSheet("")
        self.Opciones = QtWidgets.QTabWidget(UI_empleados)
        self.Opciones.setGeometry(QtCore.QRect(0, 0, 781, 581))
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
"#b_actualizar{\n"
"background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;\n"
"}")
        self.Opciones.setObjectName("Opciones")
        self.OpcionesPage1_2 = QtWidgets.QWidget()
        self.OpcionesPage1_2.setObjectName("OpcionesPage1_2")
        self.table_mos_empleado = QtWidgets.QTableWidget(self.OpcionesPage1_2)
        self.table_mos_empleado.setGeometry(QtCore.QRect(10, 120, 611, 261))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_mos_empleado.setFont(font)
        self.table_mos_empleado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_mos_empleado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mos_empleado.setAutoScroll(True)
        self.table_mos_empleado.setObjectName("table_mos_empleado")
        self.table_mos_empleado.setColumnCount(6)
        self.table_mos_empleado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_mos_empleado.setHorizontalHeaderItem(5, item)
        self.b_buscar = QtWidgets.QPushButton(self.OpcionesPage1_2)
        self.b_buscar.setGeometry(QtCore.QRect(190, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_buscar.setFont(font)
        self.b_buscar.setStyleSheet("")
        self.b_buscar.setObjectName("b_buscar")
        self.e_codi = QtWidgets.QLineEdit(self.OpcionesPage1_2)
        self.e_codi.setGeometry(QtCore.QRect(30, 70, 141, 41))
        self.e_codi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.e_codi.setText("")
        self.e_codi.setObjectName("e_codi")
        self.layoutWidget = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 120, 121, 131))
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
        self.T_emo_3 = QtWidgets.QWidget(self.OpcionesPage1_2)
        self.T_emo_3.setGeometry(QtCore.QRect(80, 10, 601, 41))
        self.T_emo_3.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_3.setObjectName("T_emo_3")
        self.label_4 = QtWidgets.QLabel(self.T_emo_3)
        self.label_4.setGeometry(QtCore.QRect(220, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Opciones.addTab(self.OpcionesPage1_2, "")
        self.OpcionesPage2_2 = QtWidgets.QWidget()
        self.OpcionesPage2_2.setObjectName("OpcionesPage2_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 150, 315, 222))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.t_idemple = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_idemple.setFont(font)
        self.t_idemple.setAlignment(QtCore.Qt.AlignCenter)
        self.t_idemple.setObjectName("t_idemple")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_idemple)
        self.e_idemple = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_idemple.setFont(font)
        self.e_idemple.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_idemple.setText("")
        self.e_idemple.setFrame(True)
        self.e_idemple.setObjectName("e_idemple")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.e_idemple)
        self.t_nombre = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre.setFont(font)
        self.t_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre.setObjectName("t_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_nombre)
        self.e_nombre = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_nombre.setFont(font)
        self.e_nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_nombre.setObjectName("e_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.e_nombre)
        self.t_apellido = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_apellido.setFont(font)
        self.t_apellido.setAlignment(QtCore.Qt.AlignCenter)
        self.t_apellido.setObjectName("t_apellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_apellido)
        self.e_apellido = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_apellido.setFont(font)
        self.e_apellido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_apellido.setObjectName("e_apellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.e_apellido)
        self.t_direccion = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_direccion.setFont(font)
        self.t_direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.t_direccion.setObjectName("t_direccion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.t_direccion)
        self.e_direccion = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_direccion.setFont(font)
        self.e_direccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_direccion.setObjectName("e_direccion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.e_direccion)
        self.t_telefono = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_telefono.setFont(font)
        self.t_telefono.setAlignment(QtCore.Qt.AlignCenter)
        self.t_telefono.setObjectName("t_telefono")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.t_telefono)
        self.e_telefono = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.e_telefono.setFont(font)
        self.e_telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_telefono.setObjectName("e_telefono")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.e_telefono)
        self.t_telefono_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_telefono_2.setFont(font)
        self.t_telefono_2.setAlignment(QtCore.Qt.AlignCenter)
        self.t_telefono_2.setObjectName("t_telefono_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.t_telefono_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout_2.addLayout(self.formLayout)
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
        self.verticalLayout_2.addWidget(self.b_agregar)
        self.T_emo_2 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_emo_2.setGeometry(QtCore.QRect(90, 20, 601, 41))
        self.T_emo_2.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_2.setObjectName("T_emo_2")
        self.label_3 = QtWidgets.QLabel(self.T_emo_2)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.T_emo_4 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_emo_4.setGeometry(QtCore.QRect(40, 80, 271, 41))
        self.T_emo_4.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_4.setObjectName("T_emo_4")
        self.label_5 = QtWidgets.QLabel(self.T_emo_4)
        self.label_5.setGeometry(QtCore.QRect(70, 0, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(450, 220, 291, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.t_nombre_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre_3.setFont(font)
        self.t_nombre_3.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre_3.setObjectName("t_nombre_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_nombre_3)
        self.text_mos_nom = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.text_mos_nom.setFont(font)
        self.text_mos_nom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_mos_nom.setObjectName("text_mos_nom")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.text_mos_nom)
        self.t_maq = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_maq.setFont(font)
        self.t_maq.setAlignment(QtCore.Qt.AlignCenter)
        self.t_maq.setObjectName("t_maq")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_maq)
        self.caja_cam_ma = QtWidgets.QComboBox(self.layoutWidget_2)
        self.caja_cam_ma.setObjectName("caja_cam_ma")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.caja_cam_ma)
        self.t_apellido_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_apellido_3.setFont(font)
        self.t_apellido_3.setAlignment(QtCore.Qt.AlignCenter)
        self.t_apellido_3.setObjectName("t_apellido_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_apellido_3)
        self.texto_mos_ape = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.texto_mos_ape.setFont(font)
        self.texto_mos_ape.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.texto_mos_ape.setObjectName("texto_mos_ape")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.texto_mos_ape)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.b_cambiarmaq = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_cambiarmaq.setFont(font)
        self.b_cambiarmaq.setStyleSheet("    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"")
        self.b_cambiarmaq.setObjectName("b_cambiarmaq")
        self.verticalLayout_3.addWidget(self.b_cambiarmaq)
        self.T_emo_6 = QtWidgets.QWidget(self.OpcionesPage2_2)
        self.T_emo_6.setGeometry(QtCore.QRect(440, 80, 311, 41))
        self.T_emo_6.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_6.setObjectName("T_emo_6")
        self.label_7 = QtWidgets.QLabel(self.T_emo_6)
        self.label_7.setGeometry(QtCore.QRect(20, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.b_buscar_cam_maq = QtWidgets.QPushButton(self.OpcionesPage2_2)
        self.b_buscar_cam_maq.setGeometry(QtCore.QRect(620, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.b_buscar_cam_maq.setFont(font)
        self.b_buscar_cam_maq.setStyleSheet("background-color: rgb(93, 179, 255);\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.b_buscar_cam_maq.setObjectName("b_buscar_cam_maq")
        self.e_codi_cam_maq = QtWidgets.QLineEdit(self.OpcionesPage2_2)
        self.e_codi_cam_maq.setGeometry(QtCore.QRect(450, 150, 141, 41))
        self.e_codi_cam_maq.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"padding: 10px;\n"
"border-radius: 12px;")
        self.e_codi_cam_maq.setText("")
        self.e_codi_cam_maq.setObjectName("e_codi_cam_maq")
        self.Opciones.addTab(self.OpcionesPage2_2, "")
        self.OpcionesPage3 = QtWidgets.QWidget()
        self.OpcionesPage3.setObjectName("OpcionesPage3")
        self.T_emo_7 = QtWidgets.QWidget(self.OpcionesPage3)
        self.T_emo_7.setGeometry(QtCore.QRect(30, 110, 311, 41))
        self.T_emo_7.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_7.setObjectName("T_emo_7")
        self.label_9 = QtWidgets.QLabel(self.T_emo_7)
        self.label_9.setGeometry(QtCore.QRect(20, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.T_emo_5 = QtWidgets.QWidget(self.OpcionesPage3)
        self.T_emo_5.setGeometry(QtCore.QRect(410, 110, 331, 41))
        self.T_emo_5.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_5.setObjectName("T_emo_5")
        self.label_10 = QtWidgets.QLabel(self.T_emo_5)
        self.label_10.setGeometry(QtCore.QRect(30, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.T_emo_8 = QtWidgets.QWidget(self.OpcionesPage3)
        self.T_emo_8.setGeometry(QtCore.QRect(90, 20, 601, 41))
        self.T_emo_8.setStyleSheet("background-color: rgb(85, 79, 255);\n"
"border-radius: 20px;")
        self.T_emo_8.setObjectName("T_emo_8")
        self.label_11 = QtWidgets.QLabel(self.T_emo_8)
        self.label_11.setGeometry(QtCore.QRect(220, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.layoutWidget2 = QtWidgets.QWidget(self.OpcionesPage3)
        self.layoutWidget2.setGeometry(QtCore.QRect(450, 190, 261, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.t_nombre_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre_5.setFont(font)
        self.t_nombre_5.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre_5.setObjectName("t_nombre_5")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_nombre_5)
        self.e_nom_ope = QtWidgets.QLineEdit(self.layoutWidget2)
        self.e_nom_ope.setObjectName("e_nom_ope")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.e_nom_ope)
        self.t_nombre_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre_6.setFont(font)
        self.t_nombre_6.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre_6.setObjectName("t_nombre_6")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_nombre_6)
        self.e_pre_ope = QtWidgets.QLineEdit(self.layoutWidget2)
        self.e_pre_ope.setObjectName("e_pre_ope")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.e_pre_ope)
        self.t_nombre_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre_7.setFont(font)
        self.t_nombre_7.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre_7.setObjectName("t_nombre_7")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_nombre_7)
        self.caja_maq_ope = QtWidgets.QComboBox(self.layoutWidget2)
        self.caja_maq_ope.setObjectName("caja_maq_ope")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.caja_maq_ope)
        self.verticalLayout_4.addLayout(self.formLayout_5)
        self.b_agregar_ope = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_agregar_ope.setFont(font)
        self.b_agregar_ope.setStyleSheet("    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"")
        self.b_agregar_ope.setObjectName("b_agregar_ope")
        self.verticalLayout_4.addWidget(self.b_agregar_ope)
        self.layoutWidget3 = QtWidgets.QWidget(self.OpcionesPage3)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 190, 216, 72))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.t_nombre_4 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.t_nombre_4.setFont(font)
        self.t_nombre_4.setAlignment(QtCore.Qt.AlignCenter)
        self.t_nombre_4.setObjectName("t_nombre_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_nombre_4)
        self.e_nom_maq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.e_nom_maq.setObjectName("e_nom_maq")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.e_nom_maq)
        self.verticalLayout_5.addLayout(self.formLayout_4)
        self.b_agregar_maq = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_agregar_maq.setFont(font)
        self.b_agregar_maq.setStyleSheet("    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"")
        self.b_agregar_maq.setObjectName("b_agregar_maq")
        self.verticalLayout_5.addWidget(self.b_agregar_maq)
        self.Opciones.addTab(self.OpcionesPage3, "")

        self.retranslateUi(UI_empleados)
        self.Opciones.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UI_empleados)

        #----------------BOTONES--------------------------#
        self.mos = self.b_mostrar.clicked.connect(lambda:self.controlador.list_Emp())
        self.agre = self.b_agregar.clicked.connect(lambda:self.emp.insert_empl(self.e_idemple.text(),self.e_nombre.text().upper(),self.e_apellido.text().upper(),self.e_direccion.text(),self.e_telefono.text(),str(self.comboBox.currentText())))
        self.act = self.b_actualizar.clicked.connect(lambda:self.controlador.act_Emp())
        self.bus = self.b_buscar.clicked.connect(lambda:self.controlador.bus_Emp(self.e_codi.text()))
        self.bus_cam_maq = self.b_buscar_cam_maq.clicked.connect(lambda:self.controlador.bus_emp_maq(self.e_codi_cam_maq.text()))
        self.cam_maq = self.b_cambiarmaq.clicked.connect(lambda:self.emp.cam_maq(self.e_codi_cam_maq.text(),str(self.caja_cam_ma.currentText())))
        self.eliemp = self.b_eliminar.clicked.connect(lambda:self.controlador.delete_Emp())
        self.agre_maq = self.b_agregar_maq.clicked.connect(lambda:self.emp.insert_maq(self.e_nom_maq.text().upper()))
        self.agre_ope = self.b_agregar_ope.clicked.connect(lambda:self.emp.insert_ope(self.e_nom_ope.text().upper(),self.e_pre_ope.text(),str(self.caja_maq_ope.currentText())))
        
    def retranslateUi(self, UI_empleados):
        _translate = QtCore.QCoreApplication.translate
        UI_empleados.setWindowTitle(_translate("UI_empleados", "Empleados"))
        item = self.table_mos_empleado.horizontalHeaderItem(0)
        item.setText(_translate("UI_empleados", "ID EMPLEADO"))
        item = self.table_mos_empleado.horizontalHeaderItem(1)
        item.setText(_translate("UI_empleados", "NOMBRE "))
        item = self.table_mos_empleado.horizontalHeaderItem(2)
        item.setText(_translate("UI_empleados", "APELLIDO"))
        item = self.table_mos_empleado.horizontalHeaderItem(3)
        item.setText(_translate("UI_empleados", "DIRECCION"))
        item = self.table_mos_empleado.horizontalHeaderItem(4)
        item.setText(_translate("UI_empleados", "TELEFONO"))
        item = self.table_mos_empleado.horizontalHeaderItem(5)
        item.setText(_translate("UI_empleados", "MAQUINA"))
        self.table_mos_empleado.setColumnWidth(5,150)
        self.b_buscar.setText(_translate("UI_empleados", "BUSCAR"))
        self.e_codi.setPlaceholderText(_translate("UI_empleados", "ID"))
        self.b_mostrar.setText(_translate("UI_empleados", "REFRESCAR"))
        self.b_actualizar.setText(_translate("UI_empleados", "ACTUALIZAR"))
        self.b_eliminar.setText(_translate("UI_empleados", "ELIMINAR"))
        self.label_4.setText(_translate("UI_empleados", "EMPLEADOS"))
        self.t_idemple.setText(_translate("UI_empleados", "ID EMPLEADO*:"))
        self.t_nombre.setText(_translate("UI_empleados", "NOMBRE*:"))
        self.t_apellido.setText(_translate("UI_empleados", "APELLIDO*:"))
        self.t_direccion.setText(_translate("UI_empleados", "DIRECCION:"))
        self.t_telefono.setText(_translate("UI_empleados", "TELEFONO*:"))
        self.t_telefono_2.setText(_translate("UI_empleados", "MAQUINA:"))
        self.b_agregar.setText(_translate("UI_empleados", "AGREGAR"))
        self.label_3.setText(_translate("UI_empleados", "EMPLEADOS"))
        self.label_5.setText(_translate("UI_empleados", "AGREGAR"))
        self.t_nombre_3.setText(_translate("UI_empleados", "NOMBRE:"))
        self.text_mos_nom.setText(_translate("UI_empleados", "---"))
        self.t_maq.setText(_translate("UI_empleados", "MAQUINA:"))
        self.t_apellido_3.setText(_translate("UI_empleados", "APELLIDO:"))
        self.texto_mos_ape.setText(_translate("UI_empleados", "---"))
        self.b_cambiarmaq.setText(_translate("UI_empleados", "CAMBIAR"))
        self.label_7.setText(_translate("UI_empleados", "CAMBIAR MAQUINA"))
        self.b_buscar_cam_maq.setText(_translate("UI_empleados", "BUSCAR"))
        self.e_codi_cam_maq.setPlaceholderText(_translate("UI_empleados", "ID"))
        self.label_9.setText(_translate("UI_empleados", "AGREGAR MAQUINA"))
        self.label_10.setText(_translate("UI_empleados", "AGREGAR OPERACION"))
        self.label_11.setText(_translate("UI_empleados", "EMPLEADOS"))
        self.t_nombre_5.setText(_translate("UI_empleados", "NOMBRE*:"))
        self.t_nombre_6.setText(_translate("UI_empleados", "PRECIO*:"))
        self.t_nombre_7.setText(_translate("UI_empleados", "MAQUINA:"))
        self.b_agregar_ope.setText(_translate("UI_empleados", "AGREGAR"))
        self.t_nombre_4.setText(_translate("UI_empleados", "NOMBRE*:"))
        self.b_agregar_maq.setText(_translate("UI_empleados", "AGREGAR"))
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, _translate("UI_empleados","NINGUNA"))
        self.caja_cam_ma.addItem("")
        self.caja_cam_ma.setItemText(0, _translate("UI_empleados","NINGUNA"))
        self.caja_maq_ope.addItem("")
        self.caja_maq_ope.setItemText(0, _translate("UI_empleados","NINGUNA"))
        #-------------------Llenar cajas-----------------------#
        maq = self.emp.obt_maq()
        x= 1
        for i in maq:
            self.comboBox.addItem("")
            self.comboBox.setItemText(x, _translate("UI_empleados",i[0]))
            self.caja_cam_ma.addItem("")
            self.caja_cam_ma.setItemText(x, _translate("UI_empleados",i[0]))
            self.caja_maq_ope.addItem("")
            self.caja_maq_ope.setItemText(x, _translate("UI_empleados",i[0]))
            x = x+1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_UI_empleados()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())

