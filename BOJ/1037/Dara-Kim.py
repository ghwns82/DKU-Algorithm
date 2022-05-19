SubMulNumofN = int(input())
SubMulList = list(map(int, input().split()))
SubMulList.sort()
print(SubMulList[0] * SubMulList[-1])
