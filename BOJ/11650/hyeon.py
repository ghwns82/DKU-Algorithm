import sys

cnt = int(sys.stdin.readline())
points = []
for i in range(cnt):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x,y])
points.sort(key = lambda x: (x[0], x[1]))
# x좌표 오름차순 정렬 -> y좌표 오름차순 정렬
for point in points:
    print(point[0], point[1])
