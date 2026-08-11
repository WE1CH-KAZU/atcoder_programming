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
A = list(map(int, input().split()))

ans = 0
for i in range(1,N-2,1):
    a1 = A[i]
    a2 = A[i+1]
    a3 = A[i+2]
    if a1 < a2 > a3:
        ans += 1

print(ans)
