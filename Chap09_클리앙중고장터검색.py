#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

hdr = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75'}

for n in range(0,11):
        #오늘의 유머 베스트 게시판 
        url = "https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" + str(n)
        print(url)
        # 웹브라우저 헤더 추가
        req = urllib.request.Request(url, headers=hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        
        for item in list:
            try:
                title = item.find("a")
                title = title.text.strip()
                # print(title)
                if re.search("미국", title):
                    print(title)
            except:
                pass


