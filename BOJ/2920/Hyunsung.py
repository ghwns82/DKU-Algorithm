#2920 음계 브론즈 2

import sys
input = sys.stdin.readline

flag = 0
play = list(map(int, input().split()))

for i in range(6) :
    if play[i] - play[i + 1] == play[i + 1] - play[i + 2] :
        if play[i] - play[i + 1] == -1 :
            flag = 1
        elif play[i] - play[i + 1] == 1 :
            flag = -1
        continue
    else :
        flag = 0
        break

if flag == 1 :
    print('ascending')
elif flag == -1 : 
    print('descending')
else :
    print('mixed')