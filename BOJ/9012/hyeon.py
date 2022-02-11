cnt = int(input())
for i in range(cnt):
    st = list(input())
    left = 0
    state = "YES"
    for c in st:
        if c == '(':
            left += 1
        else:
            if left == 0: # ')'에 비해 '('가 부족한 경우
                state = "NO"
                break
            left -= 1
    if left > 0: # '('에 비해 ')'가 부족한 경우
        state = "NO"
    print(state)