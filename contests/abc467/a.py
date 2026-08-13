"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import permutations

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

H, W = map(int, input().split())
H_m = H /100

bmi = W / H_m / H_m
if bmi >= 25:
    print('Yes')
else:
    print('No')
