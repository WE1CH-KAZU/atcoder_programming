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

# dictのvalueの関数を指定、list
receive = defaultdict(list)

for i in range(1, N+1):
    K, *A = map(int,input().split())
    for a in A:
        # 人 a が受け取ったリストに、送り主 i を追加
        receive[a].append(i)

for i in range(1, N+1):
    # 人 i が受け取った数(len)と、その送り主一覧
    print(len(receive[i]), *receive[i])

