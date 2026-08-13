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

# permutationsを使って順列組み合わせを算出する

N = int(input())

# permutationsはtupleなのでlistではなくtuple
P_lis = tuple(map(int, input().split()))
Q_lis = tuple(map(int, input().split()))

res=0
for x in permutations(range(1,N+1)):
    if P_lis < x < Q_lis:
        res +=1

print(res)
