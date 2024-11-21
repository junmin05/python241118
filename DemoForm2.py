# DemoForm.ui(화면)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일 로드
form_class = uic.loadUiType("DemoForm.ui")[0]

# 화면 생성
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 위젯")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
