from MainWindow_ui import Ui_MainWindow
from PySide import QtCore, QtGui

class ControlMainWindow(QtGui.QMainWindow,Ui_MainWindow):
    """
        MainWindow for Asset import, QWidget for docking

    """
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)
        self.assetList = []
