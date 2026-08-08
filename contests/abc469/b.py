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

S = input().strip()

res = 0
for i in range(N):
    if S[i] != 'x':
        continue

    # hidari ok
    h_ok = (i == 0 or S[i-1] == 'x')

    # migi ok
    m_ok = (i == N-1 or S[i+1] == 'x')

    # AND check
    if h_ok and m_ok:
        res +=1

print(res)
