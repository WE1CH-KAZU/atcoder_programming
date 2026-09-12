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

ichi = 0
juu = 0
hyaku = 0

A = list(map(int, input().split()))


for i in range(N):
    temp = -(-A[i] // 1000)
    otsuri = temp*1000 - A[i]
    hyaku += otsuri // 100
    otsuri %= 100
    juu += otsuri // 10
    otsuri %= 10
    ichi += otsuri

print(ichi, juu , hyaku)

    