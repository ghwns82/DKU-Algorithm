#11723 집합 실버 5

import sys

num = int(input())
sets = set()

for i in range(num) :
    command = sys.stdin.readline().strip().split()

    if len(command) == 1 :
        if command[0] == 'all' :
            sets = set([i for i in range(1, 21)])
            
        elif command[0] == 'empty' :
            sets = set()

    else :
        a = command[0]
        b = command[1]
        b = int (b)

        if a == 'add' :
            sets.add(b)

        elif a == 'remove' :
            if b in sets :
                sets.discard(b)
        
        elif a == 'check' :
            if b in sets :
                print('1')
            else :
                print('0')

        elif a == 'toggle' :
            if b in sets :
                sets.discard(b)
            else :
                sets.add(b)