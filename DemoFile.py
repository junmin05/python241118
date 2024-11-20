# 쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close

f = open("demo.txt","rt",encoding="utf-8")
result = f.read()
print(result)
f.close()

# 문자열처리
strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print("MBC250".isalnum())
print("2580".isdecimal())
data = " spam and ham "
result = data.strip()
print(result)
print("--리스트로 변환--")
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print( ":)".join(lst))


# 정규표현식:특정 패턴 검색
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

rresult = re.search("apple", "this is apple")
print(result.group())