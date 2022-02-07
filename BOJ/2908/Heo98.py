'''
3자리 숫자를 말하고 그것을 거꾸로 읽어서 큰수를 출력
숫자 2개를 받고 input().split() 각 변수에 넣어준다.
뒤에서 부터 읽어서 저장해주고 int형으로 바꿔준다.
'''

first, second= input().split()
first=int(first[::-1])
second=int(second[::-1])
if first> second:
    print(first)
else:
    print(second)
