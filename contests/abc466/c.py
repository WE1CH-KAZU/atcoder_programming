"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import permutations # 順列組み合わせ
from itertools import combinations # i<jの組み合わせ

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

N = int(input())

ans = 0
right = 1  # 距離1以下でいられる右端。iを進めても戻らない
for i in range(1, N + 1):
    right = max(right, i)
    # right+1 まで届くか聞き、届く限り伸ばす
    while right < N:
        print('?', i, right + 1, flush=True)
        if input().strip() != 'Yes':
            break
        right += 1
    ans += right - i

print('!', ans, flush=True)
