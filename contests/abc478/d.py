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

def sosu_judge(n):
    # 素数かどうかを判定する
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

N, Q = map(int, input().split())

# 一旦保存
nyuryoku_x = defaultdict(list)
for _ in range(Q):
    L, R, X = map(int, input().split())
    nyuryoku_x[X].append((L, R))

kukan = [0] * (N + 2)

for x, ranges in nyuryoku_x.items():
    ranges.sort()
    # 個別に取り出す
    zero_l, zero_r = ranges[0]
    for l, r in ranges[1:]:
        if zero_r < l:
            # 離れてる
            kukan[zero_l] += 1
            kukan[zero_r + 1] -= 1
            zero_l, zero_r = l, r
        else:
            zero_r = max(zero_r, r)
    kukan[zero_l] += 1
    kukan[zero_r + 1] -= 1

ima = 0
sowa = []
for i in range(1, N+1):
    ima += kukan[i]
    sowa.append(ima)

print(*sowa)
