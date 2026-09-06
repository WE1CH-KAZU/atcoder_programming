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

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [a - b for a, b in zip(A, B)]

# 組み合わせ一つを返せば良いので、最大値を返すことにする
ans = [0]* (N)
W = [0] * (N)
for i in range(len(C)):
    if C[i] >0:
        W[i] = INF
        ans[i] = C[i] * W[i]
    if C[i] < 0:
        W[i] = 1
        ans[i] = C[i] * W[i]
    if C[i] == 0:
        W[i] = 1
        ans[i] = C[i] * W[i]

if sum(ans) > 0:
    print("Yes")
    print(*W)
else:
    print("No")

