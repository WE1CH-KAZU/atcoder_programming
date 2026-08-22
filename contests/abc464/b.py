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

# pixcel H: height, W: width
# 左上が(H,W)=(1,1)
H, W = map(int, input().split())

temp = []
h_min = INF
h_max = -1
for i in range(H):
    C = list(input().strip())
    if '#' in C:
        h_min = min(h_min, i)
        h_max = max(h_max, i)
    temp.append(C)


# 転置
temp_t = list(zip(*temp))

w_min = INF
w_max = -1
for i in range(W):
    C = temp_t[i]
    if '#' in C:
        w_min = min(w_min, i)
        w_max = max(w_max, i)

for row in temp[h_min:h_max+1]:
    print(''.join(row[w_min:w_max+1]))
