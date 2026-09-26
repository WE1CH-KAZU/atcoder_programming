"""
提出間に合わず
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

def sosu_judge(n):
    # 素数かどうかを判定する
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

N, Q = map(int, input().split())

iro = ["a"]*(N)
tairu = ["."]*(N)

tairu_kioku = set(range(N))

saigo_iro = "a"
saigo_bango = -1
bango = [-1]*N

for q in range(Q):
    q1, q2 = input().split()
    q1 = int(q1)
    if q1 == 1:
        q2 = int(q2)
        q2 = q2 -1
        if tairu[q2] == "#":
            # 取り除く
            tairu[q2] = "."
            bango[q2] = q
        elif tairu[q2] == ".":
            # おく
            # タイルが置かれているかどうか関係がないから色を決める
            if saigo_bango > bango[q2]:
                iro[q2] = saigo_iro
            tairu[q2] = "#"
    
    if q1 == 2:
        saigo_iro = q2
        saigo_bango = q

for n in range(N):
    # タイルが"."かつ最後までタイルがない番号に色を確定
    if tairu[n] == "." and saigo_bango > bango[n]:
        iro[n] = saigo_iro


# for q in range(Q):
#     q1, q2 = input().split()
#     q1 = int(q1)
#     if q1 == 1:
#         q2 = int(q2)
#         q2 = q2-1
#         if tairu[q2] == "#":
#             # 取り除く
#             tairu[q2] = "."
#             tairu_kioku.add(q2)
#         elif tairu[q2] == ".":
#             tairu[q2] = "#"
#             tairu_kioku.discard(q2)

#     if q1 == 2:
#         for i in tairu_kioku:
#             iro[i] = q2
#         tairu_kioku = set()


print("".join(iro))
