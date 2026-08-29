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

A = Counter(map(int,input().split()))

ans = 0
for key, items in A.items():
    if items % 2:
        ans += key

print(ans)
