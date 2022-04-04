K = int(input())

integerList = []
for a in range(K):
    integer = int(input())

    if integer == 0:
        integerList.pop()
    else:
        integerList.append(integer)

print(sum(integerList))
