# 9095 1,2,3 더하기
import sys
input = sys.stdin.readline
result = [1, 2, 4]
for i in range(3,10):
    result.append(sum(result[i-3:i]))
for _ in range(int(input())):
    print(result[int(input())-1])
