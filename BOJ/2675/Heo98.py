T=int(input())
for i in range(T):
    num, string=input().split()
    for char in string:
        print(char*int(num),end='')
    print()
