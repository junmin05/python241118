# DemoListSet

# List
colors = ["red", "blue", "green"]
print(colors)
colors.append("white")
print(colors)
colors.append("yellow")
print(colors)

# Set
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Tuple
tp = (10,20,30)
print(tp)
print(len(tp))

# 함수 정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

# 형식변환(Type Casting)
a = set((1,2,3))
print(a)
b=list(a)
b.append(4)
print(b)

colors2 = {"apple":"red", "banana":"yellow"}

for item in colors2.items:
    print(item)