"""決め打ち全探索"""

import re
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

# N=宝石の数
# K=選んだ数
# M=宝石の色の種類
N, K, M = map(int, input().split())

color_value = defaultdict(list)
for _ in range(N):
    C, V = map(int, input().split())
    color_value[C].append(V)


max_val = []
theother_val = []

for color in color_value.values():
    color.sort(reverse=True)
    max_val.append(color[0])
    theother_val.extend(color[1:])

max_val.sort(reverse=True)
theother_val.sort(reverse=True)

ruiseki = [0] * (len(max_val) + 1)
for i in range(len(max_val)):
    ruiseki[i+1] = ruiseki[i] + max_val[i]

ruiseki_other = [0] * (len(theother_val) + 1)
for i in range(len(theother_val)):
    ruiseki_other[i+1] = ruiseki_other[i] + theother_val[i]

ans = 0
for i in range(M, min(len(max_val), K) + 1):
    if K - i > len(theother_val):
        continue
    ans = max(
        ans,
        ruiseki[i] + ruiseki_other[K - i]
    )

print(ans)
