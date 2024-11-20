import random

print(random.random())
print(random.random())

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print(random.sample(range(20),10))
print(random.sample(range(20),10))

# 파일명, 파일정보
from os.path import *

print(abspath("python.exe"))
print(basename("c:\\workspace\\python.exe"))

# r = raw string notation
fileName = r"c:\\python310\python.exe"

if exists(fileName):
    print("파일크기:{0}".format(getsize(fileName)))
else:
    print("파일 없음")

# 운영체제 정보
import os
print("운영체제명:", os.name)
# print("환경변수:", os.environ)

#외부 프로세스 실행
# os.system("notepad.exe")

import glob

print(glob.glob(r"c:\workspace\*.py"))