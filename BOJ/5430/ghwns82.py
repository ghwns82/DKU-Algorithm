for _ in range(int(input())):
    flag = 1
    cmd = input()
    input()
    line = input()[1:-1].split(',')
    for i in cmd:
        if i == 'R':
            flag *= -1
        if i == 'D':
            if not line or len(line)==1 and line[0]=='':
                print('error')
                break
            if flag == 1:
                del line[0]
            else:
                del line[-1]
    else:
        print('['+','.join(line[::flag]) +']')
