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

A, B = map(int, input().split())

a = A + B
b = A - B
c = A * B

if a == 9 or b == 9 or c == 9:
    print('Nine')
elif A == 9 * B:
    print('Nine')
else:
    print('Nein')
