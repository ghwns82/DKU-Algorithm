import sys

scale = list(map(int, sys.stdin.readline().rstrip().split()))
standard = [x for x in range(1, 9)]
reverse_s = sorted(standard, reverse=True)

if scale[0] == 1:
    if standard == scale:
        print("ascending")
    else:
        print("mixed")
elif scale[0] == 8:
    if reverse_s == scale:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")