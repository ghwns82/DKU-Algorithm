def main():
    _ = input()
    data=tuple(map(int,input().split()))
    invmap={j:i for i,j in enumerate(sorted(set(data)))}
    for i in data:
        print(invmap[i],end=' ')
if __name__=='__main__':
    main()
