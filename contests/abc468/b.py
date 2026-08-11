"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

# M: マス個数
# D: ガードマン監視距離
M,D = map(int, input().split())
G = input()

res = [False] * M

for i , g in enumerate(G):
    if g == 'G':
        for j in range(max(0, i - D), min(M, i + D + 1), 1):  # 最小値はmax(0,x-D)で負値を防ぎ、最大値はmin(M, x+D)でM+1を防ぐ
            res[j] = True

print(res.count(False))
