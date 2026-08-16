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

# N ボールの数
# M 色の数
N, M = map(int,input().split())

c_dict = {}

for i in range(1,N+1):
    C, S = map(int,input().split())
    c_dict[C] = max(c_dict.get(C, -1), S) # -1 は存在しない場合の逃し数値

ans = []
for i in range(1, M+1):
    ans.append(c_dict.get(i, -1))

print(' '.join(map(str, ans)))
