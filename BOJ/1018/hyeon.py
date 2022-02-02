W, H = map(int, input().split())
board = []
for i in range(W):
    board += [list(input())]
pattern = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
wrongs = []
for h in range(H - 7):  # 가로 j ~ j+7
    for w in range(W - 7):  # 세로 : i ~ i+7
        wrong = 0
        for m in range(8):
            for n in range(8):
                if board[w+m][h+n] != pattern[m%2][n]:
                    wrong += 1
        if 32 < wrong:
            wrongs.append(64-wrong)
        else:
            wrongs.append(wrong)
print(min(wrongs))



# 방법2) 백준 상에서는 메모리와 시간이 동일
'''
answer = 32
for h in range(H - 7):  # 가로 j ~ j+7
    for w in range(W - 7):  # 세로 : i ~ i+7
        wrong = 0
        for m in range(8):
            for n in range(8):
                if board[w+m][h+n] != pattern[m%2][n]:
                    wrong += 1
        # 오류 개수를 모았다가 min() 처리보다 빠르게
        if wrong < 32 and wrong < answer:
            answer = wrong
        elif (64-wrong) < answer:
            answer = 64-wrong
print(answer)
'''