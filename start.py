#from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication,  QMainWindow
from ui.ui import MainWindow
#from ui.dialog import Dialog
if __name__ == "__main__":
    import sys 
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

