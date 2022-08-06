import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from CONTROLADORES.contro_menu import PrincipalController
from UIS.UI_empleados import  Ui_UI_empleados
from UIS.UI_lotes import Ui_lotes
from UIS.UI_gastos import Ui_Gastos
from UIS.UI_clientes import Ui_clientes
from UIS.UI_abonos import Ui_abonos
from UIS.UI_sueldo import Ui_sueldo


class Ui_menu_principal(object):

    def __init__(self):
        self.principal_controller = PrincipalController(self)

    def setupUi(self, menu_principal):
        menu_principal.setObjectName("menu_principal")
        menu_principal.resize(737, 298)
        menu_principal.setStyleSheet("#menu_principal{\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"#B_empleados{\n"
"    background-color: ;\n"
"    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"\n"
"#B_lotes{\n"
"    background-color: ;\n"
"    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"\n"
"#B_cliente{\n"
"    background-color: ;\n"
"    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#B_abonos{\n"
"    background-color: ;\n"
"    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#B_gastos{\n"
"    background-color: ;\n"
"    background-color: rgb(93, 179, 255);\n"
"    border: 2px solid #fff;\n"
"    color: #fff;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"}")
        menu_principal.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(menu_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 91))
        self.frame.setStyleSheet("background-color: rgb(137, 101, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(10, -20, 151, 131))
        self.pushButton.setStyleSheet("border: None;background-color: rgb(137, 101, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/data_storage_database_icon_194717.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/iconos/data_storage_database_icon_194717.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 10, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(48)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(137, 101, 255);")
        self.label.setObjectName("label")
        self.B_empleados_2 = QtWidgets.QPushButton(self.frame)
        self.B_empleados_2.setGeometry(QtCore.QRect(620, 10, 81, 71))
        self.B_empleados_2.setStyleSheet("    background-color: ;\n"
"    background-color: ;\n"
"    border-radius: 12px;")
        self.B_empleados_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/prefijoNuevo/calcu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_empleados_2.setIcon(icon1)
        self.B_empleados_2.setIconSize(QtCore.QSize(70, 90))
        self.B_empleados_2.setObjectName("B_empleados_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 110, 710, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.B_empleados = QtWidgets.QPushButton(self.layoutWidget)
        self.B_empleados.setStyleSheet("QpushButton{\n"
"\n"
"    background-color: rgb(67, 255, 255);\n"
"    border-radius: 12px;\n"
"}")
        self.B_empleados.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/empleados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_empleados.setIcon(icon2)
        self.B_empleados.setIconSize(QtCore.QSize(100, 100))
        self.B_empleados.setObjectName("B_empleados")
        self.gridLayout.addWidget(self.B_empleados, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 1)
        self.B_gastos = QtWidgets.QPushButton(self.layoutWidget)
        self.B_gastos.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/descarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_gastos.setIcon(icon3)
        self.B_gastos.setIconSize(QtCore.QSize(100, 100))
        self.B_gastos.setObjectName("B_gastos")
        self.gridLayout.addWidget(self.B_gastos, 2, 4, 1, 1)
        self.B_lotes = QtWidgets.QPushButton(self.layoutWidget)
        self.B_lotes.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.B_lotes.setStyleSheet("")
        self.B_lotes.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconos/34479120-jeans-o-pantalones-de-los-hombres-firman-icono-casual-símbolo-ropa-botones-de-círculo-con-larga-somb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_lotes.setIcon(icon4)
        self.B_lotes.setIconSize(QtCore.QSize(100, 100))
        self.B_lotes.setObjectName("B_lotes")
        self.gridLayout.addWidget(self.B_lotes, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.B_abonos = QtWidgets.QPushButton(self.layoutWidget)
        self.B_abonos.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconos/shoppaymentorderbuy-04_icon-icons.com_73886.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_abonos.setIcon(icon5)
        self.B_abonos.setIconSize(QtCore.QSize(100, 100))
        self.B_abonos.setObjectName("B_abonos")
        self.gridLayout.addWidget(self.B_abonos, 2, 3, 1, 1)
        self.B_cliente = QtWidgets.QPushButton(self.layoutWidget)
        self.B_cliente.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconos/users_people_workers_customers_icon_124243.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_cliente.setIcon(icon6)
        self.B_cliente.setIconSize(QtCore.QSize(100, 100))
        self.B_cliente.setObjectName("B_cliente")
        self.gridLayout.addWidget(self.B_cliente, 2, 2, 1, 1)
        self.layoutWidget.raise_()
        self.frame.raise_()
        menu_principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu_principal)
        QtCore.QMetaObject.connectSlotsByName(menu_principal)
        self.emp = self.B_empleados.clicked.connect(lambda:self.principal_controller.openCreate(Ui_UI_empleados))
        self.cli = self.B_cliente.clicked.connect(lambda:self.principal_controller.openCreate(Ui_clientes))
        self.gas = self.B_gastos.clicked.connect(lambda:self.principal_controller.openCreate(Ui_Gastos))
        self.lot = self.B_lotes.clicked.connect(lambda:self.principal_controller.openCreate(Ui_lotes))
        self.abo = self.B_abonos.clicked.connect(lambda:self.principal_controller.openCreate(Ui_abonos))
        self.sueldo = self.B_empleados_2.clicked.connect(lambda:self.principal_controller.openCreate(Ui_sueldo))
        

    def retranslateUi(self, menu_principal):
        _translate = QtCore.QCoreApplication.translate
        menu_principal.setWindowTitle(_translate("menu_principal", "MENU"))
        self.label.setText(_translate("menu_principal", "FABJ"))
        self.label_2.setText(_translate("menu_principal", "Empleados"))
        self.label_5.setText(_translate("menu_principal", "Gastos"))
        self.label_6.setText(_translate("menu_principal", "Abonos"))
        self.label_4.setText(_translate("menu_principal", "Clientes"))
        self.label_3.setText(_translate("menu_principal", "Lotes"))
import IMAGENES.calcu
import IMAGENES.ima
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_menu_principal()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())