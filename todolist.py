import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 나가기 버튼 만든거 및
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)


        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar().showMessage('Ready')

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
   ex = MyApp()
   sys.exit(app.exec_())