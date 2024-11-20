from bs4 import BeautifulSoup

import urllib.request

import re

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
# <a class="list_subject" href="/service/board/sold/18843936?od=T31&po=0&category=0&groupCd=" data-role="cut-string">
						 
# 								<span class="category fixed" title="판매">판매</span>
# 						<span class="subject_fixed" data-role="list-title-text" title="맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.">
# 							맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.
# 						</span>
# 					</a>