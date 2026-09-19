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

N, M, K = map(int, input().split())
X, Y = map(int, input().split())

desert_list = list(map(int, input().split()))
drink_list = list(map(int, input().split()))
desert_list.sort()
drink_list.sort()

desert_sum = [0]*(N+1)
for i in range(N):
    desert_sum[i+1] = desert_sum[i] + desert_list[i]

drink_sum = [0]*(M+1)
for i in range(M):
    drink_sum[i+1] = drink_sum[i] + drink_list[i]

drink_sum_k = [0]*(M+1)
for i in range(M):
    drink_sum_k[i+1] = drink_sum_k[i] + (drink_list[i] + K-1) // K

ans = 0
for d in range(M+1):
    if drink_sum_k[d] > Y:
        continue
    nokori = (X + Y*K) - drink_sum[d]
    desert_kosu = bisect_right(desert_sum, nokori) - 1

    ans = max(ans, d + desert_kosu)

print(ans)

