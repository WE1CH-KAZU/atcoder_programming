import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

N, K = map(int, input().split())

A = Counter(map(int, input().split()))

kurasu = [0] * (K+1)
for i in range(K+1):
    kurasu[i] = A[i]

max_ninzu= max(kurasu)

max_ninzu_1 = max_ninzu - 1

ans = 0
for i in range(1, K+1):
    if kurasu[i] >= max_ninzu_1:
        ans += 1

print(ans)

