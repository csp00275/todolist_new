import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWidget(QWidget): # 위젯
    def __init__(self):
        super().__init__()
        # 캘린더
        cal = QCalendarWidget(self) # QcalendarWidget의 객체를 하나 만듭니다.
        cal.setGridVisible(True) # 그리드 온
        cal.setMinimumDate(QDate(2020,9,22)) # 캘린더 시작 날짜 선정
        cal.setMaximumDate(QDate(2030,12,31)) # 캘린더 끝 날짜 선정
        cal.clicked[QDate].connect(self.showDate) # 날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줌

        self.lbl = QLabel(self)
        date = cal.selectedDate()  # selectedDate는 현재 선택된 날짜 정보를 가지고 있습니다.
        self.lbl.setText(date.toString()) # 현재 날짜정보를 라벨에 표시되도록 해줍니다.

        # 레이아웃 설정


        # 선택 버튼
        select_btn = QPushButton('&선택',self)
        select_btn.clicked.connect(self.mainwidget)
        select_btn.setCheckable(False)
        # selcect_btn.animateClick(True)
        # selcect_btn.toggle()


        # 레이아웃 설정 (수직레이아웃)
        vbox = QVBoxLayout()
        vbox.addWidget(cal)  # 달력
        vbox.addWidget(self.lbl)  # 라벨을 수직으로
        vbox.addWidget(select_btn)
        self.setLayout(vbox)

        self.setGeometry(300, 100, 350, 150) # x, y, width, height

    # def select_btn_func(self):

    def showDate(self, date):  # 날짜를 클릭 할 때 마다 라벨 텍스트가 선택한 날짜로 표시되도록 합니다.
        self.lbl.setText(date.toString())
    def mainwidget(self):
        print('selected')

class TodolistWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.select_btn = QPushButton('Login')
        layout.addWidget(self.select_btn)
        self.setLayout(layout)

class MainWindow(QMainWindow):  # 메인 윈도우
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        Main_widget = MainWidget()
        Main_widget.select_btn.cllicked.connect(self.select_btn1)
        self.central_widget.addWidget(Main_widget)

        label1 = QLabel('MainWindow Label', self)
        label1.setAlignment(Qt.AlignCenter)

        exitAction = QAction('Exit', self) # 아이콘과 Exit 라벨을 같은 동작을 만듦
        exitAction.setShortcut('Ctrl+Q') # 단축키를 정의함
        exitAction.setStatusTip('Exit application') # 마우스를 올렸을 때 나오는 메시지
        exitAction.triggered.connect(qApp.quit) # 이 동작을 선택했을 때 생성된 시그널이 위젯의 메서드에 연결되고 프로그램이 종료되게 만듦

        saveAction = QAction('Save', self)  # 아이콘과 Exit 라벨을 같은 동작을 만듦
        saveAction.setShortcut('Ctrl+S')  # 단축키를 정의함
        saveAction.setStatusTip('Exit application')  # 마우스를 올렸을 때 나오는 메시지
        saveAction.triggered.connect(qApp.quit)  # 이 동작을 선택했을 때 생성된 시그널이 위젯의 메서드에 연결되

        self.statusBar()

        menubar = self.menuBar() # 메뉴바를 생성함
        menubar.setNativeMenuBar(False) # ???
        filemenu = menubar.addMenu('&File') # File 앞에 앰퍼샌트가 있어서 alt + F가 단축키임
        filemenu.addAction(exitAction)
        filemenu.addAction(saveAction)

        self.statusBar().showMessage('상태창에뭐쓰지')

        self.setWindowTitle('박재형의 할 일 목록')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def select_btn1(self):
        to_do_list = TodolistWidget(self)
        self.central_widget.addWidget(to_do_list)
        self.central_widget.setCurrentWidget(to_do_list)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()