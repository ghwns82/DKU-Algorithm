# #1620 나는야 포켓몬 마스터 이다솜 실버 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_name = {}
pokemon_num = {}

for i in range(1, N + 1) :
    monster = str(input()).strip()
    pokemon_name[i] = monster
    pokemon_num[monster] = i

for _ in range(M) :
    quest = str(input()).strip()
    try :
        print(pokemon_name[int(quest)])
    except :
        print(pokemon_num[quest])
