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

N, L = map(int, input().split())

S =[input().strip() for _ in range(N)]

S.sort()

print("".join(S))
