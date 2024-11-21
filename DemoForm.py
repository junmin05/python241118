# DemoForm2.ui(화면)

import sys
from bs4 import BeautifulSoup
import urllib.request
import re
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일 로드
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 화면 생성
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 위젯")
    def firstClick(self):
        f = open("clien.txt", "wt", encoding="utf-8")

        for i in range(0, 10):
            url = "https://www.clien.net/service/board/sold?od=T31&catrgory=0&po=" + str(i)
            # print(url)
                
            response = urllib.request.urlopen(url)

            page = response.read().decode("utf-8")

            soup = BeautifulSoup(page, "html.parser")

            list = soup.find_all("a", attrs={"class": "list_subject"})

            for item in list:
                try:
                    title = item.find("span", attrs={"data-role": "list-title-text"})
                    title = title.text.strip()
                    # print(title)
                    if re.search("맥북", title):
                        print(title)
                        f.write(title + "\n")
                except:
                    pass

        f.close()
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
