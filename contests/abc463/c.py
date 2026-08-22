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

N = int(input())

# H= 身長
# L= 退出時間
Hs = [0] * N
Ls = [0] * N

for i in range(N):
    H, L = map(int, input().split())
    Hs[i] = H
    Ls[i] = L

# sufmax[i] = Hs[i:] の最大値
sufmax = [0] * (N + 1)
# N-1から-1(手前の0)までを-1ずつループ
for i in range(N - 1, -1, -1):
    # sufmax[i] を「index i 以降の H の最大値」と定義
    sufmax[i] = max(sufmax[i + 1], Hs[i])

Q = int(input())
T = list(map(int, input().split()))

res = []
for i in range(Q):
    idx = bisect_right(Ls, T[i])  # Ls[idx] 以降が「まだ残っている人」
    res.append(sufmax[idx]) # 「そこから先の最大身長」

print("\n".join(map(str, res)))