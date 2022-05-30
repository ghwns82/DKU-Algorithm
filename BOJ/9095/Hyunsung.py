#9095 1, 2, 3 더하기 실버 3

import sys
input = sys.stdin.readline

count = 0

def plus(a) :
    global count 
    if a == 0 :
        count += 1
        return
    else :
        if a - 1 >= 0 :
            plus(a - 1)
        if a - 2 >= 0 :
            plus(a - 2)
        if a - 3 >= 0 :
             plus(a - 3)

num = int(input())
for i in range(num) :
    plus(int(input()))
    print(count)
    count = 0