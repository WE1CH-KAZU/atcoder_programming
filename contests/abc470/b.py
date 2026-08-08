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
C = input().split()

# カウントチェック
count = Counter(C)

# 最大値
m_count = max(count.values())

# 個数から最大値を引いた数だけ書き換え必要
print(N - m_count)
