"""
制限時間内に解けなかった。
手法も正しくない。差分最小値の商品を複数回買うことを考慮したモデルに変更が必要
"""

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

# T: ループ回数
T = int(input())


for _ in range(T):
    N = int(input())
    A_list = [0] * (N)
    B_list = [0] * (N)
    for i in range(N):
        A, B = map(int, input().split())
        A_list[i] = A
        B_list[i] = B
    takai_souwa = sum(A_list)

    nebiki = [a-b for a, b in zip(A_list, B_list)]
    nebiki.sort(reverse=True)
    coupon = N // 2
    takai_souwa -= sum(nebiki[:coupon])
    # print(takai_souwa, coupon, nebiki)
    print(takai_souwa)

