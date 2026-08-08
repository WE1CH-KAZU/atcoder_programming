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

# 1 <= a,b,c <= 10
counts = Counter(map(int, input().split()))

# 5が2個、7が1個あるかを調べる
if counts[5] == 2 and counts[7] == 1:
    print("YES")
else:
    print("NO")
