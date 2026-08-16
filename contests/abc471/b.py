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

ans_set = Counter()

for i in range(1, N+1):
    ans = input().strip()
    ans = ans.lower()
    ans_set[ans] += 1

count = max(ans_set.values())

print(count)