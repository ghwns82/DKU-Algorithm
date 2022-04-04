#1259 팰린드롬수 브론즈 1

import sys
input = sys.stdin.readline

while(True) :
    num = int(input())
    if num == 0 :
        break
    else :
        number = []
        flag = 1
        for i in str(num):
            number.append(i)
        
        for i in range((len(number) // 2) + 1) :
            if number[i] != number[-i - 1] :
                flag = 0
                break

        if flag == 1 :
            print('yes')
        else :
            print('no')
