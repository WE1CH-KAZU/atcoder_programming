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

N, K = map(int, input().split())

# 全探索
# ループはN回、O(6N) => O(N)

count = 0

for i in range(1, N + 1):
    d_sum = sum(map(int, str(i)))
    if d_sum == K:
        count += 1

print(count)
