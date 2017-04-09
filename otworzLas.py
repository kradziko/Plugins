from PyQt4.QtCore import *
from PyQt4.QtGui import *
from otworzLas_dialog import OtworzLasDialog
from PyQt4 import QtGui, uic
from qgis.core import *

# initialize Qt resources from file resources.py
import resources


class OtworzLas():
    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface

    def config(self):
        dlg = OtworzLasDialog()
        dlg.label_2.hide()

        dlg.show()

    def initGui(self):
        pass


    def unload(self):
        pass

    def run(self):
        pass

    def renderTest(self, painter):
        pass