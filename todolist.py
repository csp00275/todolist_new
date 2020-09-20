import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

class PyQt5Bar(QMainWindow):
    def __init__(self):
        super().__init__()
        wg = ()
        self.Main_bar()
        self.setCentralWidget(wg)

    def Main_Bar(self):
        self.statusbar().showMessage('ready')

        self.geometry(300,300,300,200)
        self.setWindowTitle('StatusBar_Form')
        self.show()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        detailMenu = QMenu('Detail',self)
        detailAct = QAction('real Detail',self)
        detailMenu.addAction(detailAct)

        newAct = QAction('New',self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(detailMenu)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁에 사용될 폰트 및 사이즈
        self.setToolTip('This is a <b>QWidget</b> widget') # ???

        btn = QPushButton('Button', self) # 푸시버튼을 하나 만듭니다.
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 푸시버튼에 툴팁을 달아줍니다.
        btn.move(50, 50) # 버튼의 위치와 크기를 설정합니다.
        btn.resize(btn.sizeHint()) # 버튼을 적절한 크기로 설정하도록 도와줍니다


        self.setWindowTitle('My First Application') # 창의 제목을 결정합니다.
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300,300,400,200) # 창의 위치 , 창의 크기
        self.show() # 위젯을 스크린에 보여줍니다


if __name__ == '__main__':
   app = QApplication(sys.argv)
   form = PyQt5Bar()
   form.show()
   app.exec_()
