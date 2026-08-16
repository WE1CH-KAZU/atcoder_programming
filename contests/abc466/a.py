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

N = int(input())

X = list(map(int, input().split()))

if X[0] < 0 and X[N-1] < 0:
    print('Yes')
else:
    print('No')
