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

N, Q = map(int, input().split())

last = [0] * (N+1)

P = list(map(int, input().split()))

for q in range(1,Q+1):
    # 保存
    a = int(input())
    last[a] = q

nokori = [
    v for v in P if last[v] ==0
]

idou = sorted(
    [v for v in P if last[v] > 0 ],
    key=lambda x: last[x],
)

ans = nokori + idou

print(*ans)
