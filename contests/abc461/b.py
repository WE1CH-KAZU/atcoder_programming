import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

N = int(input())

# A=斧の番号
# B=木こりの番号
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i+1 != B[A[i]-1]:
        print('No')
        break
    ans+=1

if ans == N:
    print('Yes')
