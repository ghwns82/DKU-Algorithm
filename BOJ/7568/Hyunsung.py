#7568 덩치 실버 5

import sys
input = sys.stdin.readline

num = int(input())
person = []
answer = []

for i in range(num) :
    person.append(list(map(int, input().split())))

for i in range(num) :
    rank = 1
    for j in range(num) :
        if person[i][0] != person[j][0] and person[i][1] != person[j][1] :
            if person[i][0] < person[j][0] and person[i][1] < person[j][1] :
                rank += 1
    print(rank, end = ' ')