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

N, V = map(int, input().split())

W = list(map(int, input().split()))

ans = 0
for a, b, c in permutations(enumerate(W, 1), 3):
    if a[0] + b[0] + c[0] <= V:
        kakaku = a[1] + b[1] + c[1]
        ans = max(ans, kakaku)

print(ans)
