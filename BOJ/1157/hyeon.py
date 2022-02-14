data = input().upper()

result = {}
max = 0
answer = []
for d in data:
    if d not in result.keys():
        result[d] = 1
        if max < 1:
            max = 1
            answer += [d]
    else:
        result[d] += 1
        if result[d] > max:
            max = result[d]
            answer = [d]
        elif result[d] == max:
            answer += [d]

if len(answer) == 1:
    print(answer[0])
else:
    print('?')