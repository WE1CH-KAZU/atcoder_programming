import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline
# 再起上限
sys.setrecursionlimit(10**6)

INF = 10**18
MOD = 998244353

N = int(input())

P = list(map(int, input().split()))

for i, p in enumerate(P):
    if i // 10 != (p-1) // 10:
        print("No")
        sys.exit()

print("Yes")
