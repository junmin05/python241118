value = 5
while value > 0:
    print(value)
    value -= 1

list = [100,"python",3.14]
for item in list:
    print(item, type(item))

print("--dict형태--")
fruits = {"apple":"red", "kiwi": "green"}
for k,v, in fruits.items():
    print(k,v)

# print("--range함수--")
# print(list(range(10)))
# print(list(range(2000,2025)))
# print(list(range(1,32)))

# for i in range(10):
#     print(i)

print("--필터링 함수--")
lst = [10, 25, 30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

def getBiggerThan20(i):
    return i > 20

print("--필터링 함수 있음--")
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("--람다 함수 있음--")
itemL = filter(lambda i:i>20, lst)
for item in itemL:
    print(item)