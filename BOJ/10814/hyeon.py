cnt = int(input())
data = []
for i in range(cnt):
    age, name = input().split()
    data += [[int(age), name]]
# 나이순 정렬 -> 입력된 순서대로 정렬
data.sort(key = lambda x : x[0])
for i, n in data:
    print(i, n)
