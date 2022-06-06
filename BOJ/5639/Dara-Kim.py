import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 늘려줌
nums = []

while True: # 입력 종료 조건X, 입력이 있을 때까지만                     
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if nums[start] < nums[i]:
            mid = i
            break
    
    postorder(start+1, mid-1) # 왼쪽도 탐색
    postorder(mid, end) # 오른쪽도 탐색
    print(nums[start])

postorder(0, len(nums)-1)
