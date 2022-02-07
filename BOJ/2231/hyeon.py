num = input().rstrip()
length = len(num)
i_num = int(num)
start = i_num - length*9
end = i_num-length
answer = 0
if start < 0: # 8이하의 숫자는 -값이 나옴
    start = 1
for i in range(start, end+1):
    if i + sum([int(x) for x in str(i)]) == i_num:
        answer = i
        break
print(answer)