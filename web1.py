from bs4 import BeautifulSoup

page = open("Chap09_test.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())

# print(soup.find_all("p"))

# print(soup.find("p", class_="inner-text"))

print(soup.find_all("p", attrs={"class": "inner-text"}))

# 태그 내부에 존재하는 텍스트만 출력
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)
