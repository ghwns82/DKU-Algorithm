string=input().split()
if string== sorted(string):
    print("ascending")
elif string== sorted(string)[::-1]:
    print("descending")
else:
    print('mixed')
