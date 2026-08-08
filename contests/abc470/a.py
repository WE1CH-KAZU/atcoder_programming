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

N = int(input())

for i in range(1, N + 1):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
