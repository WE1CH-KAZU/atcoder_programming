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

N, S, L = map(int, input().split())
s = S - 1
A = list(map(int, input().split()))

P = [0]*(N)
for i in range(N-1):
    P[i+1] = A[i] + P[i]

ans = 0
for i in range(s+1):
    temp = P[s] - P[i]
    nokori = L - 2*temp
    if nokori < 0:
        continue

    jogen = P[s] + nokori
    j = bisect_right(P, jogen) - 1
    ans = max(ans, j - i + 1)


# 反対方向
for j in range(s, N):
    temp = P[j] - P[s]
    nokori = L - 2*temp
    if nokori < 0:
        continue

    kagen = P[s] - nokori
    i = bisect_left(P, kagen)
    ans = max(ans, j - i + 1)

print(ans)
