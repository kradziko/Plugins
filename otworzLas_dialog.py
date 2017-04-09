import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox, QFrame

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__),'otworzLas_dialog.ui'))
class OtworzLasDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.otworzLas = parent

        self.get_config_main_window()

        self.checkBox.stateChanged.connect(self.showOutput)

    def showOutput(self):
        pass
