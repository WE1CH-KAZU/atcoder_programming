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

N, K = map(int, input().split())

A = list(map(int, input().split()))
S = sorted(A)

hantei = [0] * N
for i in range(N):
    if A[i] != S[i]:
        hantei[i] = 1

indx = [i for i in range(N) if hantei[i] == 1]
if len(indx) == 0:
    print("Yes")
    sys.exit()

L = indx[0]
R = indx[-1]

if (R - L + 1) > K:
    print("No")
    sys.exit()

print("Yes")
