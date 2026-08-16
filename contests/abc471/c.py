"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import permutations # 順列組み合わせ

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

# 座標数
N = int(input())

distance = 0
init = 0

A = sorted(map(int, input().split()))

lef = bisect_left(A, 0) -1 # 負の方向
rig = lef + 1 # 正の方向

for _ in range(N):
    if lef >= 0:
        d_lef = init - A[lef]
    else:
        d_lef = INF

    if rig <= N-1:
        d_rig = A[rig] - init
    else:
        d_rig = INF

    # 近い方はどっちか
    if d_lef <= d_rig:
        distance += d_lef
        # 座標更新
        init = A[lef]
        lef -=1
    else:
        distance += d_rig
        # 座標更新
        init = A[rig]
        rig +=1

print(distance)

