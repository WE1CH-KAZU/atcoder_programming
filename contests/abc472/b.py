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

L = list(map(int, input().split()))
ans = INF
for i in range(N-1):
    left = L[:i+1]
    right = L[i+1:]
    suml = sum(left)
    sumr = sum(right)
    ans = min(ans, abs(suml-sumr))

print(ans)
