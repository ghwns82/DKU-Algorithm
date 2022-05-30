def Hanoi(n, fr, tmp, to):

    if n == 1:
        print(f"{fr} {to}")
    else:
        Hanoi(n - 1, fr, to, tmp)
        print(f"{fr} {to}")
        Hanoi(n - 1, tmp, fr, to)


n = int(input())

print(2**n - 1)
Hanoi(n, 1, 2, 3)
