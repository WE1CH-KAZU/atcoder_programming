import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace
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

N = int(input())

A_list = list(map(int, input().split()))

fir, sec, thr = sorted(A_list[:3], reverse=True)
ans = [thr]

for a in A_list[3:]:
    if a > fir:
        fir, sec, thr = a, fir, sec
    elif a > sec:
        sec, thr = a, sec
    elif a > thr:
        thr = a
    ans.append(thr)

print("\n".join(map(str, ans)))

