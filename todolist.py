import sys
from PyQt5.QtWidgets import *

from PyQt5 import uic
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow,form_class):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())