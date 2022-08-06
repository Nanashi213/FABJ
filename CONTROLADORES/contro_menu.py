import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class PrincipalController():

    def __init__(self, principal):
        
        self.principal = principal
    
    def openCreate(self, Ui_empleados):
        self.principal.Form = QtWidgets.QWidget()
        self.principal.ui = Ui_empleados()
        self.principal.ui.setupUi(self.principal.Form)
        self.principal.Form.show()

    