"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import permutations

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

N = int(input())

init = 10000
oturi = 0
shusshi = 0
less = 0
kaimono = 0
for _ in range(1, N+1):
    A, B, S = input().split()
    A = int(A)
    B = int(B)
    shusshi += B
    kaimono += A
    less += B - A
    if S == 'take':
        oturi += B - A

# X : この入力に対する残金
# Y : 全てお釣りを受け取っていた場合の残金
# =====
# 下の数式を見ると結局oturi, lessの差分になっているので、それを計算すれば良かっただけ
# =====
X = init - shusshi + oturi
Y = init - shusshi + less

res = Y - X
print(res)
