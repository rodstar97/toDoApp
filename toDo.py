# toDo.py
import logging
from PySide import QtCore, QtGui
import sys
from testStuff import testStuff
from build_utils import convert_ui
from toDoApp_ui.MainWindow import ControlMainWindow

convert_ui.convert(r'Z:\Projects\toDoApp\toDoApp_ui')


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('started')
    #testStuff()
    logging.info('Finished')

if __name__ == '__main__':
    main()
    app = QtGui.QApplication(sys.argv)
    # with open(STYLESHEET, "r") as fh:
    #     app.setStyleSheet(fh.read())
    app.setStyle('Plastique')
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())