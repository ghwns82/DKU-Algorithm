#1018 체스판 다시 칠하기

x, y = map(int, input().split())
board = []
count = []

for i in range(x) :
    board.append(input())

for a in range(x - 7) :
    for b in range(y - 7) :
        first = 0
        second = 0
        for i in range(a, a + 8) :
            for j in range(b, b + 8) :
                if (i + j) % 2 == 0 :
                    if board[i][j] != 'W' :
                        first += 1
                    if board[i][j] != 'B' :
                        second += 1
                else :
                    if board[i][j] != 'B' :
                        first += 1
                    if board[i][j] != 'W' :
                        second += 1
        count.append(first)
        count.append(second)
        
print(min(count))