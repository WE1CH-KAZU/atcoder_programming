import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline
# 再起上限
sys.setrecursionlimit(10**6)

INF = 10**18
MOD = 998244353

def sosu_judge(n):
    # 素数かどうかを判定する
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

N, M = map(int, input().split())

syari_list = list(map(int, input().split()))
neta_list = list(map(int, input().split()))

syari_list.sort()
neta_list.sort()

ans = 0
neta_kazu = 0
for i in range(N):
    syari = syari_list[i]
    if syari*2 >= neta_list[neta_kazu]:
        ans +=1
        neta_kazu += 1
        if neta_kazu == M:
            break

print(ans)
