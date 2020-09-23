import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # 중앙위젯에 MainWidget을 연결
        main_widget = MainWidget(self)
        main_widget.select_btn.clicked.connect(self.selected)
        self.central_widget.addWidget(main_widget)

        exitAction = QAction('Exit', self) # 아이콘과 Exit 라벨을 같은 동작을 만듦
        exitAction.setShortcut('Ctrl+Q') # 단축키를 정의함
        exitAction.setStatusTip('Exit application') # 마우스를 올렸을 때 나오는 메시지
        exitAction.triggered.connect(qApp.quit) # 이 동작을 선택했을 때 생성된 시그널이 위젯의 메서드에 연결되고 프로그램이 종료되게 만듦

        saveAction = QAction('Save', self)  # 아이콘과 Exit 라벨을 같은 동작을 만듦
        saveAction.setShortcut('Ctrl+S')  # 단축키를 정의함
        saveAction.setStatusTip('Save as')  # 마우스를 올렸을 때 나오는 메시지
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


        # def select_btn_func(self):



    def selected(self):
        selecting_the_day = selectedDay(self)
        self.central_widget.addWidget(selecting_the_day)
        self.central_widget.setCurrentWidget(selecting_the_day)

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        cal = QCalendarWidget(self)  # QcalendarWidget의 객체를 하나 만듭니다.
        cal.setGridVisible(True)  # 그리드 온
        cal.setMinimumDate(QDate(2020, 1, 1))  # 캘린더 시작 날짜 선정
        cal.setMaximumDate(QDate(2030, 12, 31))  # 캘린더 끝 날짜 선정
        cal.clicked[QDate].connect(self.showDate)  # 날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줌


        self.middle_title_lbl = QLabel('날짜 선택')
        self.lbl = QLabel(self)
        date = cal.selectedDate()  # selectedDate는 현재 선택된 날짜 정보를 가지고 있습니다.
        self.lbl.setText(date.toString())  # 현재 날짜정보를 라벨에 표시되도록 해줍니다.

        self.select_btn = QPushButton('선택')


        vbox = QVBoxLayout()
        vbox.addWidget(self.middle_title_lbl)
        vbox.addWidget(cal)  # 달력
        vbox.addWidget(self.lbl)  # 라벨을 수직으로
        vbox.addWidget(self.select_btn)
        self.setLayout(vbox)


    def showDate(self, date):  # 날짜를 클릭 할 때 마다 라벨 텍스트가 선택한 날짜로 표시되도록 합니다.
        self.lbl.setText(date.toString())



class selectedDay(QWidget):
    def __init__(self, parent=None):
        super(selectedDay, self).__init__(parent)

        grid = QGridLayout()
        self.setLayout(grid)

        names = [' ', ' ', ' ', ' ',
                 ' ', ' ', ' ', ' ',
                 ' ', ' ', ' ', ' ',
                 ' ', ' ', ' ', ' ',
                 ' ', ' ', ' ', ' ']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            lineedit = QLineEdit(name)
            grid.addWidget(lineedit, *position)

        self.move(300, 150)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())