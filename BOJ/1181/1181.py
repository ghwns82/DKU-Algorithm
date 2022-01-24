import sys
data = []

cnt = int(sys.stdin.readline())
for i in range(cnt):
    s = sys.stdin.readline().rstrip() # 개행문자 제거
    if s not in data: # 중복 방지
        data.append(s)
data.sort(key = lambda x: x) # 조건2 : 사전 순
data.sort(key = lambda x: len(x)) # 조건1 : 길이가 짧은 순

for d in data:
    print(d)