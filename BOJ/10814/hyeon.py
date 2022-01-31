cnt = int(input())
data = []
for i in range(cnt):
    age, name = input().split()
    data += [[int(age), name]]

data.sort(key = lambda x : x[0])
for i, n in data:
    print(i, n)
